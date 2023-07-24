#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :demo_batch_functions.py
@说明    :
@时间    :2023/07/18 15:41:48
@作者    :ChenCY
@版本    :1.0
'''

import gradio as gr
import time

def trim_words(words, lens):
    trimmed_words = []
    time.sleep(5)
    for w, l in zip(words, lens):
        trimmed_words.append(w[:int(l)])
    return [trim_words]

demo = gr.Interface(trim_words, ["textbox", "number"], ["textbox"],
                    batch=True, max_batch_size=16)

demo.queue()
demo.launch()