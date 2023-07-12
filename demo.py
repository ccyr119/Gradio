#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :demo.py
@说明    :
@时间    :2023/07/06 18:10:08
@作者    :ChenCY
@版本    :1.0
'''

import gradio as gr

def sketch_recognition(name):
    return "Hello " + name + "!"

demo = gr.Interface(fn=sketch_recognition, inputs="text", outputs="text")
demo.launch()