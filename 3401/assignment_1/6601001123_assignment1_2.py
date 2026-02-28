import cv2
import numpy as np
from image_process import image_show, calculate_hist , equalization , powerGamma

img = cv2.imread('pic2.png', 0)
image_show(img)
out = [img]
listHist = []

listHist.append(calculate_hist(img,"assignment1_2","hist_before_equalized.jpg"))

out.append(equalization(out[-1],listHist[-1]))
image_show(out[-1])
listHist.append(calculate_hist(out[-1]))

hconcat_img = cv2.hconcat(out)
image_show(hconcat_img)
cv2.imwrite("./assignment1_2/final.jpg",hconcat_img)