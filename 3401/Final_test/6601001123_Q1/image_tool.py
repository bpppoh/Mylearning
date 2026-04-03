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
    
def equalization(img,hist=None):
    if hist is None :
        cdf = cv2.calcHist([img],[0],None,[256],[0,256]).flatten().cumsum()
    else :
        cdf = hist.flatten().cumsum()
    cdf_m = np.ma.masked_equal(cdf, 0) 
    cdf_m = ((cdf_m - cdf_m.min())  / (cdf_m.max() - cdf_m.min()))*255
    cdf = np.ma.filled(cdf_m, 0).astype('uint8')
    return cdf[img]

def image_show(img) :
    cv2.imshow("xxxx",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.waitKey(1)
    return img
    
def powerGamma(image,gamma) :
    image = image.astype('float')/np.max(image)
    image = (image**gamma*255).astype('uint8')
    return image

def imwrite(filename,img) :
    return cv2.imwrite(filename,img)