import cv2
import numpy as np
from image_process import powerGamma,calculate_hist,image_show,equalization

img = cv2.imread('pic1.png', 1)
cv2.imwrite("./assignment1_1/original_img.jpg",img)

row , col , channel = img.shape
color_img = np.zeros_like(img,dtype='uint8')
for space in range(channel) :
    color_img[:,:,space] = powerGamma(img[:,:,space],0.4)
    # color_img[:,:,space] = equalization(img[:,:,space])

cv2.imwrite("./assignment1_1/color_after_powergamma.jpg",color_img)
hconcat_img = cv2.hconcat([img,color_img])
cv2.imwrite("./assignment1_1/final.jpg",hconcat_img)
