import cv2
import numpy as np
import matplotlib.pyplot as plt

def prewitt(img) :
    # img = cv2.GaussianBlur(img, (5, 5), 0)
    mask_gx = np.array([[-1,0,1],[-2,0,2],[-1,0,1]] , dtype='float16')
    mask_gy = np.array([[-1,-2,-1],[0,0,0],[1,2,1]] , dtype='float16')
    gx = cv2.filter2D(img,cv2.CV_64F,mask_gx)
    gy = cv2.filter2D(img,cv2.CV_64F,mask_gy)
    out = np.sqrt(gx**2 , gy**2)
    out = np.clip(out,0,255).astype('uint8')
    return out

img = cv2.imread('./pic3.png',0)
print(f"min : {np.min(img)} , max : {np.max(img)}")
hist = cv2.calcHist([img],[0],None,[256],[0,256])
plt.plot(hist)
plt.show()
new_img = img - np.min(img)
new_img = ((new_img.astype('float16')/np.max(new_img))*255).astype('uint8')
print(f"min : {np.min(new_img)} , max : {np.max(new_img)}")
new_img = prewitt(new_img)
concat_img = cv2.hconcat([img,new_img])
cv2.imwrite('assignment1_3 no gaussian.jpg',concat_img)