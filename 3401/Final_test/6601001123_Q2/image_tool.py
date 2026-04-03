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

def rgb2hsv(img) :
    b,g,r = cv2.split(img/255.)
    c_max = np.maximum(np.maximum(r,g),b)
    c_min = np.minimum(np.minimum(r,g),b)
    delta = c_max - c_min
    h = np.zeros_like(r,dtype='float32')
    
    mask_delta = delta != 0
    mask_r = mask_delta & (c_max == r)
    mask_g = mask_delta & (c_max == g)
    mask_b = mask_delta & (c_max == b)
    
    h[mask_r] = 60 * (((g[mask_r] - b[mask_r]) / delta[mask_r]) % 6.0)
    h[mask_g] = 60 * (((b[mask_g] - r[mask_g]) / delta[mask_g]) + 2)
    h[mask_b] = 60 * (((r[mask_b] - g[mask_b]) / delta[mask_b]) + 4)
    
    s = np.zeros_like(h,dtype='float32')
    mask_v = c_max!=0
    s[mask_v] = delta[mask_v]/c_max[mask_v]
    v = c_max
    return np.stack([h,s,v],axis=2)

def saturation_adjust(s,factor,mask) :
    s[mask] = s[mask] * factor
    s = np.clip(s,0,1.0)
    return s

def value_adjust(v,factor,mask) :
    v[mask] = v[mask] * factor
    v = np.clip(v,0,1.0)
    return v

def focus_mask_hsv(hsv_img,mask) :
    h,s,v = cv2.split(hsv_img)
    v[~mask] = 0.0
    return np.stack([h,s,v],axis=2)

def hsv2bgr(hsv_img) :
    return (cv2.cvtColor(hsv_img.astype('float32'),cv2.COLOR_HSV2BGR)*255).astype('uint8')