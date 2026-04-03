from assignment_3.image_process import *
import numpy as np
import cv2

img = imread('./image/dark2.png',0)
image_show(img)
show_hist(calculate_hist(img))

img_float = img.astype('float16')
c = 255 / np.log(1 + np.amax(img_float))
out = c * np.log(1 + img_float)
out = out.astype(np.uint8)

image_show(out)
show_hist(calculate_hist(out))