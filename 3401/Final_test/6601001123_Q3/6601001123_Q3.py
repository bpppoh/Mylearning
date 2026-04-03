from image_tool import *
import cv2
import numpy as np

img = imread('./cells.tif',1)
image_show(img)
b,g,r = cv2.split(img)
c,m,y,k = cv2.split(bgr2cmyk(img))
mask = (c > y)
mask_pic = (mask*255).astype(np.uint8)
r[mask] = np.clip(r[mask] + ((g[mask]*0.5870) + (b[mask]*0.1140))/2,0,255)
g[mask] = 0
b[mask] = 0
out = np.stack([b,g,r],axis=2)
imwrite("mask_pic.jpg",image_show(mask_pic))
imwrite("output.jpg",image_show(out))
imwrite("output_compare.jpg",image_show(cv2.hconcat([img,out])))
