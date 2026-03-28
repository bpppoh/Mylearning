from image_process import image_show , rgb2hsv , saturation_adjust 
import cv2
import numpy as np

img = cv2.imread('./shade.png',cv2.IMREAD_COLOR)
h,s,v = rgb2hsv(img)
h,s,v = saturation_adjust(h,s,v,0.35,180,270)
out = (cv2.cvtColor(np.stack((h, s, v), axis=2).astype('float32'),cv2.COLOR_HSV2BGR)*255).astype('uint8')
image_show(cv2.hconcat([img,out]))