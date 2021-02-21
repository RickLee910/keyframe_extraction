import numpy as np
import cv2

cap = cv2.VideoCapture('pikachu.mp4')
bb = 4  # 分块数
rcc_rate = 0.6  # RCC相关系数的阈值
rcc_windows = 11  # 卷积平滑窗口


# 接下来要用的函数

# 分块计算像素亮度的定序测度Rank矩阵
def imgblock(mat):
    r = mat.shape[0] // bb
    w = mat.shape[1] // bb
    t = np.zeros(bb * bb)
    for R in range(bb):
        for W in range(bb):
            ll = R * r
            lr = (R + 1) * r
            rl = W * w
            rr = (W + 1) * w
            t[R * bb + W] = np.sum(mat[ll:lr, rl:rr]) / (r / bb * w / bb)
    res = np.argsort(t)
    res += 1
    res = res.reshape((bb, bb))
    # print(res)
    return res


# 计算两帧之间的RCC系数
def RCC(mata, matb):
    diff = np.sum(np.square(mata - matb))  ##计算平方差，两帧之间的欧式距离
    N = bb * bb
    rcc = 1 - 6 * diff / (N * (N ** 2 - 1))
    print(rcc)
    return rcc


# 卷积光滑
def smooth(npary, windows):
    len_npary = npary.shape[0]
    res = np.zeros(npary.shape)
    for k in range(len_npary):
        for i in range(bb):
            for j in range(bb):
                l = max(0, k - windows // 2)
                r = min(npary.shape[0], k + windows // 2)
                res[k, i, j] = np.sum(npary[l:r + 1, i, j]) / (windows)
    return res


# 提取帧的预处理部分
index = 0
time = 0  # 用于指定帧的时长
L = []

# 提取帧
while (cap.isOpened()):
    cap.set(cv2.CAP_PROP_POS_MSEC, time)
    ret, img = cap.read()  # 获取图像
    # cv2.imshow("00"+str(index),img)
    # cv2.waitKey()
    if not ret:  # 如果获取失败，则结束
        print("exit")
        break
    img0 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 转换成灰度图
    tmp = np.array(img0)
    L.append(imgblock(tmp))
    time += 20  # 设置每隔50ms读取帧
    index += 1
    print(index)  # 便于观看进度
#    if index > 20 :
#        break

# 转换成numpy矩阵，并且初始化flag矩阵，表示是否是关键帧
L = np.array(L)
flag = np.zeros(L.shape[0])
L = smooth(L, rcc_windows)

pre = 0
for i in range(L.shape[0] - 1):
    if RCC(L[i], L[i + 1]) < rcc_rate:
        if i - pre >= 10:
            flag[i] = 1
        pre = i
index = 0
time = 0
num = 0

dir = './extract_result/'
while (cap.isOpened()):
    cap.set(cv2.CAP_PROP_POS_MSEC, time)
    ret, img = cap.read()  # 获取图像
    # cv2.imshow("00"+str(index),img)
    # cv2.waitKey()
    if not ret:  # 如果获取失败，则结束
        print("exit")
        break
    if flag[index] == 1:

        name = 'frame_' + str(num) + '.jpg'
        cv2.imwrite(dir + name, img)  # 保存关键帧
        num += 1
    time += 50  # 设置每隔50ms读取帧
    index += 1

