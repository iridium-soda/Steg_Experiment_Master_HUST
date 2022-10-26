import cv2
import numpy as np
import math
def main():
    path = "lena512.bmp"
    wstr = ""
    rpath = "result.bmp"
    img = cv2.imread(path)
    embedwater(img, wstr, rpath)
    result = extrawater(rpath)
    print(result)