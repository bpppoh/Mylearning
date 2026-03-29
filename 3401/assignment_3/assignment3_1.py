from image_process import image_show , rgb2hsv , saturation_adjust 
import cv2
import numpy as np

img = cv2.imread('./shade.png',cv2.IMREAD_COLOR)
hsv_img = rgb2hsv(img)
hsv_img = saturation_adjust(hsv_img,0.35,180,270)
out = (cv2.cvtColor(hsv_img.astype('float32'),cv2.COLOR_HSV2BGR)*255).astype('uint8')
image_show(cv2.hconcat([img,out]));