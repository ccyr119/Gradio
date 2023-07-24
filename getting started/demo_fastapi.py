#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :demo_fastapi.py
@说明    :
@时间    :2023/07/21 18:18:08
@作者    :ChenCY
@版本    :1.0
'''


from fastapi import FastAPI
import gradio as gr
import uvicorn

CUSTOM_PATH ="/gradio"

app = FastAPI()

@app.get("/")
def read_main():
    return {"message": "This is you main app!"}

io = gr.Interface(lambda x: "Hello, " + x + "!", "textbox", "textbox")
app = gr.mount_gradio_app(app, io, path=CUSTOM_PATH)

# if __name__ == 'main':
#     uvicorn.run(app="demo_fastapi:app", host="127.0.0.1", port=8000, reload=True, debug=True)

# Run this from the terminal as you would normally start a FastAPI app: `uvicorn run:app`
# and navigate to http://localhost:8000/gradio in your browser.