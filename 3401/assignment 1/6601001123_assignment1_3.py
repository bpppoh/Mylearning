import cv2
import numpy as np
import matplotlib.pyplot as plt
import image_process

# def sobel(img) :
#     mask_gx = np.array([[-1,0,1],[-2,0,2],[-1,0,1]] , dtype='float16')
#     mask_gy = np.array([[-1,-2,-1],[0,0,0],[1,2,1]] , dtype='float16')
#     gx = cv2.filter2D(img,cv2.CV_64F,mask_gx)
#     gy = cv2.filter2D(img,cv2.CV_64F,mask_gy)
#     out = np.sqrt(gx**2 , gy**2)
#     out = np.clip(out,0,255).astype('uint8')
#     return out

# Import image into programme
img = cv2.imread('./pic3.png',0)
print(f"min : {np.min(img)} , max : {np.max(img)}")
# Output >>  min : 43 , max : 255
# Can normalizing the image

hist = image_process.calculate_hist(img)
# Investigate histogram 
# พบว่า ความถี่กระจุกตัวอยู่ในช่วงความเข้ม 170 - 240
# จึงสามารถใช้การ Power Gamma เพื่อกระจายการกระจุกตัวได้

# ปรับฐานความเข้มของรูปภาพ ให้อยู่ที่ 0
new_img = img - np.min(img)
# Normalize and Power Gamma
new_img = (((new_img.astype('float16')/np.max(new_img))**3.5)*255).astype('uint8')


print(f"min : {np.min(new_img)} , max : {np.max(new_img)}")
# Output : min : 0 , max : 255

hist = image_process.calculate_hist(new_img)
# Investigate histogram after Normalize and PowerGamma
# พบว่า ความถี่กระจายตัวอย่างสม่ำเสมอแล้ว

new_img = image_process.sobel(new_img)
# ดำเนินการ prewitt (Edge Detection)

concat_img = cv2.hconcat([img,new_img])
cv2.imwrite('assignment1_3.jpg',concat_img)