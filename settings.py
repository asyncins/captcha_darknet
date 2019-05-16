import pathlib
from os import path


# 路径
PARENT_LAYER = pathlib.Path.cwd().parent

# 图片路径
PATH_PARENT = path.join(PARENT_LAYER, 'data')
PATH_IMAGES = path.join(PATH_PARENT, 'images')
PATH_PREDICTS = path.join(PATH_PARENT, 'predict')
PATH_OUT = path.join(PATH_PARENT, 'out')
PATH_COO = path.join(PATH_PARENT, 'coo')
# 文件路径
PATH_TRAIN = path.join(PATH_PARENT, 'train.txt')
PATH_LABELS = path.join(PATH_PARENT, 'labels')
PATH_PREDICT = path.join(PATH_PARENT, 'predict.txt')

FILE_TYPE = 'xml'
IMAGE_TYPE = 'png'
CLASSES = ['text']
