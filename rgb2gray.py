#!/usr/bin/python3

import cv2 
import numpy as np 

for n in [1, 2, 3, 4]:
    file_name='image'+str(n)+'.jpg'
    im = cv2.imread(file_name)
    im1=im[0:1080, 320:1400]
    im1=cv2.resize(im1, (320, 320))
    im_colormap=cv2.applyColorMap(im1, cv2.COLORMAP_JET)
    im_gray = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)

    colormap_name='colormap_'+file_name
    gray_name ='gray_'+file_name

    print(im_colormap.shape)

    cv2.imwrite(colormap_name, im_colormap)
    cv2.imwrite(gray_name, im_gray)
