#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :demo_global_state.py
@说明    :
@时间    :2023/07/24 14:11:23
@作者    :ChenCY
@版本    :1.0
'''

import gradio as gr

scores = []

def trace_score(score):
    scores.append(score)
    top_scores =sorted(scores, reverse=True)[:3]
    return top_scores

demo = gr.Interface(
    trace_score,
    gr.Number(label="Score"),
    gr.JSON(label="Top Scores")
)

demo.launch()