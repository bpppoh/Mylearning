import cv2
import numpy as np
from image_process import powerGamma,image_show,calculate_hist
import matplotlib.pyplot as plt

img = cv2.imread('pic1.png', 1)
image_show(img)
calculate_hist(img)

plt.figure(figsize=(12,4))
row , col , channel = img.shape
color_img = np.zeros_like(img,dtype='uint8')
for space in range(channel) :
    color_img[:,:,space] = powerGamma(img[:,:,space],0.4)
    plt.subplot(1,channel,space+1)
    plt.plot(cv2.calcHist([img],[space],None,[256],[0,256]))
plt.show()

hconcat_img = cv2.hconcat([img,color_img])
image_show(hconcat_img)
cv2.imwrite("./assignment1_1/final.jpg",hconcat_img)
