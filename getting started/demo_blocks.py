#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :demo_blocks.py
@说明    :
@时间    :2023/07/13 13:59:45
@作者    :ChenCY
@版本    :1.0
'''

import gradio as gr

def greet(name):
    return 'Hello ' + name + '!'

with gr.Blocks() as demo:
    name = gr.Textbox(label="Name")
    output = gr.Textbox(label="Output Box")
    greet_btn = gr.Button("Greet")
    greet_btn.click(fn=greet, inputs=name, outputs=output, api_name="greet")

demo.launch()