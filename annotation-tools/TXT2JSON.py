import cv2
import sys
import numpy as np
import os
from glob import glob

from math import cos, sin
from os.path import isfile, splitext, basename, isdir
from os import makedirs
import json

img_files_path = r'G:\DeepLearning\LCNN\lcnn\annotation-tools\img'

img_files = glob('%s/*.txt' % img_files_path)
# img_files_path = os.path.join("./img/")
# img_files = os.listdir(img_files_path)

writePath = './train.json'

with open(writePath, 'w') as fo:
    label = []
    for i in range(len(img_files)):
        dic = {}
        dic["filename"] = img_files[i][len(img_files_path) + 1:-4] + '.png'
        print(img_files[i][:-4] + '.png')
        im = cv2.imread(img_files[i][:-4] + '.png')
        h, w, _ = im.shape
        # print(w,h)
        lines = []
        with open(img_files[i], 'r') as fi:
            lines = []
            for line in fi:
                line = line.split(',')
                # print(line)
                # print(img_files[i][len(img_files_path)+1:])
                # print(int(len(line)/4))
                # for j in range(int(len(line)/4)):
                # 	t = 4*j
                lines.append([int(float(line[1]) * w), int(float(line[3]) * h), int(float(line[2]) * w),
                              int(float(line[4]) * h)])
            # print(lines)
            # os.system('pause')
        dic["lines"] = lines
        dic["height"] = h
        dic["width"] = w
        label.append(dic)
    json.dump(label, fo)