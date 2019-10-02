#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 08:58:45 2018

@author: kannan.kalidasan
"""

import cv2

def main():
    print(cv2.__version__)
    imgpath="sunflower.jpg"
    # read the image and store it in img variable
    img = cv2.imread(imgpath)
    img = cv2.imread(imgpath,0) # default mode 
    #img = cv2.imread(imgpath,0) # gray scale mode 
    #img = cv2.imread(imgpath,-1) # load as it is and also save the alpha transparency in the image
    cv2.namedWindow('Lena',cv2.WINDOW_AUTOSIZE)
    
    cv2.startWindowThread()
    
    outputpath="sunflower-gray.jpg"
    cv2.imwrite(outputpath,img)

if __name__ == "__main__":
    main()