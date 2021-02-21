import cv2

# vidcap = cv2.VideoCapture('test_video.avi')
# success,image = vidcap.read()
# count = 0
# success = True
# while success:
#     success,image = vidcap.read()
#
#     cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file
#     if cv2.waitKey(10) == 27:
#         break
#     count += 1

def images_to_video():
    fps = 30  # 帧率
    num_frames = 1768
    img_array = []

    # img_width = 0
    # img_height = 0
    for i in range(num_frames + 1):
        filename = "./extract_result/keyframe_" + str(i) + ".jpg"
        img = cv2.imread(filename)

        if img is None:
            print(filename + " is non-existent!")
            continue
        imgInfo = img.shape
        size = (imgInfo[1], imgInfo[0])
        img_array.append(img)

    out = cv2.VideoWriter('demo.avi', cv2.VideoWriter_fourcc(*'XVID'), fps, size)

    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()


def main():
    images_to_video()


if __name__ == "__main__":
    main()