# 代码生成时间: 2025-09-16 22:27:46
import gradio as gr
def generate_report(test_results, test_version):
    try:
        # 创建一个字典来模拟测试结果
        results_dict = {
            "version": test_version,
            "errors": [],
            "passed": [],
            "failed": [],
        }
        # 根据测试结果更新字典
        for result in test_results:
            if result['status'] == 'passed': results_dict['passed'].append(result)
            elif result['status'] == 'failed': results_dict['failed'].append(result)
            else: results_dict['errors'].append(result)
        # 将字典转换为JSON字符串
        report_json = jsonify(results_dict)
        return report_json
    except Exception as e:
        return f"An error occurred: {str(e)}"
def jsonify(data):
    import json
    try:
        return json.dumps(data, indent=4)
    except Exception as e:
        return f"An error occurred while converting to JSON: {str(e)}
def main():
    # 定义输入和输出组件
    test_results_input = gr.Dropdown(label="Enter test results", choices=[], placeholder="Select test results")
    test_version_input = gr.Textbox(label="Enter test version", placeholder="Enter test version")
    report_output = gr.Textbox(label="Test Report")
    # 使用Gradio创建接口
    iface = gr.Interface(
        fn=generate_report,
        inputs=[test_results_input, test_version_input],
        outputs=report_output,
        examples=[[([{"id": 1, "status": "passed"}], "1.0.0"), ([{"id": 2, "status": "failed"}], "1.0.1")]],
        live=True,
    )
    iface.launch()
def __name__ == "__main__":
    main()"}