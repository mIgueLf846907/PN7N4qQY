# 代码生成时间: 2025-10-03 23:42:42
import gradio as gr

# 模拟的物流跟踪数据
logistics_data = {
    "123456789": "包裹已签收",
    "987654321": "运输中",
    "555555555": "已发货"
}

# 函数：根据物流单号查询跟踪信息
def track_package(tracking_number):
    """根据物流单号查询跟踪信息。
    
    参数:
    tracking_number (str): 物流单号
    
    返回:
    dict: {'status': '跟踪信息', 'tracking_number': '物流单号'}
    """
    try:
        # 检查物流单号是否在模拟数据中
        if tracking_number in logistics_data:
            return {"status": logistics_data[tracking_number], "tracking_number": tracking_number}
        else:
            # 如果物流单号不在模拟数据中，返回错误信息
            return {"status": "物流单号不存在", "tracking_number": tracking_number}
    except Exception as e:
        # 捕捉并处理任何异常
        return {"status": str(e), "tracking_number": tracking_number}

# Gradio界面
iface = gr.Interface(
    fn=track_package,
    inputs=gr.Textbox(label="请输入物流单号"),
    outputs="json",
    title="物流跟踪系统",
    description="输入物流单号查询跟踪信息"
)

# 启动Gradio界面
iface.launch()