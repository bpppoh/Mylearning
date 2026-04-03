from assignment_3.image_process import *
import numpy as np
import cv2

img = cv2.imread('./image/shade.png',cv2.IMREAD_COLOR)

h,s,v = cv2.split(rgb2hsv(img))
mask_purple = (h > 240)
v[mask_purple] = 0.0

s_uint8 = (s * 255.).astype(np.uint8)
thr = intermean_method(s_uint8,1)
mask_red_green = (h < 180) & (s_uint8 > thr)
s[mask_red_green] = 0.0
v[mask_red_green] = 0.0

out = (cv2.cvtColor(np.stack([h,s,v],axis=2).astype('float32'), cv2.COLOR_HSV2BGR)*255).astype('uint8')
image_show(out)