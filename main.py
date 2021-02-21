import pickle
import numpy
f = open('D:\download\mini-imagenet-cache-train.pkl','rb')
data = pickle.load(f)
print(data)
# import os.path as osp
# THIS_PATH = osp.dirname(__file__)
# ROOT_PATH1 = osp.abspath(osp.join(THIS_PATH, '..', '..', '..'))
# ROOT_PATH2 = osp.abspath(osp.join(THIS_PATH, '..', '..'))
# IMAGE_PATH = osp.join(ROOT_PATH1, 'FEAT/data/cub/CUB_200_2011/images')
# SPLIT_PATH = osp.join(ROOT_PATH2, 'data/cub/split')
# def parse_csv(self, txt_path):
#     data = []
#     label = []
#     lb = -1
#     self.wnids = []
#     lines = [x.strip() for x in open(txt_path, 'r').readlines()][1:]
#
#     for l in lines:
#         context = l.split(',')
#         name = context[1] + '/' + context[0]
#         wnid = context[1]
#         path = osp.join(IMAGE_PATH, name)
#         if wnid not in self.wnids:
#             self.wnids.append(wnid)
#             lb += 1
#
#         data.append(path)
#         label.append(lb)
#
#     return data, label
# txt_path = osp.join(SPLIT_PATH, setname + '.csv')
# data, label = parse_csv(txt_path)