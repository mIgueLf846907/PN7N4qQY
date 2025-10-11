# 代码生成时间: 2025-10-12 03:37:20
import gradio as gr

# 定义职业规划系统类
class CareerPlanningSystem:
    def __init__(self):
        # 初始化职业数据库
        self.careers = self.load_careers()

    def load_careers(self):
        # 从文件或数据库加载职业数据
        # 这里假设我们有一个职业列表文件'careers.json'
        try:
            with open('careers.json', 'r') as f:
                careers = json.load(f)
                return careers
        except FileNotFoundError:
            print("职业数据文件未找到")
            return {}
        except json.JSONDecodeError:
            print("职业数据文件格式错误")
            return {}

    def suggest_careers(self, user_interests):
        # 根据用户兴趣推荐职业
        suggestions = []
        for career in self.careers:
            if set(user_interests).issubset(set(career['interests'])):
                suggestions.append(career['name'])
        return suggestions

    def get_career_info(self, career_name):
        # 获取特定职业的详细信息
        for career in self.careers:
            if career['name'] == career_name:
                return career
        return None

# 创建Gradio界面
iface = gr.Interface(
    fn=CareerPlanningSystem().suggest_careers,
    inputs=gr.Textbox(label='Enter your interests separated by commas'),
    outputs=gr.Textbox(label='Career suggestions')
)

# 启动界面
iface.launch()