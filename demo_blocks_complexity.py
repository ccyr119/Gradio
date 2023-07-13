#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :demo_blocks_complexity.py
@说明    :
@时间    :2023/07/13 14:06:12
@作者    :ChenCY
@版本    :1.0
'''

import numpy as np
import gradio as gr

def flip_text(x):
    return x[::-1]

def flip_image(x):
    return np.fliplr(x)

with gr.Blocks() as demo:
    gr.Markdown("Flip text or image flies using this demo.")
    with gr.Tab("Flip Text"):
        text_input = gr.Textbox(label="Input text")
        text_Output = gr.Textbox(label="Output text")
        text_button = gr.Button("Flip")
    with gr.Tab("Flip Image"):
        with gr.Row():
            image_input = gr.Image()
            image_output = gr.Image()
        image_button = gr.Button("Flip")
    
    with gr.Accordion("Open for More!"):
        gr.Markdown("Look at me...")

    text_button.click(flip_text, inputs=text_input, outputs=text_Output)
    image_button.click(flip_image, inputs=image_input, outputs=image_output)

demo.launch()