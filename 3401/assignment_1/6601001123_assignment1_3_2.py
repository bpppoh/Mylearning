import cv2
from image_process import sobel, powerGamma, equalization, image_show

out = [cv2.imread('./pic3.png',0)]
out.append(powerGamma(out[-1],2.5))
out.append(equalization(out[-1]))
edgeList = [sobel(pic) for pic in out]
image_show(cv2.vconcat([cv2.hconcat(out),cv2.hconcat(edgeList)]))