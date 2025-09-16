# 代码生成时间: 2025-09-16 09:38:21
import gradio as gr
import requests

"""
HTTP请求处理器
使用Gradio库创建一个简单的HTTP请求处理界面
"""

# 定义一个函数来发送HTTP请求
def send_http_request(url, method):
    """
    发送HTTP请求并返回响应内容
    参数:
    - url (str): 请求的URL
    - method (str): 请求方法（GET, POST等）
    返回:
    - response (str): 响应内容
    """
    try:
        if method.upper() == 'GET':
            response = requests.get(url)
        elif method.upper() == 'POST':
            response = requests.post(url)
        else:
            return "Unsupported method"
        return response.text
    except requests.exceptions.RequestException as e:
        return f"Request error: {e}"

# 创建Gradio界面
iface = gr.Interface(
    fn=send_http_request,
    inputs=[gr.Textbox(label="URL"), gr.Radio(["GET", "POST"], label="Method")],
    outputs="text",
    title="HTTP Request Handler",
    description="Send HTTP requests using Gradio"
)

# 启动Gradio应用
iface.launch(inline=False)