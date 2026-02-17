import cv2
import numpy as np
from image_process import image_show, calculate_hist , equalization , powerGamma

img = cv2.imread('pic2.png', 0)
cv2.imwrite("./assignment1_2/original_img.jpg",img)

image_show(img)
calculate_hist(img)

equalized_img = equalization(img)

image_show(equalized_img)
calculate_hist(equalized_img)

cv2.imwrite("./assignment1_2/equalized_img.jpg",equalized_img)
hconcat_img = cv2.hconcat([img,equalized_img])

cv2.imwrite("./assignment1_2/final.jpg",hconcat_img)