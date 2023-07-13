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

placeholder = "Name Here..."

def greet(name : str, is_morning : bool, temperature : float):
    salutation = "Good morning" if is_morning else "Good evening"
    greeting = f"{salutation} {name}. It is {temperature} degress today"
    celsius = (temperature - 32) * 5 / 9
    return greeting, round(celsius, 2)

demo = gr.Interface(fn=greet, 
    inputs=["text", "checkbox", gr.Slider(0, 100)],
    outputs=["text", "number"]
)
demo.launch()