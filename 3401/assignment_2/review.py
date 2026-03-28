from image_process import image_show , imread_grayscale , init_transform , flip_horizontal_grayscale ,matrix_rotate , matrix_translate , matrix_scaling , img_transform

img = imread_grayscale('./cameraman.tif')
image_show(img)
cen = [img.shape[0]/2 , img.shape[1]/2]

T = init_transform()
T = matrix_translate(T, cen[1], cen[0])
# T = matrix_scaling(T, 0.5, 0.5)
# T = matrix_rotate(T,45)
T = matrix_scaling(T, -1, 1)
T = matrix_translate(T, -cen[1], -cen[0])
newimg = img_transform(img,T)

image_show(newimg)