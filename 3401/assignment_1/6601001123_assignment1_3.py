import cv2
import numpy as np
from image_process import calculate_hist , sobel , powerGamma ,equalization , image_show

img = cv2.imread('./pic3.png',0)
out = [img]
image_show(out[-1])
listHist = []
listHist.append(calculate_hist(out[-1]))
edgeList = []

edgeList.append(sobel(out[-1]))

out.append(powerGamma(out[-1],2))
image_show(out[-1])
listHist.append(calculate_hist(out[-1]))
edgeList.append(sobel(out[-1]))

out.append(equalization(out[-1],listHist[-1]))
image_show(out[-1])
listHist.append(calculate_hist(out[-1]))
edgeList.append(sobel(out[-1]))

showimg = cv2.vconcat([cv2.hconcat(out),cv2.hconcat(edgeList)])
image_show(showimg)
cv2.imwrite('./assignment1_3/assignment1_3.jpg',showimg)