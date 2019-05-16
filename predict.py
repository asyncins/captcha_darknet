import os
from pathlib import Path

from settings import *

# 配置
instruct = 'test'
data = 'captcha.data'
cfg = 'train.cfg'
weights = 'train_final.weights'
predicts = list(Path(PATH_PREDICTS).glob('*.{}'.format(IMAGE_TYPE)))
if not os.path.isdir(PATH_OUT):
    # out目录存储输出图片，如果目录不存在则创建
    os.makedirs(PATH_OUT)
if not os.path.isdir(PATH_COO):
    # coo目录存储输出坐标，如果目录不存在则创建
    os.makedirs(PATH_COO)
# 循环检测
for i in predicts:
    out = os.path.join(PATH_OUT, str(i.name))
    coo = os.path.join(PATH_COO, str(i.stem) + '.txt')
    command = 'cd darknet && ./darknet detector {instruct} data/{data} cfg/{cfg}' \
              ' weights/{weights} -out {out} -coo {coo} {i} -thresh 0.5 -gpus 0 ' \
              .format(instruct=instruct, data=data, cfg=cfg,
                      weights=weights, out=out, coo=coo, i=i)
    os.system(command)