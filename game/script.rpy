transform lo:
         xcenter 0.5
         ycenter 0.5
         zoom 2
transform con:
         xcenter 0.3
         ycenter 0.85
         zoom 1
transform on:
         xcenter 0.84
         ycenter 0.39
transform ti:
         xpos 0.016
         ypos 0.04
transform text:
         xcenter 0.5
         ycenter 0.5
transform on2:
         xcenter 0.845
         ycenter 0.405
transform go:
         xcenter 0.926
         ycenter 0.685
         zoom 1.7
transform girl:
         xcenter 0.84
         ycenter 0.39
         zoom 0.725
init python:
    config.keymap['game_menu'] = []
    config.keymap['rollback'] = []
    config.keymap['screenshot'] = []
    config.keymap['launch_editor'] = []
    config.keymap['reload_game'] = []
    config.keymap['inspector'] = []
    config.keymap['full_inspector'] = []
    config.keymap['developer'] = []
    config.keymap['help'] = []
    config.keymap['choose_renderer'] = []
    config.keymap['progress_screen'] = []
    config.keymap['accessibility'] = []
    config.keymap['bubble_editor'] = []
    config.keymap['self_voicing'] = []
    config.keymap['clipboard_voicing'] = []
    config.keymap['debug_voicing'] = []
    config.keymap['rollforward'] = []
    config.keymap['focus_left'] = []
    config.keymap['focus_right'] = []
    config.keymap['focus_up'] = []
    config.keymap['focus_down'] = []
    config.keymap['skip'] = []
    config.keymap['toggle_skip'] = []
    config.keymap['fast_skip'] = []
    config.keymap['performance'] = []
    config.keymap['image_load_log'] = []
    config.keymap['profile_once'] = []
    config.keymap['memory_profile'] = []
    import requests
    def get_data_from_server(url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.text
            else:
                return None
        except Exception as e:
            print("连接失败：", e)
            return None
    def get_amadeus(url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.text
            else:
                return None
        except Exception as e:
            print("连接失败：", e)
            return None
    hanashi = get_amadeus('http://api.dfsteve.top/amadeus')
    apikey = get_data_from_server('http://api.dfsteve.top/api_key_endpoint')
    keyword_to_voice = {
        "你好": ["hello.ogg","pleased_to_meet_you.ogg","what_do_you_want.ogg"],
        "hello": ["hello.ogg","what_do_you_want.ogg"],
        "hi": ["hello.ogg","what_do_you_want.ogg"],
        "变态": ["devilish_pervert.ogg","pervert_idot_wanttodie.ogg","perverts_go_to_hell.ogg","pervert_confirmed.ogg"],
        "下流": ["devilish_pervert.ogg","pervert_idot_wanttodie.ogg","perverts_go_to_hell.ogg","pervert_confirmed.ogg"],
        "禽兽": ["devilish_pervert.ogg","pervert_idot_wanttodie.ogg","perverts_go_to_hell.ogg","pervert_confirmed.ogg"],
        "事": ["ask_me_whatever.ogg","what_do_you_want.ogg","what_is_it.ogg"],
        "问题": ["ask_me_whatever.ogg","what_do_you_want.ogg","what_is_it.ogg"],
        "问": ["ask_me_whatever.ogg"],
        "克里斯": ["christina.ogg","should_christina.ogg","who_the_hell_christina.ogg","why_christina.ogg"],
        "提娜": ["dont_add_tina.ogg","should_christina.ogg","who_the_hell_christina.ogg","why_christina.ogg"],
        "娜": ["christina.ogg","should_christina.ogg","who_the_hell_christina.ogg","why_christina.ogg"],
        "chr": ["christina.ogg","should_christina.ogg","who_the_hell_christina.ogg","why_christina.ogg"],
        "助手": ["christina.ogg","should_christina.ogg","who_the_hell_christina.ogg","why_christina.ogg"],
        "帮助": ["could_i_help.ogg","what_do_you_want.ogg","what_is_it.ogg"],
        "帮忙": ["could_i_help.ogg","what_do_you_want.ogg","what_is_it.ogg"],
        "拒绝": ["daga_kotowaru.ogg","still_not_happy.ogg"],
        "做不到": ["daga_kotowaru.ogg","sorry.ogg","still_not_happy.ogg"],
        "不要": ["daga_kotowaru.ogg"],
        "zombie": ["dont_call_me_like_that.ogg"],
        "蒙古": ["dont_call_me_like_that.ogg"],
        "天才": ["dont_call_me_like_that.ogg"],
        "@cher": ["gah_extended.ogg"],
        "栗悟饭": ["dont_call_me_like_that.ogg"],
        "@ch": ["gah.ogg"],
        "有趣": ["heheh.ogg"],
        "开": ["heheh.ogg"],
        "哈": ["heheh.ogg"],
        "嘟": ["heheh.ogg"],
        "为": ["huh_why_say.ogg"],
        "why": ["huh_why_say.ogg"],
        "人": ["humans_software.ogg"],
        "是的": ["i_guess.ogg"],
        "这样": ["i_guess.ogg"],
        "总": ["i_guess.ogg"],
        "差": ["i_guess.ogg"],
        "以": ["i_guess.ogg"],
        "啊": ["i_see.ogg","you_sure.ogg"],
        "吗": ["i_see.ogg","you_sure.ogg"],
        "关": ["look_forward_to_working.ogg","pleased_to_meet_you.ogg","what_do_you_want.ogg"],
        "名": ["memories_christina.ogg"],
        "不同": ["memory_complex.ogg"],
        "不一样": ["memory_complex.ogg"],
        "不同": ["modifying_memories_impossible.ogg"],
        "很好": ["nice.ogg"],
        "ni": ["nice.ogg"],
        "冈部伦太郎": ["nice_to_meet_okabe.ogg","pleased_to_meet_you.ogg"],
        "红莉栖": ["nice_to_meet_okabe.ogg","pleased_to_meet_you.ogg"],
        "秘密": ["secret_diary.ogg"],
        "禁止": ["secret_diary.ogg"],
        "前辈": ["senpai_please_dont_tell.ogg","senpai_question.ogg","senpai_questionmark.ogg","senpai_what_we_talkin.ogg","senpai_who_is_this.ogg","uh_senpai.ogg","whats_so_funny_senpai.ogg"],
        "先辈": ["senpai_please_dont_tell.ogg","senpai_question.ogg","senpai_questionmark.ogg","senpai_what_we_talkin.ogg","senpai_who_is_this.ogg","uh_senpai.ogg","whats_so_funny_senpai.ogg"],
        "抱歉": ["sorry.ogg","still_not_happy.ogg"],
        "对不起": ["sorry.ogg","still_not_happy.ogg"],
        "sorry": ["sorry.ogg","still_not_happy.ogg"],
        "厉害": ["sounds_tough.ogg"],
        "de": ["sounds_tough.ogg"],
        "u": ["sounds_tough.ogg"],
        "ch": ["sounds_tough.ogg"],
        "ux": ["sounds_tough.ogg"],
        "windows": ["sounds_tough.ogg"],
        "py": ["sounds_tough.ogg"],
        "x": ["sounds_tough.ogg"],
        "arm": ["sounds_tough.ogg"],
        "mac": ["sounds_tough.ogg"],
        "an": ["sounds_tough.ogg"],
        "os": ["sounds_tough.ogg"],
        "un": ["sounds_tough.ogg"],
        "内核": ["sounds_tough.ogg"],
        "操作": ["sounds_tough.ogg"],
        "呢": ["sounds_tough.ogg"],
        "强": ["sounds_tough.ogg"],
        "受": ["this_guy_hopeless.ogg"],
        "办法": ["this_guy_hopeless.ogg"],
        "居然": ["this_guy_hopeless.ogg"],
        "没救了": ["this_guy_hopeless.ogg"],
        "无聊": ["this_guy_hopeless.ogg"],
        "意思": ["this_guy_hopeless.ogg"],
        "无趣": ["this_guy_hopeless.ogg"],
        "假": ["tm_nonsense.ogg"],
        "说": ["tm_nonsense.ogg"],
        "虚构": ["tm_nonsense.ogg"],
        "胡": ["tm_nonsense.ogg"],
        "不是": ["tm_nonsense.ogg"],
        "时间": ["tm_not_possible.ogg","tm_you_said.ogg"],
        "时光": ["tm_not_possible.ogg","tm_you_said.ogg"],
        "证": ["tm_scientist_no_evidence.ogg"],
        "据": ["tm_scientist_no_evidence.ogg"],
        "开": ["tm_scientist_no_evidence.ogg"],
        "维": ["tm_scientist_no_evidence.ogg"],
        "护": ["tm_scientist_no_evidence.ogg"],
        "明": ["tm_scientist_no_evidence.ogg"],
        "实": ["tm_scientist_no_evidence.ogg"],
        "依": ["tm_scientist_no_evidence.ogg"],
        "根": ["tm_scientist_no_evidence.ogg"],
        "太早": ["tm_too_early.ogg"],
        "提前": ["tm_too_early.ogg"],
        "未知": ["tm_we_dont_know.ogg"],
        "知道": ["tm_we_dont_know.ogg"],
        "是": ["what_is_it.ogg"],
        "什么": ["ok.ogg","sounds_tough.ogg"],
        "啊": ["ok.ogg","sounds_tough.ogg"],
        # 其他关键词和语音文件的映射
    }
init python:
    # 关键词到图像文件的映射
    keyword_to_image = {
        "变态": ["amadeus angry","amadeus sided_angry"],
        "下流": ["amadeus angry","amadeus sided_angry"],
        "畜生": ["amadeus angry","amadeus sided_angry"],
        "禽兽": ["amadeus angry","amadeus sided_angry"],
        "无聊": ["amadeus sided_eyes_closed","amadeus eyes_closed","amadeus annoyed","amadeus indifferent","amadeus pissed","amadeus side","amadeus sided_pleasant","amadeus sided_surprised","amadeus sided_thinking","amadeus sided_worried"],
        "没意思": ["amadeus sided_eyes_closed","amadeus eyes_closed","amadeus annoyed","amadeus indifferent","amadeus pissed","amadeus side","amadeus sided_pleasant","amadeus sided_surprised","amadeus sided_thinking","amadeus sided_worried"],
        "这样": ["amadeus sided_eyes_closed","amadeus eyes_closed","amadeus annoyed","amadeus indifferent","amadeus pissed","amadeus side","amadeus sided_pleasant","amadeus sided_surprised","amadeus sided_thinking","amadeus sided_worried"],
        "无趣": ["amadeus sided_eyes_closed","amadeus eyes_closed","amadeus annoyed","amadeus indifferent","amadeus pissed","amadeus side","amadeus sided_pleasant","amadeus sided_surprised","amadeus sided_thinking","amadeus sided_worried"],
        "真是": ["amadeus sided_eyes_closed","amadeus eyes_closed","amadeus annoyed","amadeus indifferent","amadeus pissed","amadeus side","amadeus sided_pleasant","amadeus sided_surprised","amadeus sided_thinking","amadeus sided_worried"],
        "没救": ["amadeus sided_eyes_closed","amadeus eyes_closed","amadeus annoyed","amadeus indifferent","amadeus pissed","amadeus side","amadeus sided_pleasant","amadeus sided_surprised","amadeus sided_thinking","amadeus sided_worried"],
        "克里斯": ["amadeus blush","amadeus sided_blush","amadeus angry","amadeus sided_angry"],
        "老婆": ["amadeus blush","amadeus sided_blush","amadeus angry","amadeus sided_angry"],
        "媳妇": ["amadeus blush","amadeus sided_blush","amadeus angry","amadeus sided_angry"],
        "爱": ["amadeus blush","amadeus sided_blush","amadeus angry","amadeus sided_angry"],
        "亲": ["amadeus blush","amadeus sided_blush","amadeus angry","amadeus sided_angry"],
        "女": ["amadeus blush","amadeus sided_blush","amadeus angry","amadeus sided_angry"],
        "美": ["amadeus blush","amadeus sided_blush","amadeus angry","amadeus sided_angry"],
        "可爱": ["amadeus blush","amadeus sided_blush","amadeus angry","amadeus sided_angry"],
        "帅": ["amadeus blush","amadeus sided_blush","amadeus angry","amadeus sided_angry"],
        "chri": ["amadeus blush","amadeus sided_blush","amadeus angry","amadeus sided_angry"],
        "@ch": ["amadeus blush","amadeus sided_blush","amadeus angry","amadeus sided_angry"],
        "栗悟饭": ["amadeus blush","amadeus sided_blush","amadeus angry","amadeus sided_angry"],
        "助手": ["amadeus blush","amadeus sided_blush","amadeus angry","amadeus sided_angry"],
        "zombie": ["amadeus blush","amadeus sided_blush","amadeus angry","amadeus sided_angry"],
        "蒙古斑": ["amadeus blush","amadeus sided_blush","amadeus angry","amadeus sided_angry"],
        "天才": ["amadeus blush","amadeus sided_blush","amadeus angry","amadeus sided_angry"],
        "可以": ["amadeus happy","amadeus sided_pleasant","amadeus winking"],
        "棒": ["amadeus happy","amadeus sided_pleasant","amadeus winking"],
        "厉害": ["amadeus happy","amadeus sided_pleasant","amadeus winking"],
        "强": ["amadeus happy","amadeus sided_pleasant","amadeus winking"],
        "是": ["amadeus happy","amadeus sided_pleasant","amadeus winking"],
        "天": ["amadeus happy","amadeus sided_pleasant","amadeus winking"],
        "好": ["amadeus happy","amadeus sided_pleasant","amadeus winking"],
        "哼": ["amadeus happy","amadeus sided_pleasant","amadeus winking"],
        "看": ["amadeus happy","amadeus sided_pleasant","amadeus winking"],
        "说": ["amadeus happy","amadeus sided_pleasant","amadeus winking"],
        "种": ["amadeus happy","amadeus sided_pleasant","amadeus winking"],
        "东": ["amadeus happy","amadeus sided_pleasant","amadeus winking"],
        "西": ["amadeus happy","amadeus sided_pleasant","amadeus winking"],
        "南": ["amadeus happy","amadeus sided_pleasant","amadeus winking"],
        "北": ["amadeus happy","amadeus sided_pleasant","amadeus winking"],
        "吃": ["amadeus happy","amadeus sided_pleasant","amadeus winking"],
        "喝": ["amadeus happy","amadeus sided_pleasant","amadeus winking"],
        "ubun": ["amadeus happy","amadeus sided_pleasant","amadeus winking"],
        "ux": ["amadeus happy","amadeus sided_pleasant","amadeus winking"],
        "un": ["amadeus happy","amadeus sided_pleasant","amadeus winking"],
        "os": ["amadeus happy","amadeus sided_pleasant","amadeus winking"],
        "id": ["amadeus happy","amadeus sided_pleasant","amadeus winking"],
        "win": ["amadeus happy","amadeus sided_pleasant","amadeus winking"],
        "mac": ["amadeus happy","amadeus sided_pleasant","amadeus winking"],
        "86": ["amadeus happy","amadeus sided_pleasant","amadeus winking"],
        "x": ["amadeus happy","amadeus sided_pleasant","amadeus winking"],
        "arm": ["amadeus happy","amadeus sided_pleasant","amadeus winking"],
        "/": ["amadeus happy","amadeus sided_pleasant","amadeus winking"],
        "c": ["amadeus happy","amadeus sided_pleasant","amadeus winking"],
        "命运石之门": ["amadeus happy","amadeus sided_pleasant","amadeus winking"],
        "鸣泣之时": ["amadeus happy","amadeus sided_pleasant","amadeus winking"],
        "不存在": ["amadeus happy","amadeus sided_pleasant","amadeus winking"],
        "十三": ["amadeus happy","amadeus sided_pleasant","amadeus winking"],
        "野": ["amadeus happy","amadeus sided_pleasant","amadeus winking"],
        "传说": ["amadeus happy","amadeus sided_pleasant","amadeus winking"],
        "17": ["amadeus happy","amadeus sided_pleasant","amadeus winking"],
        "kid": ["amadeus happy","amadeus sided_pleasant","amadeus winking"],
        "5pb": ["amadeus happy","amadeus sided_pleasant","amadeus winking"],
        "自": ["amadeus happy","amadeus sided_pleasant","amadeus winking"],
        "me": ["amadeus happy","amadeus sided_pleasant","amadeus winking"],
        "这样": ["amadeus happy","amadeus sided_pleasant","amadeus winking"],
        "哈": ["amadeus happy","amadeus sided_pleasant","amadeus winking"],
        "ga": ["amadeus happy","amadeus sided_pleasant","amadeus winking"],
        "st": ["amadeus happy","amadeus sided_pleasant","amadeus winking"],
        "el": ["amadeus happy","amadeus sided_pleasant","amadeus winking"],
        "@": ["amadeus happy","amadeus sided_pleasant","amadeus winking"],
        "嘟": ["amadeus happy","amadeus sided_pleasant","amadeus winking"],
        "咪": ["amadeus happy","amadeus sided_pleasant","amadeus winking"],
        "可": ["amadeus happy","amadeus sided_pleasant","amadeus winking"],
        "行": ["amadeus happy","amadeus sided_pleasant","amadeus winking"],
        "安": ["amadeus happy","amadeus sided_pleasant","amadeus winking"],
        # 添加更多关键词和图像文件的映射
    }

    
# The game starts here.
image connect = Text("Connect to Kurisu?", size=55,color="#ff9e17")
define e = Character(None,image="phone1", kind=bubble,voice_tag="amadeus", what_prefix='『', what_suffix='』',ctc="hito_kotoba",ctc_position="fixed",what_xoffset= -10,what_textalign=0.0)
define error = Character("",ctc="hito_kotoba2",ctc_position="nestled")
label start:
    scene black
    show connect at con
    play music "ringtone_gate_of_steiner.ogg" fadein 1.0 fadeout 1.0
    show logo2 at lo
    $ renpy.pause(200, hard=False)
    python:
        import socket
        def check_internet_connection():
            try:
        # 建立一个TCP连接来检查网络连接
                socket.create_connection(("dfsteve.top", 80))
                return True
            except OSError:
                return False
        if check_internet_connection():
            renpy.jump("start2")
        else:
            renpy.jump("error")
label error:
    scene BG40N2
    play music "audio/bgm219.ogg"
    jump errorloop
label error2:
    scene BG40N2
    play music "audio/bgm219.ogg"
    jump errorloop2
label errorloop:
    error "\n\n你似乎没有连接网络。请尝试检查联网后重新启动。"
    jump errorloop
label errorloop2:
    error "\n\nAI出现了一些问题。请尝试重新启动。"
    jump errorloop2
label start2:
    play sound "tone.ogg"
    python:
        # 导入random模块
        import random
        # 定义一个包含所有可能标签的列表
        bg_list = ["BG01A", "BG13A1", "BG05A1", "BG18A2","BG101A","BG99A","BG91N","BG42A3","BG40A"]
        bgm_list = ["audio/bgm204.ogg", "audio/bgm205.ogg","audio/bgm212.ogg","audio/bgm216.ogg"]
        # 随机选择一个标签
        renpy.store.random_bg = random.choice(bg_list)
        renpy.store.random_bgm = random.choice(bgm_list)
        # 根据索引调用对应的标签
    scene expression renpy.store.random_bg
    play music renpy.store.random_bgm fadein 1.0 fadeout 1.0 volume 0.5
    show phone2 at on
    show amadeus normal at girl
    show phone3 at on
    show logo at go
    show phone1 at on2
    show screen time
    voice "audio/hello.ogg"
    e "Hello~"
    python:
        import chatgpt
        import io 
        import os
        import urllib
        import urllib.request
        import json
        import tempfile
        import uuid
        import time
        import re
        import shutil
        messages = [
            {"role": "system", "content": hanashi},
            {"role": "assistant", "content": "Hello~"}
        ]
        tts_url = "http://43.128.47.234:5001/tts"
        def send_text_to_tts(text):
            # 准备数据和请求
            data = json.dumps({"text": text,"uuid":myuuid})
            data = data.encode("utf-8")
            req = urllib.request.Request(tts_url, data, {'Content-Type': 'application/json'})
    # 发送请求并接收响应
            try:
                with urllib.request.urlopen(req) as response:
                    if response.getcode() == 200:
                        if not os.path.exists(audio_folder):
                            os.makedirs(audio_folder)
                        with open(audio_file_path, "wb") as audio_file:
                            audio_file.write(response.read())
                        return audio_file_path
                    else:
                        return None
            except urllib.error.HTTPError as e:
                renpy.jump("error2")
            except urllib.error.URLError as e:
                renpy.jump("error2")
            except OSError as e:
                renpy.jump("error2")
            except Exception as e:
                renpy.jump("error2")

# This function splits the text by sentence enders and yields the parts
        def split_by_punctuation(text, max_length=20):
    # Define the regex pattern for sentence enders
            pattern = re.compile(r'。|！|？|!|\?')
            start = 0
            for match in pattern.finditer(text):
                end = match.end()
        # Yield the sentence part
                yield text[start:end]
                start = end
    # Yield any remaining text after the last punctuation mark
            if start < len(text):
                yield text[start:]
        # 这个函数检查文本中是否含有关键词，并返回对应的图像文件名
        def get_image_for_keywords(text):
            text = text.lower()
            for keyword, image_file in keyword_to_image.items():
                if keyword in text:
                    return random.choice(image_file)
            return None
        def get_voice_file_for_keywords(text):
        # 假设关键词和文本都是小写，为了简单起见，我们将输入文本转换为小写
            text = text.lower()
            for keyword, voice_file in keyword_to_voice.items():
                if keyword in text:
                # 如果找到关键词，则随机选择关联的音效之一
                    return random.choice(voice_file)
        # 如果没有找到匹配的关键词，返回 None
            return None
        response = ""
        while True:
    # 使用前面定义的is_connected_to_internet函数来检查网络连接
            # 用户输入
            user_input = renpy.input("", length=100)
            renpy.show("loading")
            to_gpt = user_input
            renpy.pause(0.2)
            config.keymap['dismiss'] = None
            messages.append({"role": "user", "content": to_gpt})
            if check_internet_connection():
            # 原有的API调用代码
              try:
                 messages = chatgpt.completion(messages, proxy="http://prima.wiki/proxy.php")
                 response = messages[-1]["content"]
              except BaseException as e:
                 renpy.jump("error2")
              except Exception as e:
                 renpy.jump("error2")
              except KeyError as e:
                 renpy.jump("error2")
            else:
              renpy.jump("error")
     
    
    # 根据你的游戏逻辑，你可能需要在这里添加break语句来退出循环
    # 例如，如果用户输入了一个特定的命令或者选择了退出
    # if user_input == "quit":
    #     break

    
    # Split the response by punctuation
            for part in split_by_punctuation(response):
        # Display each part in a bubble
                image_file = get_image_for_keywords(part)
                if image_file is not None:
        # 显示对应的图像
                    renpy.show(image_file)
                else:
                    renpy.show("amadeus normal")
                voice_file = get_voice_file_for_keywords(part)
                renpy.hide("loading")
                config.keymap['dismiss'] = None
                #time.sleep(0.5)
                # 确保存放目录存在
                if persistent.vits:
                    myuuid = str(uuid.uuid4())
                    audio_folder = os.path.join(config.gamedir, "audio_temp")
                    audio_file_path = os.path.join(audio_folder,myuuid+".ogg")
                    audio_tts = os.path.join("audio_temp/",myuuid+".ogg")
                    folder_path = "audio_temp"
                    audio_file = send_text_to_tts(part)
                    url = os.path.join("https://dfsteve.top/tts/",myuuid+".ogg")
                    game_directory = config.gamedir
                    destination = os.path.join(game_directory, "audio_temp",myuuid+".ogg")
                    destination = os.path.normpath(destination)
                    if not os.path.exists(os.path.dirname(destination)):
                        os.makedirs(os.path.dirname(destination))
                    # 发起请求并下载文件
                    try:
                        r = requests.get(url)
                        with open(destination, 'wb') as f:
                            f.write(r.content)
                    except requests.exceptions.RequestException as e:
                        renpy.jump("error")
                    except IOError as e:
                        renpy.jump("error")
                    except BaseException as e:
                        renpy.jump("error")
                    except Exception as e:
                        renpy.jump("error")
                    voice(audio_tts)
                    e(part)
                    renpy.pause(0.3)
                    if os.path.exists(audio_file):
                       os.remove(audio_file)
                else:
                    if voice_file is not None:
                       voice(voice_file, tag=None)
                    else:
                       voice("ask_me_whatever.ogg",tag=None)
                    e(part)
                    renpy.pause(0.3) 


    return
