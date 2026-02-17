import cv2
import numpy as np
from image_process import calculate_hist , sobel , powerGamma ,equalization

img = cv2.imread('./pic3.png',0)

calculate_hist(img,"assignment1_3","hist_before_powergamma.jpg")
powergamma_img = powerGamma(img,2)

calculate_hist(powergamma_img,"assignment1_3","hist_after_powergamma.jpg")

equalized_img = equalization(powergamma_img)
calculate_hist(equalized_img,"assignment1_3","hist_after_equalization.jpg")
edge_detected_img = sobel(equalized_img)

concat_img = cv2.hconcat([img,powergamma_img,equalized_img,edge_detected_img])
cv2.imwrite('./assignment1_3/assignment1_3.jpg',concat_img)