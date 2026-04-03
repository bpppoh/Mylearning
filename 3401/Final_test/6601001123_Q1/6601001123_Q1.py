from image_tool import *

img = [ imread('./Image1.jpg',1) ]
img.extend([powerGamma(img[0],5.5) , equalization(img[0])])
histList = [calculate_hist(pic) for pic in img]
show_hist_list(histList)
imwrite('output_pic_powerGamma.jpg',img[1])
imwrite('output_pic_equalization.jpg',img[2])
imwrite('output_pic_compare.jpg',image_show(cv2.hconcat(img)))