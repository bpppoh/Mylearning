import cv2
import numpy as np
from image_process import image_show , calculate_hist , powerGamma

img = cv2.imread('./pic2.png',0)
print(f"img min : {np.min(img)} , img max : {np.max(img)}")
image_show(img)

# Output >> img min : 76 , img max : 218
# ทราบได้ว่า ความเข้มของภาพ ค่อนข้างสว่าง เนื้อจากจุดภาพที่มีความเข้มที่ต่ำที่สุด มีความเข้มถึง 76 ส่งผลให้ภาพสว่างเกินไป
# ต้องปรับภาพให้กระจายตัวเต็ม Scale 0-255 เพื่อให้ภาพมีมิติมากยิ่งขึ้น

hist = calculate_hist(img,"assignment1_2","hist_before_powergamma.jpg")
# Output สังเกตได้ว่า

img_new = powerGamma(img,2.2)

print(f"img_new min : {np.min(img_new)} , img_new max : {np.max(img_new)}")
# img_new min : 0 , img_new max : 255
image_show(img_new)

hist = calculate_hist(img_new,"assignment1_2","hist_after_powergamma.jpg")

concatImg = cv2.hconcat([img,img_new])
cv2.imwrite('./assignment1_2/assignment1_2.jpg',concatImg)