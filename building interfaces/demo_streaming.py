#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :demo_streaming.py
@说明    :
@时间    :2023/07/25 14:12:22
@作者    :ChenCY
@版本    :1.0
'''

import gradio as gr
import numpy as np

def flip(im):
    return np.flipud(im)

demo = gr.Interface(
    flip,
    gr.Image(source="webcam", streaming=True),
    "image",
    live=True
)

demo.launch()