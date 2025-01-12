#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 21:21:42 2025

@author: jinjinzhang
"""

import cv2
def resize_image(input_path,output_path,size=(100,100)):
    image=cv2.imread(input_path)
    resized=cv2.resize(image,size)
    cv2.imwrite(output_path,resized)