import cv2
import numpy as np
import matplotlib.pyplot as plt
import image_process

img = cv2.imread('./pic2.png',0)
print(f"img min : {np.min(img)} , img max : {np.max(img)}")
image_process.image_show(img)

# Output >> img min : 76 , img max : 218
# ทราบได้ว่า ความเข้มของภาพ ค่อนข้างสว่าง เนื้อจากจุดภาพที่มีความเข้มที่ต่ำที่สุด มีความเข้มถึง 76 ส่งผลให้ภาพสว่างเกินไป
# ต้องปรับภาพให้กระจายตัวเต็ม Scale 0-255 เพื่อให้ภาพมีมิติมากยิ่งขึ้น

hist = image_process.calculate_hist(img)

img_new = img - np.min(img)
# img_new = ((img_new.astype('float')/np.max(img_new)**1.025) * 255.0).astype('uint8')
img_new = image_process.powerGamma(img_new,1.2)
print(f"img_new min : {np.min(img_new)} , img_new max : {np.max(img_new)}")
# Output >> img_new min : 0 , img_new max : 255
image_process.image_show(img_new)

hist = image_process.calculate_hist(img_new)

concatImg = cv2.hconcat([img,img_new])
cv2.imwrite('assignment1_2.jpg',concatImg)