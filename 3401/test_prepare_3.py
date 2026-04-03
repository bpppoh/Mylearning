from assignment_3.image_process import *
import numpy as np
import cv2

img = imread('./image/document2.jpg',0)
img = 255 - img
image_show(img)
splitList = split_image(img,6)
out = []

for i in range(len(splitList)) :
    pic = splitList[i]
    print(np.amin(pic) , np.amax(pic))
    pic = log_transformation(pic)
    thr = intermean_method(pic,4)
    out.append(((pic < thr) * 255).astype(np.uint8))

image_show(merge_image(out))