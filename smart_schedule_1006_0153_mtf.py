# 代码生成时间: 2025-10-06 01:53:21
import gradio as gr
def generate_schedule(timetable, courses, teachers, rooms):
    # 简单的贪心算法实现智能排课系统
    # 假设timetable是一个二维数组，存储每个时间段的课程
    # courses是一个列表，包含课程属性
    # teachers是一个列表，包含教师属性
    # rooms是一个列表，包含教室属性
    schedule = []
    for time_slot in timetable:
        for course in courses:
            if course not in [s['course'] for s in schedule if s['time'] == time_slot]:
                schedule.append({'time': time_slot, 'course': course})
    return schedule
def main():
    # 创建Gradio界面
    with gr.Blocks() as demo:
        # 输入参数
        courses_input = gr.Dropdown(label="Courses", choices=["Math", "Science", "English"], multiple=True)
        teachers_input = gr.Dropdown(label="Teachers", choices=["Alice", "Bob", "Charlie"], multiple=True)
        rooms_input = gr.Dropdown(label="Rooms", choices=["Room 1", "Room 2", "Room 3"], multiple=True)
        time_input = gr.Number(label="Number of Time Slots", value=5)
        
        # 输出参数
        schedule_output = gr.Dataframe(label="Schedule")
        
        # 根据输入参数生成排课表
        def generate_schedule_callback(courses, teachers, rooms, time_slots):
            timetable = [f"Time Slot {i+1}" for i in range(time_slots)]
            return generate_schedule(timetable, courses, teachers, rooms)
        
        # 连接输入输出
        schedule_output.change(generate_schedule_callback, inputs=[courses_input, teachers_input, rooms_input, time_input])
    
    # 启动应用
    demo.launch()

if __name__ == "__main__":
    main()
