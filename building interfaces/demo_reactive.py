#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :demo_reactive.py
@说明    :
@时间    :2023/07/25 14:12:36
@作者    :ChenCY
@版本    :1.0
'''


import gradio as gr

def calculator(num1, operation, num2):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        return num1 / num2
    
demo = gr.Interface(
    calculator,
    [
        "number",
        gr.Radio(["add", "subtract", "multiply", "divide"]),
        "number"
    ],
    "number",
    live=True,
)

demo.launch()