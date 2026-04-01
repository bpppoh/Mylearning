import numpy as np
import cv2
import math

def image_show(img) :
    cv2.imshow("xxxx",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.waitKey(1)
    
def init_Transformation():
    return np.identity(3, dtype = float)

def matrix_Translate(T, tx, ty):
    Ts =  np.identity(3, dtype = float)
    Ts[2,0] = tx
    Ts[2,1] = ty
    return np.matmul(Ts, T)

def matrix_Scale(T, sx, sy):
    S =  np.identity(3, dtype = float)
    S[0,0] = sx
    S[1,1] = sy
    return  np.matmul(S, T)    

def matrix_Rotatef(T, theta):
    R =  np.identity(3, dtype = float)
    ang = (theta*np.pi)/180
    R[0,0] = math.cos(ang)
    R[0,1] = math.sin(ang)
    R[1,0] = -math.sin(ang)
    R[1,1] = math.cos(ang)
    return np.matmul(R, T)

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

def centroid(img) :
    return (int(img.shape[1]/2),int(img.shape[0]/2))
    
img = cv2.imread('./image/cameraman.tif',0)
cen = centroid(img)
T = init_Transformation()
T = matrix_Translate(T, cen[1], cen[0])
T = matrix_Scale(T, 0.5, 0.5)
T = matrix_Rotatef(T,45)
T = matrix_Scale(T, -1, 1)
T = matrix_Translate(T, -cen[1], -cen[0])
newimg = img_transform(img,T)

image_show(newimg)