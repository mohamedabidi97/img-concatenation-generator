#import packages
import cv2
import sys
# Arguments
path1 = sys.argv[1]
path2 = sys.argv[2]
path3 = sys.argv[3]
path4 = sys.argv[4]
pixel_arg = sys.argv[5]
# final size : 2700x4050
f_size = (2700,4050)
p1_size = (2700,2025)
p2_size = (1350,2025)
#border color
white = [255,255,255]
def get_concat_4_v(im_1,im_2,im_3,im_4,pixel_param):
    pxl = int(pixel_param) * 150
    im_list = [im_1,im_2,im_3,im_4]
    im_list_resize = [cv2.resize(im, p2_size) for im in im_list]
    img_with_border = [cv2.copyMakeBorder(im,pxl,pxl,pxl,pxl, \
                                         cv2.BORDER_CONSTANT,value=white) for im in im_list_resize]
    output_1 = cv2.hconcat(img_with_border[0:2])
    output_2 = cv2.hconcat(img_with_border[2:4])
    img_ = cv2.vconcat([output_1, output_2])
    output = cv2.resize(img_, f_size)
    try : 
        cv2.imwrite('final_4.png',output)
        print('Succes!')
    except : 
        print('Error')
def get_concat_2_v(img_1,img_2,pixel_param):
    pxl = int(pixel_param) * 150
    im_list = [img_1,img_2]
    im_list_resize = [cv2.resize(im, p1_size) for im in im_list]
    img_with_border = [cv2.copyMakeBorder(im,pxl,pxl,pxl,pxl, \
                                         cv2.BORDER_CONSTANT,value=white) for im in im_list_resize]
    img_ = cv2.vconcat(img_with_border)
    output = cv2.resize(img_, f_size)
    try : 
        cv2.imwrite('final_2.png',output)
        print('Succes ! ')
    except :
        print('Error in generation')
if (path3 in ['Null','NULL','null'] and path4 in ['Null','NULL','null']) : 
    img1 = cv2.imread(path1) 
    img2 = cv2.imread(path2)
    get_concat_2_v(img1,img2,pixel_arg)
else : 
    img1 = cv2.imread(path1) 
    img2 = cv2.imread(path2)
    img3 = cv2.imread(path3)
    img4 = cv2.imread(path4)
    get_concat_4_v(img1,img2,img3,img4,pixel_arg)


     






