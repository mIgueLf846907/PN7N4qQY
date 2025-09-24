# 代码生成时间: 2025-09-24 11:23:37
import pandas as pd
import gr

"""
统计数据分析器
使用GRADIO框架创建一个简单的应用，用于加载数据文件，
进行基本的统计分析，并展示结果。
"""

class DataAnalysisApp:
    """
    统计数据分析器类
    """
    def __init__(self):
        self.title = "统计数据分析器"
        self.description = "加载数据文件，进行基本统计分析。"
        self.input_file = "上传数据文件"
        self.output = "统计结果"
        self.analysis_functions = [
            ("mean", "计算平均值"),
            ("median", "计算中位数"),
            ("max", "计算最大值"),
            ("min", "计算最小值"),
            ("std", "计算标准差"),
            ("var", "计算方差"),
        ]

    def load_data(self, file):
        """
        加载数据文件到Pandas DataFrame
        """
        try:
            return pd.read_csv(file)
        except pd.errors.EmptyDataError:
            gr.Error("文件为空，请上传非空文件。")
        except pd.errors.ParserError:
            gr.Error("文件解析错误，请上传正确格式的文件。")
        except Exception as e:
            gr.Error(f"加载文件时出现错误：{str(e)}")

    def perform_analysis(self, df, analysis_type):
        """
        根据选择的分析类型，对数据进行分析
        """
        try:
            if analysis_type == "mean":
                return df.mean()
            elif analysis_type == "median":
                return df.median()
            elif analysis_type == "max":
                return df.max()
            elif analysis_type == "min":
                return df.min()
            elif analysis_type == "std":
                return df.std()
            elif analysis_type == "var":
                return df.var()
            else:
                gr.Error("未知的分析类型")
        except Exception as e:
            gr.Error(f"分析数据时出现错误：{str(e)}")

    def run(self, file, analysis_type):
        """
        运行数据分析器
        """
        df = self.load_data(file)
        result = self.perform_analysis(df, analysis_type)
        return result

    def create_interface(self):
        """
        创建GRADIO界面
        """
        with gr.Blocks() as demo:
            gr.Markdown(
                f"## {self.title}
                {self.description}"
            )
            file_input = gr.File(label=self.input_file)
            analysis_type_input = gr.Radio(
                choices=self.analysis_functions, label="选择分析类型"
            )
            output = gr.Dataframe(label=self.output)
            file_input.change(self.run, inputs=[file_input, analysis_type_input], outputs=output)
            analysis_type_input.change(self.run, inputs=[file_input, analysis_type_input], outputs=output)

        demo.launch()

# 创建统计数据分析器实例并启动GRADIO界面
app = DataAnalysisApp()
app.create_interface()