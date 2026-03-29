from image_process import split_image_color , imread , image_show , rgb2hsv , merge_image , calculate_hist , intermean_method , show_hist
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
    h,s,v = cv2.split(rgb2hsv(pic))
    print(np.amax(v),np.amin(v))

    if opt[i] == 1 :
        h_uint8 = ((h/np.amax(h)) * 255.).astype(np.uint8)
        thr = intermean_method(h_uint8,2)
        mask = h_uint8 < thr
    elif opt[i] == 2 :
        s_uint8 = (s*255.).astype(np.uint8)
        thr = intermean_method(s_uint8,2)
        mask = s_uint8 < thr
    elif opt[i] == 3 :
        v_uint8 = (v * 255.0).astype(np.uint8)
        thr = intermean_method(v_uint8, 2,reversed=True)
        mask = thr < v_uint8
    pic = np.zeros_like(h,dtype='uint8')
    pic[mask] = 255

    out.append(pic)
    
img_out = merge_image(out)
image_show(img)
image_show(img_out)