import os
import cv2
import chardet
import unicodedata
import numpy as np
from time import sleep

os.system("clear")

fileName = input('[INPUT] 파일 이름 입력: ')

inputList = os.listdir('input/')
inputCount = 0
for num in range(0, len(inputList), 1):
    if fileName in unicodedata.normalize('NFC', inputList[num]): inputCount += 1

getImg = []
for num in range(0, inputCount, 1):
    getImg.append(cv2.imread(f'input/{fileName}-{num + 1}.jpg'))

height = 0
for num in range(0, len(getImg), 1):
    height += len(getImg[num])

mergeImg = np.zeros(shape=(height, 1920, 3), dtype=getImg[0].dtype)

pointer = 0
for numA in range(0, len(getImg), 1):
    for numB in range(pointer, pointer + len(getImg[numA]), 1):
        mergeImg[numB] = getImg[numA][numB - pointer]
    pointer += len(getImg[numA])

cv2.imwrite(f'output/{fileName}-merge.jpg', mergeImg)

cropImg = []
for num in range(0, int(len(mergeImg) / 2560), 1):
    cropImg.append(np.zeros(shape=(2560, 1920, 3), dtype=getImg[0].dtype))
if len(mergeImg) % 2560 != 0:
    cropImg.append(np.zeros(shape=((len(mergeImg) % 2560), 1920, 3), dtype=getImg[0].dtype))

for num in range(0, len(mergeImg), 1):
    cropImg[int(num / 2560)][num % 2560] = mergeImg[num]

for num in range(0, len(cropImg), 1):
    cv2.imwrite(f'output/{fileName}-{num}.jpg', cropImg[num])