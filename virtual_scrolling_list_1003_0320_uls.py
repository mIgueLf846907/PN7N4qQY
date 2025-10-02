# 代码生成时间: 2025-10-03 03:20:20
import gradio as gr
def get_data(start, end):
    """
    Function to generate mock data for virtual scrolling.

    Args:
        start (int): starting index of the data range
        end (int): ending index of the data range

    Returns:
        list: list of dictionaries containing mock data
    """
    return [{'id': i, 'text': f'Item {i}'} for i in range(start, end)]

def main():
    """
    Main function to create a Gradio interface for the virtual scrolling list.

    Creates an interface with two input sliders to specify the range for data retrieval,
    and a button to fetch and display the data within that range.
    """
    # Create Gradio interface
    demo = gr.Interface(
        fn=get_data,
        inputs=[gr.Slider(minimum=0, maximum=10000, step=1, label='Start Index'),
                gr.Slider(minimum=0, maximum=10000, step=1, label='End Index')],
        outputs='json',
        examples=[[0, 100], [1000, 1100], [5000, 5100]],
        title='Virtual Scrolling List',
        description='Enter the start and end indices to fetch data.'
    )

    # Launch the interface
    demo.launch()

if __name__ == '__main__':
    main()