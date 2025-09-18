# 代码生成时间: 2025-09-18 09:27:46
import gradio as gr
def validate_access(user_id, password):
    # 模拟的用户数据库
    user_db = {'user1': 'pass1', 'user2': 'pass2'}
    # 检查用户ID和密码
    if user_id in user_db and user_db[user_id] == password:
        return 'Access Granted'
    else:
        return 'Access Denied'

# 创建Gradio接口
iface = gr.Interface(
    validate_access,
    inputs=["text", "text"],  # 用户名和密码输入
    outputs="text",  # 输出结果
    title="Access Control System",
    description="Enter your credentials to check access."
)

# 运行Gradio应用
iface.launch()