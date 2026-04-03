from image_tool import *
import cv2
import numpy as np

img = image_show(imread('./Image2.png',1))
hsv_img = rgb2hsv(img)
h,s,v = cv2.split(hsv_img)

masks = [(h > 180) &  (h < 260) , (h > 20) & (h < 60)]
focus_name = ['blue_focus.jpg' , 'orange_focus.jpg']
for i in range(len(masks)) : 
    focus_img = image_show(hsv2bgr(focus_mask_hsv(hsv_img,masks[i])))
    imwrite(f"{focus_name[i]}",focus_img)
    
s = saturation_adjust(s,0.2,masks[0])
s = saturation_adjust(s,40.0,masks[1])
v = value_adjust(v,1.3,masks[1])
out = hsv2bgr(np.stack([h,s,v],axis=2))
imwrite('output.jpg',image_show(out))
imwrite("output_compare.jpg",image_show(cv2.hconcat([img,out])))