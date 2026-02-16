import numpy as np
import cv2
import matplotlib.pyplot as plt

def powerGamma(image,gamma) :
    image = image.astype('float')/np.max(image)
    image = (image**gamma*255).astype('uint8')
    return image

def calculate_hist(img) :
    hist = cv2.calcHist([img],[0],None,[256],[0,256])
    plt.plot(hist)
    plt.show()
    return hist

def image_show(img) :
    cv2.imshow("xxxx",img)
    cv2.waitKey()
    cv2.destroyAllWindows()
    
def sobel(img) :
    mask_gx = np.array([[-1,0,1],[-2,0,2],[-1,0,1]] , dtype='float16')
    mask_gy = np.array([[-1,-2,-1],[0,0,0],[1,2,1]] , dtype='float16')
    gx = cv2.filter2D(img,cv2.CV_64F,mask_gx)
    gy = cv2.filter2D(img,cv2.CV_64F,mask_gy)
    out = np.sqrt(gx**2 , gy**2)
    out = np.clip(out,0,255).astype('uint8')
    return out