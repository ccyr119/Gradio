#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :demo_ProgressBar.py
@说明    :
@时间    :2023/07/18 15:08:45
@作者    :ChenCY
@版本    :1.0
'''

import gradio as gr
import time

def slowlly_reverse(word, progress=gr.Progress()):
    progress(0, desc="Starting")
    time.sleep(1)
    progress(0.05)
    new_string = ""
    for letter in progress.tqdm(word, desc="Reversing"):
        time.sleep(0.25)
        new_string = letter + new_string
    return new_string

demo = gr.Interface(slowlly_reverse, gr.Text(), gr.Text())

if __name__ == "__main__":
    demo.queue(concurrency_count=10).launch()