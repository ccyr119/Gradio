#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :demo_image.py
@说明    :
@时间    :2023/07/12 18:41:20
@作者    :ChenCY
@版本    :1.0
'''

import numpy as np
import gradio as gr

def sepia(input_img):
    sepia_filter = np.array([
        [0.393, 0.769, 0.189], 
        [0.349, 0.686, 0.168], 
        [0.272, 0.534, 0.131]
    ])
    sepia_img = input_img.dot(sepia_filter.T)
    sepia_img /= sepia_img.max()
    return sepia_img

demo = gr.Interface(sepia, gr.Image(shape=(200, 200)), "image")
demo.launch()