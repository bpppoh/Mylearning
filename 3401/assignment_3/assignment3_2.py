from image_process import split_image_color , imread , image_show , rgb2hsv , intermean_method , merge_image
import numpy as np
import cv2

img = imread('./documents.png',1)
split_img = split_image_color(img)
out = []

opt = [1,2,2,3]
noise = [1,0,1,0]

for i in range(len(split_img)) :
    pic = split_img[i]
    h,s,v = rgb2hsv(pic)
    print(np.amax(v),np.amin(v))

    if opt[i] == 1 :
        h_mid = (np.amax(h) + np.amin(h)) // 2
        mask = h < h_mid
    elif opt[i] == 2 :
        mask = s != np.amax(s)
    elif opt[i] == 3 :
        mask = v != np.amin(v)
    pic = np.zeros_like(h,dtype='uint8')
    pic[mask] = 255

    if noise[i] :
        pic = cv2.medianBlur(pic,3)
    
    out.append(pic)
    
img_out = merge_image(out)
image_show(img)
image_show(img_out)