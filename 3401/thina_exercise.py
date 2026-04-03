import cv2
import numpy as np
import matplotlib.pyplot as plt
from assignment_3.image_process import *

img = imread('./image/bank4.jpg',1)
h,s,v = cv2.split(rgb2hsv(img))
mask_1 = (h > 120)

uint8_s = (s * 255.).astype(np.uint8)
thr = intermean_method(uint8_s,2)
mask_2 = uint8_s > thr

out = img.copy()
out[~(mask_1 & mask_2)] = [255,255,255]
image_show(out)