import numpy as np
import cv2
import matplotlib.pyplot as plt
import math

def imread(img,color) :
    return cv2.imread(img,color)

def powerGamma(image,gamma) :
    image = image.astype('float')/np.max(image)
    image = (image**gamma*255).astype('uint8')
    return image

def calculate_hist(img) :
    return cv2.calcHist([img],[0],None,[256],[0,256]) 

def show_hist(hist) :
    plt.figure()
    plt.plot(hist)
    plt.show()

def image_show(img) :
    cv2.imshow("xxxx",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.waitKey(1)
    
def sobel(img) :
    gx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)  
    gy = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)  
    out = np.sqrt(gx**2 + gy**2)
    return out.astype(np.uint8)

def equalization(img,hist=None):
    if hist is None :
        cdf = cv2.calcHist([img],[0],None,[256],[0,256]).flatten().cumsum()
    else :
        cdf = hist.cumsum()
    cdf_m = np.ma.masked_equal(cdf, 0) 
    cdf_m = ((cdf_m - cdf_m.min())  / (cdf_m.max() - cdf_m.min()))*255
    cdf = np.ma.filled(cdf_m, 0).astype('uint8')
    return cdf[img]

def init_transform() :
    return np.identity(3,dtype='float')

def matrix_translate(T,tx,ty) :
    t = np.identity(3,dtype=float)
    t[2,0] = tx
    t[2,1] = ty
    return np.matmul(t,T)

def matrix_scaling(T,sx,sy) :
    s = np.identity(3,dtype=float)
    s[0,0] = sx
    s[1,1] = sy
    return np.matmul(s,T)

def matrix_rotate(T,degree) :
    R = np.identity(3,dtype=float)
    degree = (degree*np.pi)/180
    R[0,0] = math.cos(degree)
    R[0,1] = -math.sin(degree)
    R[1,0] = math.sin(degree)
    R[1,1] = math.cos(degree)
    return np.matmul(R,T)

def flip_horizontal_grayscale(img) :
    new_img = np.zeros_like(img,dtype='uint8')
    row , col = img.shape
    for r in range(row) :
        for c in range(col) :
            new_img[r,c] = img[r,col-1-c]
    return new_img

def img_transform(img, T):
    out = np.zeros_like(img, dtype='uint8')
    rows, cols = img.shape
    for y in range(rows):
        for x in range(cols):
            xy = np.array([x, y, 1], dtype = float)
            new_xy = np.matmul(xy, T)
            xn = int(new_xy[0])
            yn = int(new_xy[1])
            if 0 <= xn < cols and 0 <= yn < rows:
                out[yn,xn] = img[y,x]
    return out.astype(np.uint8)

def split_image(img) :
    row , col = img.shape
    out = []
    y = [0 , row//2 , row-1]
    x = [0 , col//2 , col-1]
    for i in range(len(y)-1) :
        for j in range(len(x)-1) :
            out.append(img[y[i]:y[i+1],x[j]:x[j+1]])
    return out

def split_image_color(img) :
    row , col , space = img.shape
    out = []
    y = [0 , row//2 , row-1]
    x = [0 , col//2 , col-1]
    for i in range(len(y)-1) :
        for j in range(len(x)-1) :
            out.append(img[y[i]:y[i+1],x[j]:x[j+1],:])
    return out

def float2int(x):
    if x - math.floor(x) >= 0.5:
        result = math.ceil(x)
    else:
        result = math.floor(x)
    return result

def intermean_method(img,round,reversed=False) :
    T = [] 
    hist = calculate_hist(img).flatten()
    st = 0
    en = 256
    T.append(int((st+en)*0.5))
    for i in range(round) :
        t = intermean(hist,T[-1],st,en)
        T.append(t)
        if reversed :
            en = t
        else :
            st = t
    return T[-1]
        
def intermean(hist,t,st,en) :
    prob = np.zeros_like(hist,dtype='float16')
    prob[st:en] = hist[st:en]/np.sum(hist[st:en])
    w0 = np.sum(prob[st:t+1]) + 0.00001
    w1 = (1-w0) + 0.00001
    u0 = np.sum(np.arange(st,t+1)*prob[st:t+1])/w0
    u1 = np.sum(np.arange(t+1,en)*prob[t+1:en])/w1
    if u0 == 0.0 :
        thr = u1
    elif u1 == 0.0 :
        thr = u0
    else :
        thr = (u1+u0)/2
    return float2int(thr)

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

def saturation_adjust(hsv_img,factor,st,en) :
    h,s,v = cv2.split(hsv_img)
    blue_mask = (h>=st) & (h<=en)
    s[blue_mask] = s[blue_mask] * factor
    s = np.clip(s,0,1.0)
    return np.stack([h,s,v],axis=2)

def merge_image(img_list) :
    return cv2.vconcat([
        cv2.hconcat([img_list[0],img_list[1]]),
        cv2.hconcat([img_list[2],img_list[3]])
    ])
    
def hsv2gray(img) :
    return cv2.cvtColor(cv2.cvtColor(img,cv2.COLOR_HSV2RGB),cv2.COLOR_RGB2GRAY)

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

def cmyk2bgr(img) :
    c,m,y,k = cv2.split(img)
    r = 255 * (1 - c) * (1 - k)
    g = 255 * (1 - m) * (1 - k)
    b = 255 * (1 - y) * (1 - k)
    
    return np.stack([b,g,r],axis=2).astype(np.uint8)

def otsu(img):
    hist = cv2.calcHist([img],[0],None,[256],[0,256])
    tot = np.sum(hist)
    prob = hist/tot
    coef_max = -1
    thr = -1
    for t in range(1,256):
        w0 = np.sum(prob[:t]) + 0.00000001
        w1 = np.sum(prob[t:]) + 0.00000001
        i0 = np.array([i for i in range(t)])
        i1 = np.array([i for i in range(t,256)])
        u0 = np.sum(i0*prob[:t])/w0
        u1 = np.sum(i1*prob[t:])/w1

        coef = (w0*w1)*np.power(u0-u1,2)
        if  coef > coef_max:
            coef_max = coef
            thr = t
    return thr