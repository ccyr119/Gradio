#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :demo_interative_output.py
@说明    :
@时间    :2023/07/18 15:00:29
@作者    :ChenCY
@版本    :1.0
'''

import gradio as gr
import numpy as np
import time

#define core fn, which return a generator {steps} times before returning the image
def fake_diffusion(steps):
    for _ in range(steps):
        time.sleep(1)
        image = np.random.random((600, 600, 3))
        yield image
    image = "https://gradio-builds.s3.amazonaws.com/diffusion_image/cute_dog.jpg"
    yield image

demo = gr.Interface(fake_diffusion, inputs=gr.Slider(1, 10, 3), outputs="image")

#define queue - required for generators
demo.queue()

demo.launch()