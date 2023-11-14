init python:
    import datetime

    # 初始按钮名称
    if persistent.ontime:
        print("嘟嘟噜")
    else:
        persistent.save_name1 = "2010-12-15 12:51:43 - 无对话"
        persistent.save_name2 = "2010-12-15 12:51:43 - 无对话"
        persistent.save_name3 = "2010-12-15 12:51:43 - 无对话"
        persistent.save_name4 = "2010-12-15 12:51:43 - 无对话"
        persistent.save_name5 = "2010-12-15 12:51:43 - 无对话"
        persistent.save_name6 = "2010-12-15 12:51:43 - 无对话"
        persistent.save_name7 = "2010-12-15 12:51:43 - 无对话"
        persistent.save_name8 = "2010-12-15 12:51:43 - 无对话"
        persistent.save_name9 = "2010-12-15 12:51:43 - 无对话"
        persistent.save_name10 = "2010-12-15 12:51:43 - 无对话"
    def update_button_name1():
        global save_name1, conversation_log
        # 获取 Conversation Log 的最后一行内容
        last_line = conversation_log[-1].strip() if conversation_log else "无对话"
        if len(last_line) > 20:
           last_line = last_line[:20] + "...』"
        # 更新按钮名称为当前时间和最后一行对话
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        persistent.save_name1 = "{} - {}".format(current_time,last_line)
    def update_button_name2():
        global save_name1, conversation_log
        last_line2 = conversation_log[-1].strip() if conversation_log else "无对话"
        if len(last_line2) > 20:
           last_line2 = last_line2[:20] + "...』"
        # 更新按钮名称为当前时间和最后一行对话
        current_time2 = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        persistent.save_name2 = "{} - {}".format(current_time2,last_line2)
    def update_button_name3():
        global save_name1, conversation_log
        last_line3 = conversation_log[-1].strip() if conversation_log else "无对话"
        if len(last_line3) > 20:
           last_line3 = last_line3[:20] + "...』"
        # 更新按钮名称为当前时间和最后一行对话
        current_time3 = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        persistent.save_name3 = "{} - {}".format(current_time3,last_line3)
    def update_button_name4():
        global save_name1, conversation_log
        last_line4 = conversation_log[-1].strip() if conversation_log else "无对话"
        if len(last_line4) > 20:
           last_line4 = last_line4[:20] + "...』"
        # 更新按钮名称为当前时间和最后一行对话
        current_time4 = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        persistent.save_name4 = "{} - {}".format(current_time4,last_line4)
    def update_button_name5():
        global save_name1, conversation_log
        last_line5 = conversation_log[-1].strip() if conversation_log else "无对话"
        if len(last_line5) > 20:
           last_line5 = last_line5[:20] + "...』"
        # 更新按钮名称为当前时间和最后一行对话
        current_time5 = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        persistent.save_name5 = "{} - {}".format(current_time5,last_line5)
    def update_button_name6():
        global save_name1, conversation_log
        last_line6 = conversation_log[-1].strip() if conversation_log else "无对话"
        if len(last_line6) > 20:
           last_line6 = last_line6[:20] + "...』"
        # 更新按钮名称为当前时间和最后一行对话
        current_time6 = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        persistent.save_name6 = "{} - {}".format(current_time6,last_line6)
    def update_button_name7():
        global save_name1, conversation_log
        last_line7 = conversation_log[-1].strip() if conversation_log else "无对话"
        if len(last_line7) > 20:
           last_line7 = last_line7[:20] + "...』"
        # 更新按钮名称为当前时间和最后一行对话
        current_time7 = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        persistent.save_name7 = "{} - {}".format(current_time7,last_line7)
    def update_button_name8():
        global save_name1, conversation_log
        last_line8 = conversation_log[-1].strip() if conversation_log else "无对话"
        if len(last_line8) > 20:
           last_line8 = last_line8[:20] + "...』"
        # 更新按钮名称为当前时间和最后一行对话
        current_time8 = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        persistent.save_name8 = "{} - {}".format(current_time8,last_line8)
    def update_button_name9():
        global save_name1, conversation_log
        last_line9 = conversation_log[-1].strip() if conversation_log else "无对话"
        if len(last_line9) > 20:
           last_line9 = last_line9[:20] + "...』"
        # 更新按钮名称为当前时间和最后一行对话
        current_time9 = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        persistent.save_name9 = "{} - {}".format(current_time9,last_line9)
    def update_button_name10():
        global save_name1, conversation_log
        last_line10 = conversation_log[-1].strip() if conversation_log else "无对话"
        if len(last_line10) > 20:
           last_line10 = last_line10[:20] + "...』"
        # 更新按钮名称为当前时间和最后一行对话
        current_time10 = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        persistent.save_name10 = "{} - {}".format(current_time10,last_line10)