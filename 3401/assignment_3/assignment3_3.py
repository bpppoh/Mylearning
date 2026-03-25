from image_process import imread , rgb2hsv , image_show
import numpy as np
import cv2

img = imread('./cells.tif',1)
h,s,v = rgb2hsv(img)
image_show(img)

out = np.zeros_like(h,dtype='uint8')
mask = (h >= 140) & (h <= 230)
out[mask] = 255
out = cv2.medianBlur(out,3)
image_show(out)