# definitions
define config.rollback_enabled = False
define config.allow_skipping = False
define quick_menu = False

image connect = Text(_("Connect to Kurisu?"), size=45,color="#ff9e17", bold=True)

define e = Character(
    "Amadeus",
    image="phone1", 
    kind=bubble, 
    voice_tag="amadeus", 
    what_prefix='『', 
    what_suffix='』',
    ctc="hito_kotoba",
    ctc_position="fixed", 
    who_yoffset=-1000,
    what_xoffset=-15,
    what_textalign=0.0
)

define me = Character(
    "冈部伦太郎", 
    ctc="hito_kotoba", 
    ctc_position="nestled",
    who_yoffset=-1000,
    what_yoffset=40,
    what_prefix='『', 
    what_suffix='』'
)
define error = Character(None, ctc="hito_kotoba2", ctc_position="nestled", what_yoffset=40)

define chat = Chat()


# 开局标签
label splashscreen:
    play music "ringtone_gate_of_steiner.ogg" fadein 1.0 fadeout 1.0
    scene black
    show logo2 at lo
    show connect at con

    # 初始化
    python:
        renpy.invoke_in_thread(chat.init)
        # 非阻塞式等待（程序不会白屏卡死）
        while chat.waiting:
            renpy.pause()

        # 是否连接成功
        if not chat.conn:
            renpy.call(conn_error, err_info=chat.error)

    pause

    return


# 取消主菜单
label main_menu:
    return


# 退出前清除缓存
label quit:
    python:
        import os
        cache_path = os.path.join(config.gamedir, "/audio/ai_audio")
        if os.path.exists(cache_path):
            for file in os.listdir(cache_path):
                file = f"{cache_path}/{file}"
                os.remove(file)
    return


# 检查网络连接
label conn_error(err_info):
    scene BG40N2
    play music "audio/bgm219.ogg"
    error "[err_info!q]"

    $ renpy.pause(hard=True)    # TODO

    return


# 开始游戏
label start:
    play sound "tone.ogg"

    python:
        bg_list = ["BG01A", "BG13A1", "BG05A1", "BG18A2", "BG101A", "BG99A", "BG91N", "BG42A3", "BG40A"]
        bgm_list = ["audio/bgm204.ogg", "audio/bgm205.ogg", "audio/bgm212.ogg", "audio/bgm216.ogg"]
        bg = renpy.random.choice(bg_list)
        bgm = renpy.random.choice(bgm_list)

    scene expression bg
    play music bgm fadein 1.0 fadeout 1.0 volume 0.5
    show phone2 at on
    show amadeus normal at girl
    show phone3 at on
    show logo at go
    show phone1 at on2
    show screen time

    voice "audio/hello.ogg"
    e "Hello~"
        
    $ messages = [{"role": "system", "content": chat.character}]

    # 聊天主循环
    while True:

        python:
            # 用户输入
            user_input = renpy.input("", length=100)
            messages.append({"role": "user", "content": user_input})
            renpy.invoke_in_thread(chat.chat, messages)
        
        me "[user_input!q]"

        while chat.waiting:
            pause

        if chat.msg:
            $ msg = chat.msg[-1]["content"]
        else:
            call conn_error(err_info=chat.error) from _call_conn_error

        $ words = chat.parse_words(msg)

        default i = 0
        while i <= len(words)-1:
            python:
                w = words[i]
                img = chat.get_chat_state(w, Chat.CHAT_IMAGE)

            # 生成ai语音
            if persistent.voice_source == "ai":
                $ renpy.invoke_in_thread(chat.get_ai_voice, w)
                while chat.waiting:
                    pause
                $ vc = chat.current_vc if chat.current_vc else chat.get_chat_state(w, Chat.CHAT_VOICE)
            else:
                $ vc = chat.get_chat_state(w, Chat.CHAT_VOICE)
            
            if img:
                $ renpy.show(img)
            if vc:
                voice vc

            # 避免不必要的转义输出
            e "[w!q]"

            $ i += 1
