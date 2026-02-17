import numpy as np
import cv2
import matplotlib.pyplot as plt

def powerGamma(image,gamma) :
    image = image.astype('float')/np.max(image)
    image = (image**gamma*255).astype('uint8')
    return image

def calculate_hist(img,foldername=None,name=None) :
    hist = cv2.calcHist([img],[0],None,[256],[0,256])
    plt.figure()
    plt.plot(hist)
    if name and foldername :
        plt.savefig(foldername+"/"+name)
    plt.show()
    return hist

def image_show(img) :
    cv2.imshow("xxxx",img)
    cv2.waitKey()
    cv2.destroyAllWindows()
    
def sobel(img) :
    gx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)  
    gy = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)  
    out = np.sqrt(gx**2 + gy**2)
    return out.astype(np.uint8)

def equalization(img):
    cdf = cv2.calcHist([img],[0],None,[256],[0,256]).flatten().cumsum()
    cdf_m = np.ma.masked_equal(cdf, 0) 
    cdf_m = ((cdf_m - cdf_m.min())  / (cdf_m.max() - cdf_m.min()))*255
    cdf = np.ma.filled(cdf_m, 0).astype('uint8')
    return cdf[img]