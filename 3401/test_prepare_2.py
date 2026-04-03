from assignment_3.image_process import *
import numpy as np
import cv2

img = imread('./image/document1.png',0)
image_show(img)
splitList = split_image(img)

intermean_round = [1,1,2,1]
noise = [0,0,0,1]
inv = [1,0,0,1]
out = []

for i in range(len(splitList)) :
    pic = cv2.medianBlur(splitList[i],3) if noise[i] else splitList[i]
    pic = 255 - pic if inv[i] else pic
    thr = intermean_method(pic,intermean_round[i])
    out.append(((pic < thr)*255).astype(np.uint8))
    
image_show(cv2.vconcat([cv2.hconcat(out[:2]),cv2.hconcat(out[2:])]))