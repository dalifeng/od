import time

def focus_clock(total_work_periods=4):
    work_duration = 25 * 60  # 25分钟工作时间（秒）
    short_break_duration = 5 * 60  # 5分钟短休息时间（秒）
    long_break_duration = 15 * 60  # 15分钟长休息时间（秒）
    completed_work_periods = 0

    while completed_work_periods < total_work_periods:
        print(f"工作时间开始：{time.strftime('%H:%M:%S', time.localtime())}")
        time.sleep(work_duration)
        print("工作时间结束，休息一下！")
        completed_work_periods += 1

        if completed_work_periods < total_work_periods:
            if completed_work_periods % 4 == 0:
                print(f"长休息开始：{time.strftime('%H:%M:%S', time.localtime())}")
                time.sleep(long_break_duration)
                print("长休息结束，继续工作！")
            else:
                print(f"短休息开始：{time.strftime('%H:%M:%S', time.localtime())}")
                time.sleep(short_break_duration)
                print("短休息结束，继续工作！")

    print("所有工作时间段已完成！")

if __name__ == "__main__":
    total_work_periods = 10000  # 设置总的工作时间段数
    focus_clock(total_work_periods)
