from image_process import imread , image_show , bgr2cmyk
import numpy as np
import cv2

img = imread('./cells.tif',1)
cmyk_img = bgr2cmyk(img)
c,m,y,k = cv2.split(cmyk_img)
mask = (c >  y)  &  (c > m)
out = np.zeros_like(img,dtype=np.uint8)
out[mask] = 255
out = cv2.medianBlur(out,13)
image_show(out) 