from image_process import image_show , imread_grayscale , split_image , equalization , intermean_method , merge_image
import cv2
import numpy as np

img = imread_grayscale('./document1.png')
image_show(img)
split_list = split_image(img)
out = []

black2white = [1,0,0,1]
equalized = [1,1,0,0]
thr_round = [1,1,2,1]
noise = [0,0,0,1]

        
for i in range(len(split_list)) :
    pic = split_list[i]
    if black2white[i] :
        pic = 255 - pic
    if equalized[i] :
        pic = equalization(pic)
    if noise[i] :
        pic = cv2.medianBlur(pic,3)
    thr = intermean_method(pic,thr_round[i])
    mask = pic > thr
    pic = np.zeros_like(pic,dtype='uint8')
    pic[~mask] = 255
    out.append(pic)

out_img = merge_image(out)
image_show(out_img)