import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('./pic2.png',0)
print(f"img min : {np.min(img)} , img max : {np.max(img)}")
# Output >> img min : 76 , img max : 218
# ทราบได้ว่า ความเข้มของภาพ ค่อนข้างสว่าง เนื้อจากจุดภาพที่มีความเข้มที่ต่ำที่สุด มีความเข้มถึง 76 ส่งผลให้ภาพสว่างเกินไป
# ต้องปรับภาพให้กระจายตัวเต็ม Scale 0-255 เพื่อให้ภาพมีมิติมากยิ่งขึ้น

hist = cv2.calcHist([img],[0],None,[256],[0,256])
plt.plot(hist)
plt.show()

img_new = img - np.min(img)
img_new = (img_new.astype('float')/np.max(img_new) * 255.0).astype('uint8')
print(f"img_new min : {np.min(img_new)} , img_new max : {np.max(img_new)}")
# Output >> img_new min : 0 , img_new max : 255

hist = cv2.calcHist([img_new],[0],None,[256],[0,256])
plt.plot(hist)
plt.show()
concatImg = cv2.hconcat([img,img_new])
cv2.imwrite('assignment1_2.jpg',concatImg)
print(np.min(img_new))