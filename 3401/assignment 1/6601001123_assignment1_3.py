import cv2
import numpy as np
from image_process import calculate_hist , sobel , powerGamma

# Import image into programme
img = cv2.imread('./pic3.png',0)
print(f"min : {np.min(img)} , max : {np.max(img)}")
# Output >>  min : 43 , max : 255
# Can normalizing the image

hist = calculate_hist(img,"assignment1_3","hist_before_powergamma.jpg")
# Investigate histogram 
# พบว่า ความถี่กระจุกตัวอยู่ในช่วงความเข้ม 170 - 240
# จึงสามารถใช้การ Power Gamma เพื่อกระจายการกระจุกตัวได้

# ปรับฐานความเข้มของรูปภาพ ให้อยู่ที่ 0
# Normalize and Power Gamma
new_img = powerGamma(img,2)


print(f"min : {np.min(new_img)} , max : {np.max(new_img)}")
# Output : min : 0 , max : 255

hist = calculate_hist(new_img,"assignment1_3","hist_after_powergamma.jpg")
# Investigate histogram after Normalize and PowerGamma
# พบว่า ความถี่กระจายตัวอย่างสม่ำเสมอแล้ว

# blurred_img = new_img
blurred_img = cv2.GaussianBlur(new_img, (3, 3), 0)
edge_detected_img = sobel(blurred_img)
# ดำเนินการ prewitt (Edge Detection)

concat_img = cv2.hconcat([img,new_img,blurred_img,edge_detected_img])
cv2.imwrite('./assignment1_3/assignment1_3.jpg',concat_img)