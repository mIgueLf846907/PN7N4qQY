# 代码生成时间: 2025-10-04 01:38:29
import gradio as gr
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib

# 函数：加载设备数据集
def load_data(file_path):
    """
    加载设备数据集
    :param file_path: 文件路径
    :return: 特征数据，标签数据
    """
    try:
        data = pd.read_csv(file_path)
        X = data.drop('target', axis=1)
        y = data['target']
        return X, y
    except Exception as e:
        raise ValueError(f"加载数据失败：{e}")

# 函数：训练预测模型
def train_model(X, y):
    """
    训练预测模型
    :param X: 特征数据
    :param y: 标签数据
    :return: 训练好的模型
    """
    try:
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        print(f"均方误差：{mse:.4f}")
        return model
    except Exception as e:
        raise ValueError(f"模型训练失败：{e}")

# 函数：保存模型
def save_model(model, model_path):
    """
    保存模型
    :param model: 训练好的模型
    :param model_path: 模型保存路径
    """
    try:
        joblib.dump(model, model_path)
        print(f"模型已保存至：{model_path}")
    except Exception as e:
        raise ValueError(f"模型保存失败：{e}")

# 函数：加载模型
def load_model(model_path):
    """
    加载模型
    :param model_path: 模型保存路径
    :return: 加载的模型
    """
    try:
        model = joblib.load(model_path)
        print(f"模型已加载：{model_path}")
        return model
    except Exception as e:
        raise ValueError(f"模型加载失败：{e}")

# 函数：使用模型进行预测
def predict(model, X):
    """
    使用模型进行预测
    :param model: 模型
    :param X: 特征数据
    :return: 预测结果
    """
    try:
        return model.predict(X)
    except Exception as e:
        raise ValueError(f"模型预测失败：{e}")

# Gradio界面
def gradio_interface():
    """
    Gradio界面
    """
    with gr.Blocks() as demo:
        # 数据文件上传
        file_input = gr.File(label="上传设备数据文件")
        # 模型文件上传
        model_file_input = gr.File(label="上传模型文件")
        # 特征数据输入
        features_input = gr.Dropdown(label="选择特征")
        for col in X.columns:
            features_input.choices.append(col)
        # 预测按钮
        predict_button = gr.Button("预测")
        # 预测结果输出
        predict_output = gr.Textbox(label="预测结果")
        # 布局
        file_input.layout(height=100, width=200)
        model_file_input.layout(height=100, width=200)
        features_input.layout(height=100, width=200)
        predict_button.layout(height=100, width=200)
        predict_output.layout(height=100, width=200)

        # 回调函数：加载数据
        def load_data_callback(file):
            X, y = load_data(file.name)
            return X, y

        # 回调函数：加载模型
        def load_model_callback(file):
            model = load_model(file.name)
            return model

        # 回调函数：模型预测
        def predict_callback(model, X):
            return predict(model, X)

        # 绑定回调函数
        file_input.change(load_data_callback, inputs=file_input, outputs=(features_input,))
        model_file_input.change(load_model_callback, inputs=model_file_input, outputs=(predict_button,))
        predict_button.click(predict_callback, inputs=(features_input, predict_button), outputs=(predict_output,))

    demo.launch()

if __name__ == '__main__':
    gradio_interface()