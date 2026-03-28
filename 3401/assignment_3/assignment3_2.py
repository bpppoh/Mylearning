from image_process import split_image_color , imread , image_show , rgb2hsv , merge_image , calculate_hist , intermean_method
import numpy as np
import cv2

img = imread('./documents.png',1)
split_img = split_image_color(img)
out = []

opt = [1,2,2,3]
noise = [1,0,1,0]

for i in range(len(split_img)) :
    pic = split_img[i]
    if noise[i] :
        pic = cv2.medianBlur(pic,3)
    h,s,v = rgb2hsv(pic)
    print(np.amax(v),np.amin(v))

    if opt[i] == 1 :
        mask = (np.amax(h) + np.amin(h))//2 > h
    elif opt[i] == 2 :
        mask = (float(np.amax(s)) + float(np.amin(s)))/2.0 > s
    elif opt[i] == 3 :
        v_uint8 = (v * 255.0).astype(np.uint8)
        thr = intermean_method(v_uint8, 3)
        mask = v > 0.1 
    pic = np.zeros_like(h,dtype='uint8')
    pic[mask] = 255

    out.append(pic)
    
img_out = merge_image(out)
image_show(img)
image_show(img_out)