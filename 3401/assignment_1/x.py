import cv2
import numpy as np
from image_process import calculate_hist , sobel , powerGamma ,equalization , image_show

img = cv2.imread('./pic3.png',0)
listHist = []
out = [img]
listHist.append(calculate_hist(out[-1]))

out.append(powerGamma(out[-1],2))
listHist.append(calculate_hist(out[-1]))

out.append(equalization(out[-1],listHist[-1].flatten()))
listHist.append(calculate_hist(out[-1]))

out.append(sobel(out[-1]))

concat_img = cv2.hconcat([out[0],out[1],out[2],out[3]])
image_show(concat_img)
cv2.imwrite('./assignment1_3/assignment1_3.jpg',concat_img)