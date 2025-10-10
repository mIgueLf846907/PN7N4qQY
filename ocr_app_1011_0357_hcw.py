# 代码生成时间: 2025-10-11 03:57:19
import gradio as gr
from PIL import Image
import pytesseract

# 配置pytesseract使用的tesseract-ocr引擎路径
pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"  # 或者使用你的tesseract路径

# 函数：执行OCR识别
def ocr(image_path):
    try:
        # 打开图片
        image = Image.open(image_path)
        # 使用pytesseract识别图片中的文字
        text = pytesseract.image_to_string(image, lang='chi_sim')  # 使用中文简体语言包
        # 返回识别的文字
        return text.strip()
    except Exception as e:
        # 错误处理，返回错误信息
        return f"Error: {str(e)}"

# 创建Gradio界面
iface = gr.Interface(
    # 输入功能，接受图片文件
    fn=ocr,
    # 输入参数类型
    inputs=gr.inputs.Image(label="Upload an image"),
    # 输出参数类型
    outputs="text",
    # 界面标题
    title="OCR Text Recognition",
    # 界面描述
    description="Upload an image and extract text from it using OCR."
)

# 运行Gradio界面
iface.launch()