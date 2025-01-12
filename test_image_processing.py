#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 22:01:39 2025

@author: jinjinzhang
"""

import os 
from src.image_processing import resize_image

def test_resize_image():
    input_path='/Users/jinjinzhang/Desktop/test_json/test.jpg'
    output_path='/Users/jinjinzhang/Desktop/test_json/resized_test.jpg'
    resize_image(input_path,out_put_path,size=(50,50))
    assert os.path.exists(output_path),'Resized image not created'