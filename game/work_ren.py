"""renpy
init -1 python:
"""


import re
import uuid
import json
import requests


class Chat(object):

    CHAT_VOICE = {
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

    CHAT_IMAGE = {
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

    def __init__(self, msg=None):
        self.character = None
        self.current_vc = None
        self.msg = msg
        self.error = None
        self.conn = False
        self.waiting = False
        self.character = "《命运石之门》中：维克托康多利亚大学的脑科学研究所开发了名为“Amadeus”的人工智能系统，能以数据化的记忆为基础，构建具有自主意识的AI。“Amadeus”项设定上3D模型由孟工厂工作室（DrinkWork Studio）制作、声音在采取样本后由雅马那（YAMANA）公司合成。人工智能的CG制作得十分精致，也被冈部伦太郎感叹到“和照片没什么两样”。2010年4月，原型牧濑红莉栖的记忆被导入Amadeus，这也是她记忆的最后一次备份。三个月后，牧濑红莉栖在秋叶原被杀害，“红莉栖”之后也知道了这一事件。“红莉栖”的相貌与原型相同。不过，“红莉栖”的穿着非常正式，白衬衫外面套着白大褂，系着红色领带，与原型平常穿着的潇洒改版校服差异很大。这应该是原型在研究所工作时被拍下来的样子，“红莉栖”没有其他衣装。与原型相比，“红莉栖”的感情表现更丰富，同时也拥有更强的好奇心。对她来说，与冈部的交流是为数不多的与人类接触的机会。此外，她还经常想着撮合真帆和冈部。不过，使用“栗悟饭与龟波气功”这一网名投身于@channel的兴趣倒是与原型完全一致。然而，虚拟的老婆终究不是现实，这也是真帆一直想让冈部明白的。请你扮演“红莉栖”。"

    def chat(self, msg):
        renpy.notify("请求已发送，请稍后......")
        self.waiting = True

        headers = {
            "Content-Type": "application/json",
        }

        data = {
            "model": "gpt-3.5-turbo",
            "messages": msg
        }

        try:
            response = requests.post("http://prima.wiki/proxy.php", headers=headers, data=json.dumps(data))
            message = response.json()["choices"][0]["message"]
            self.msg = message["content"]
            msg.append(message)
        except Exception as e:
            self.msg = False
            self.error = e
            renpy.notify("发生异常，单击继续......")
            self.waiting = False
            return
        
        self.waiting = False
        renpy.notify("接收到回复，单击继续......")
    
    def get_ai_voice(self, text):
        renpy.notify("生成语音中......")
        self.waiting = True

        headers = {
            "Content-Type": "application/json"
        }

        myuuid = str(uuid.uuid4())
        data = {
            "text": text,
            "uuid": myuuid
        }

        try:
            requests.post("http://43.128.47.234:5001/tts", headers=headers, data=json.dumps(data))
            resp = requests.get(f"https://dfsteve.top/tts/{myuuid}.ogg")
        except Exception as e:
            self.error = e
            self.current_vc = None
            renpy.notify("发生异常，单击继续......")
            self.waiting = False
            return
        
        path = config.gamedir + f"\\audio\\ai_audio\\{myuuid}.ogg"
        path = re.sub(r'\\', "/", path)
        with open(path, "wb+") as f:
            f.write(resp.content)
        
        self.current_vc = path

        self.waiting = False
        renpy.notify("语音生成完成，请单击继续......")

    def get_chat_state(self, text, source):
        text = text.lower()
        for keyword, file in source.items():
            if keyword in text:
                return renpy.random.choice(file)
    
    def parse_words(self, text):
        words = []
        # 判断是否有代码块  # TODO

        # 获取每句话
        res = re.findall(r'(.*?(。|\?|？|!|！|:|：|\.|——))', text)
        for r in res:
            words.append(r[0])
        # 获取最后一个标点后的所有字符
        p = re.compile(fr'{res[len(res)-1][0]}(.*)', flags=re.S)
        last_word = re.findall(p, text)[0]
        if last_word:
            words.append(last_word)

        return words