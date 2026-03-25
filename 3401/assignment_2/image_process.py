import numpy as np
import cv2
import matplotlib.pyplot as plt
import math

def imread_grayscale(filePath) :
    return cv2.imread(filePath,0)

def powerGamma(image,gamma) :
    image = image.astype('float')/np.max(image)
    image = (image**gamma*255).astype('uint8')
    return image

def calculate_hist(img,foldername=None,name=None) :
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

def float2int(x):
    if x - math.floor(x) >= 0.5:
        result = math.ceil(x)
    else:
        result = math.floor(x)
    return result

def intermean_method(img,round) :
    T = [] 
    hist = calculate_hist(img).flatten()
    st = 0
    en = 256
    T.append(int((st+en)*0.5))
    for i in range(round) :
        t = intermean(hist,T[-1],st,en)
        T.append(t)
        st = t
    print(T)
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

def MedianCustom(img, sz):
    bd = int(sz / 2)
    inx = int(float(sz*sz)/2.0)
    (m,n) = img.shape
    #out = np.zeros((m,n), dtype = 'float16')
    out = img.copy()
    for i in range(bd,m-bd):
        for j in range(bd,n-bd):
            sub_img = img[i-bd:i+bd+1, j-bd:j+bd+1]
            asort = np.sort(np.ravel(sub_img))
            out[i,j] = asort[inx]    
    return out.astype(np.uint8)

def merge_image(img_list) :
    return cv2.vconcat([
        cv2.hconcat([img_list[0],img_list[1]]),
        cv2.hconcat([img_list[2],img_list[3]])
    ])