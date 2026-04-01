from image_process import split_image_color , imread , image_show , rgb2hsv , merge_image , intermean_method
import numpy as np
import cv2

img = imread('./documents.png',1)
split_img = split_image_color(img)
out = []

opt = [0,1,1,2]
noise = [1,0,1,0]
inv = [0,0,0,1]

for i in range(len(split_img)) :
    space = split_img[i]
    space = cv2.medianBlur(space,3) if noise[i] else space
    space = rgb2hsv(space)[:,:,opt[i]].astype(np.float32)

    space = 1 - space if inv[i] else space
    print(np.amax(space))
    uint8_data = (space / np.amax(space)) if opt[i] == 0 else space
    uint8_data = (uint8_data * 255.).astype(np.uint8)
    pic = np.zeros_like(space,dtype=np.uint8)
    pic[uint8_data < intermean_method(uint8_data,2)] = 255
    out.append(pic)
    
img_out = merge_image(out)
image_show(img)
image_show(img_out)