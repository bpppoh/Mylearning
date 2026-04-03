import numpy as np
import cv2
import matplotlib.pyplot as plt
import math

def imread(img,color) :
    return cv2.imread(img,color)

def calculate_hist(img) :
    return cv2.calcHist([img],[0],None,[256],[0,256]) 

def show_hist(hist) :
    plt.figure()
    plt.plot(hist)
    plt.show()
    
def show_hist_list(histList) :
    num = len(histList)
    plt.figure()
    for i in range(len(histList)) :
        plt.subplot(1,num,i+1)
        plt.plot(histList[i])
    plt.show()

def image_show(img) :
    cv2.imshow("xxxx",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.waitKey(1)
    return img

def imwrite(filename,img) :
    return cv2.imwrite(filename,img)

def bgr2cmyk(img) :
    B,G,R = cv2.split(img)
    r = R/255.
    g = G/255.
    b = B/255.
    
    k = 1 - np.maximum(np.maximum(r,g),b)
    c = (1 - r - k) / (1 - k + 1e-10)
    m = (1 - g - k) / (1 - k + 1e-10)
    y = (1 - b - k) / (1 - k + 1e-10)
    return np.stack([c,m,y,k],axis=2)