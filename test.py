import pickle
import random
phase = 'train'
data_path ='D:\download\mini-imagenet-cache-train.pkl'
data, labels = pickle.load(open(data_path, 'rb'))
random.seed(2019)
random_idxes = range(len(data))
random.shuffle(random_idxes)
num_train = int(len(data) * 0.9)
if phase == 'pretrain_train':
    data = [data[i] for i in random_idxes[:num_train]]
    labels = [labels[i] for i in random_idxes[:num_train]]
elif phase == 'pretrain_val':
    data = [data[i] for i in random_idxes[num_train:]]
    labels = [labels[i] for i in random_idxes[num_train:]]