import os
def save_conversation_log1():
    save_folder = "gpt_save"
    save_path = os.path.join(config.gamedir, save_folder, "gpt_save1.json")
    if not os.path.exists(os.path.join(config.gamedir, save_folder)):
        os.makedirs(os.path.join(config.gamedir, save_folder))
    with open(save_path, "w") as file:
        file.write("Conversation Log:\n")
        for line in conversation_log:
            file.write(line + "\n")
        file.write("\n\nMessages:\n")
        for message in messages:
                file.write(message + "\n")
    return
def load_conversation_log1():
    save_folder = "gpt_save"
    save_path = os.path.join(config.gamedir, save_folder, "gpt_save1.json")
    conversation_log = []
    messages = []
    if os.path.exists(save_path):
        with open(save_path, "r") as file:
            lines = file.readlines()
            is_reading_messages = False
            for line in lines:
                line = line.strip()
                if line == "Messages:":
                    is_reading_messages = True
                    continue
                if is_reading_messages:
                    messages.append(line)
                else:
                    conversation_log.append(line)
    return conversation_log, messages