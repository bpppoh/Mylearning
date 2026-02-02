import cv2
import numpy as np

img = cv2.imread('pic1.png', 1)
print(img.shape)
# หาก img.shape เป็น numpy array 2 มิติ จะเป็นภาพ Grayscale
# หาก img.shape เป็น numpy array 3 มิติ จะเป็นภาพสี

B , G , R = cv2.split(img)
# ใช้ method cv2.split(img) จะ return เป็น B G R channels

new_img = np.zeros_like(B)
# ใช้ method np.zeros_like(..) เพื่อ clone Structure ของ argument ที่เราใส่เข้าไป
# กรณีนี้ใส่ B หรือ G หรือ R เข้าไป ก็จะเป็นการโคลน structure (height,width) เนื่องจาก B/G/R จะเป็น 1 channel

for i in range(img.shape[0]) :
    for j in range(img.shape[1]) :
        new_img[i,j] = int((0.299 * R[i,j]) + (0.587 * G[i,j]) + (0.114 *B[i,j]))
        # เข้าถึง B/G/R ในแต่ละช่องจุดภาพ แล้วคูณด้วย const แล้วนำมาพวกกันเพื่อแปลงเป็นภาพขาวดำ
        
print(f"min : {np.min(new_img)} , max : {np.max(new_img)}")
# min : 0 , max : 80
# max มีเพียง 80 แสดงว่าภาพมืด ฉะนั้นต้องนำไปขยาย scale

new_img_poweredGamma = (((new_img.astype('float')/np.max(new_img))**0.25)*255).astype('uint8')
concatImg = cv2.hconcat([new_img,new_img_poweredGamma])
cv2.imwrite("assignment1_1.jpg",concatImg)
# แปลงข้อมูลเป็น float >> Normalize >> ยกกำลังด้วย gamma (ยิ่งน้อย ยิ่งสว่าง) >> คูณด้วย 255 แล้วแปลงกลับเป็น uint8