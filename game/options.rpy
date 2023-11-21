## 此文件包含有可自定义您游戏的设置。
##

## 游戏版本号。
$ persistent.vits = True
define config.version = "1.4.3"
define version = "·新增了存读档系统和历史记录系统！！！\n·化了设置菜单排版，作者信息移到了 关于。\n·微调了语音系统，现在包括人名，作品名等一些专有名词不会念错了。\n·更多细微调整。"
## 以“##”开头的语句是注释，您不应该对其取消注释。以“#”开头的语句是注释掉的代码，
## 在适用的时候您可能需要对其取消注释。
screen gpt_save:
    add renpy.store.random_bg
    add "black1"
    vbox:
        xpos 0.1
        ypos 0.1
        spacing 30
        if persistent.save1:
           textbutton ("「空存档位1」") action [Function(save_conversation_log1),SetVariable("persistent.save1",False),Function(update_button_name1),SetVariable("persistent.ontime",True)]
        else:
           textbutton ("「[persistent.save_name1]」") action [Function(save_conversation_log1),Function(update_button_name1),SetVariable("persistent.ontime",True)]
        if persistent.save2:
           textbutton ("「空存档位2」") action [Function(save_conversation_log2),SetVariable("persistent.save2",False),Function(update_button_name2),SetVariable("persistent.ontime",True)]
        else:
           textbutton ("「[persistent.save_name2]」") action [Function(save_conversation_log2),Function(update_button_name2),SetVariable("persistent.ontime",True)]
        if persistent.save3:
           textbutton ("「空存档位3」") action [Function(save_conversation_log3),SetVariable("persistent.save3",False),Function(update_button_name3),SetVariable("persistent.ontime",True)]
        else:
           textbutton ("「[persistent.save_name3]」") action [Function(save_conversation_log3),Function(update_button_name3),SetVariable("persistent.ontime",True)]
        if persistent.save4:
           textbutton ("「空存档位4」") action [Function(save_conversation_log4),SetVariable("persistent.save4",False),Function(update_button_name4),SetVariable("persistent.ontime",True)]
        else:
           textbutton ("「[persistent.save_name4]」") action [Function(save_conversation_log4),Function(update_button_name4),SetVariable("persistent.ontime",True)]
        if persistent.save5:
           textbutton ("「空存档位5」") action [Function(save_conversation_log5),SetVariable("persistent.save5",False),Function(update_button_name5),SetVariable("persistent.ontime",True)]
        else:
           textbutton ("「[persistent.save_name5]」") action [Function(save_conversation_log5),Function(update_button_name5),SetVariable("persistent.ontime",True)]
        if persistent.save6:
           textbutton ("「空存档位6」") action [Function(save_conversation_log6),SetVariable("persistent.save6",False),Function(update_button_name6),SetVariable("persistent.ontime",True)]
        else:
           textbutton ("「[persistent.save_name6]」") action [Function(save_conversation_log6),Function(update_button_name6),SetVariable("persistent.ontime",True)]
        if persistent.save7:
           textbutton ("「空存档位7」") action [Function(save_conversation_log7),SetVariable("persistent.save7",False),Function(update_button_name7),SetVariable("persistent.ontime",True)]
        else:
           textbutton ("「[persistent.save_name7]」") action [Function(save_conversation_log7),Function(update_button_name7),SetVariable("persistent.ontime",True)]
        if persistent.save8:
           textbutton ("「空存档位8」") action [Function(save_conversation_log8),SetVariable("persistent.save8",False),Function(update_button_name8),SetVariable("persistent.ontime",True)]
        else:
           textbutton ("「[persistent.save_name8]」") action [Function(save_conversation_log8),Function(update_button_name8),SetVariable("persistent.ontime",True)]
        if persistent.save9:
           textbutton ("「空存档位9」") action [Function(save_conversation_log9),SetVariable("persistent.save9",False),Function(update_button_name9),SetVariable("persistent.ontime",True)]
        else:
           textbutton ("「[persistent.save_name9]」") action [Function(save_conversation_log9),Function(update_button_name9),SetVariable("persistent.ontime",True)]
        if persistent.save10:
           textbutton ("「空存档位10」") action [Function(save_conversation_log10),SetVariable("persistent.save10",False),Function(update_button_name10),SetVariable("persistent.ontime",True)]
        else:
           textbutton ("「[persistent.save_name10]」") action [Function(save_conversation_log10),Function(update_button_name10),SetVariable("persistent.ontime",True)]
    vbox:
        xpos 0
        ypos 0.9
        textbutton ("*点我返回") action Return()
screen gpt_load:
    add renpy.store.random_bg
    add "black1"
    vbox:
        xpos 0.1
        ypos 0.1
        spacing 30
        if persistent.save1:
           textbutton ("「空存档位1」") action ShowMenu("gpt_load")
        else:
           textbutton ([persistent.save_name1]) action Function(load_conversation_log1)
        if persistent.save2:
           textbutton ("「空存档位2」") action ShowMenu("gpt_load")
        else:
           textbutton ([persistent.save_name2]) action Function(load_conversation_log2)
        if persistent.save3:
           textbutton ("「空存档位3」") action ShowMenu("gpt_load")
        else:
           textbutton ([persistent.save_name3]) action Function(load_conversation_log3)
        if persistent.save4:
           textbutton ("「空存档位4」") action ShowMenu("gpt_load")
        else:
           textbutton ([persistent.save_name4]) action Function(load_conversation_log4)
        if persistent.save5:
           textbutton ("「空存档位5」") action ShowMenu("gpt_load")
        else:
           textbutton ([persistent.save_name5]) action Function(load_conversation_log5)
        if persistent.save6:
           textbutton ("「空存档位6」") action ShowMenu("gpt_load")
        else:
           textbutton ([persistent.save_name6]) action Function(load_conversation_log6)
        if persistent.save7:
           textbutton ("「空存档位7」") action ShowMenu("gpt_load")
        else:
           textbutton ([persistent.save_name7]) action Function(load_conversation_log7)
        if persistent.save8:
           textbutton ("「空存档位8」") action ShowMenu("gpt_load")
        else:
           textbutton ([persistent.save_name8]) action Function(load_conversation_log8)
        if persistent.save9:
           textbutton ("「空存档位9」") action ShowMenu("gpt_load")
        else:
           textbutton ([persistent.save_name9]) action Function(load_conversation_log9)
        if persistent.save10:
           textbutton ("「空存档位10」") action ShowMenu("gpt_load")
        else:
           textbutton ([persistent.save_name10]) action Function(load_conversation_log10)
    vbox:
        xpos 0
        ypos 0.9
        textbutton ("*点我返回") action Return()
screen gpt_history():
    add renpy.store.random_bg
    add "black1"
    viewport id "gpt_history_viewport":
        scrollbars "vertical"  # 添加垂直滚动条
        draggable True  # 允许玩家拖动滚动条
        mousewheel True 
        vbox:
            xpos 0.1 
            ypos 0.1
            style "history_gpt"
            if conversation_log == []:
                text "\n\n\n\n\n\n\n\n\n\n\n                                                                        这里还什么都没有。" xcenter 0.5 ycenter 0.5
            else:
                for line in conversation_log:
                    text line
    add "black1" ypos 0.85 alpha 0.5
    vbox:
        xpos 0
        ypos 0.9
        textbutton ("*点我返回") action Return()
screen time:
    vbox:
        xpos 0.016
        ypos 0.04
        imagebutton idle "images/time.png" hover "images/time.png" :
             action ShowMenu("creater")
style custom_slider_style:
    xmaximum 600
style history_gpt:
    xmaximum 1300
screen gpt_about:
    add "BG40N2"
    vbox:
        xpos 0
        ycenter 0.5
        spacing 10
        text "Amadeus"
        text "版本-[config.version]"
        text "作者：{a=https://dfsteve.top}戴夫邻居史蒂夫DFsteve{/a}"
        text "{a=https://github.com/MCDFsteve/AmadeusByRenPyAndChatGPT}点此查看GitHub{/a}"
        text "版本更新内容："
        text "[version]"
    vbox:
        xpos 0
        ypos 0.9
        textbutton ("*点我返回") action Return()
screen creater:
    python:
        if persistent.vits:
            vits_status = "-AI语音"
        else:
            vits_status = "-关键词回复"
    add "BG40N2"
    vbox:
        xpos 0
        ycenter 0.5
        spacing 10
        textbutton ("*关闭AI语音（使用关键词回复，会更快）")  action SetVariable("persistent.vits",False)
        textbutton ("*打开AI语音（即时生成语音对话，会更慢）")  action SetVariable("persistent.vits",True)
        text "*当前语音状态：\n[vits_status]"
        text "*BGM音量调节"
        hbox:
            style "custom_slider_style"
            bar value Preference("music volume")
        textbutton ("*保存") action ShowMenu("gpt_save")
        textbutton ("*读取") action ShowMenu("gpt_load")
        textbutton ("*对话记录") action ShowMenu("gpt_history")
        textbutton ("*关于Amadeus") action ShowMenu("gpt_about")
    vbox:
        xpos 0
        ypos 0.9
        textbutton ("*点我返回") action Return()
    key "pad_b_press" action Return()
    key "game_menu" action Return()
define audio.hello = "audio/hello.ogg"
image BG01A=At("images/BG01A.avif")
image BG13A1=At("images/BG13A1.avif")
image BG18A2=At("images/BG18A2.avif")
image BG05A1=At("images/BG05A1.avif")
image BG40N2=At("images/BG40N2.avif")
image loading= At("images/loading.png")
image BG40A=At("images/BG40A.avif")
image BG42A3=At("images/BG42A3.avif")
image BG91N=At("images/BG91N.avif")
image BG99A=At("images/BG99A.avif")
image BG101A=At("images/BG101A.avif")

image phone1=At("images/phone1.png")
image phone2=At("images/phone2.png")
define gui.interface_text_outlines = [(1,"#000000",1,1)]
define gui.input_text_outlines = [(1,"#000000",1,1)]
define gui.input_prompt_text_outlines = [(1,"#000000",1,1)]
define gui.label_text_outlines = [(1,"#000000",1,1)]
define gui.prompt_text_outlines = [(1,"#000000",0,0)]
define gui.dialogue_text_outlines = [(1,"#000000",1,1)]
define gui.notify_text_outlines = [(1,"#000000",1,1)]
image logo2:
    "images/logo/logo1.png"
    0.04
    "images/logo/logo2.png"
    0.04
    "images/logo/logo3.png"
    0.04
    "images/logo/logo4.png"
    0.04
    "images/logo/logo5.png"
    0.04
    "images/logo/logo6.png"
    0.04
    "images/logo/logo7.png"
    0.04
    "images/logo/logo8.png"
    0.04
    "images/logo/logo9.png"
    0.04
    "images/logo/logo10.png"
    0.04
    "images/logo/logo11.png"
    0.04
    "images/logo/logo12.png"
    0.04
    "images/logo/logo13.png"
    0.04
    "images/logo/logo14.png"
    0.04
    "images/logo/logo15.png"
    0.04
    "images/logo/logo16.png"
    0.04
    "images/logo/logo17.png"
    0.04
    "images/logo/logo18.png"
    0.04
    "images/logo/logo19.png"
    0.04
    "images/logo/logo20.png"
    0.04
    "images/logo/logo21.png"
    0.04
    "images/logo/logo22.png"
    0.04
    "images/logo/logo23.png"
    0.04
    "images/logo/logo24.png"
    0.04
    "images/logo/logo25.png"
    0.04
    "images/logo/logo26.png"
    0.04
    "images/logo/logo27.png"
    0.04
    "images/logo/logo28.png"
    0.04
    "images/logo/logo29.png"
    0.04
    "images/logo/logo30.png"
    0.04
    "images/logo/logo31.png"
    0.04
    "images/logo/logo32.png"
    0.04
    "images/logo/logo33.png"
    0.04
    "images/logo/logo34.png"
    0.04
    "images/logo/logo35.png"
    0.04
    "images/logo/logo36.png"
    0.04
    "images/logo/logo37.png"
    0.04
    "images/logo/logo38.png"
    0.04
    "images/logo/logo39.png"
    0.04
image hito_kotoba:
        xpos 0.63
        ypos 0.488
        "images/anime/output2/01.png"
        0.04
        "images/anime/output2/02.png"
        0.04
        "images/anime/output2/03.png"
        0.04
        "images/anime/output2/04.png"
        0.04
        "images/anime/output2/05.png"
        0.04
        "images/anime/output2/06.png"
        0.04
        "images/anime/output2/07.png"
        0.04
        "images/anime/output2/08.png"
        0.04
        "images/anime/output2/09.png"
        0.04
        "images/anime/output2/10.png"
        0.04
        "images/anime/output2/11.png"
        0.04
        "images/anime/output2/12.png"
        0.04
        "images/anime/output2/13.png"
        0.04
        "images/anime/output2/14.png"
        0.04
        "images/anime/output2/15.png"
        0.04
        "images/anime/output2/16.png"
        0.04
        "images/anime/output2/17.png"
        0.04
        "images/anime/output2/18.png"
        0.04
        "images/anime/output2/19.png"
        0.04
        "images/anime/output2/20.png"
        0.04
        "images/anime/output2/21.png"
        0.04
        "images/anime/output2/22.png"
        0.04
        "images/anime/output2/23.png"
        0.04
        "images/anime/output2/24.png"
        0.04
        "images/anime/output2/25.png"
        0.04
        "images/anime/output2/26.png"
        0.04
        "images/anime/output2/27.png"
        0.04
        "images/anime/output2/28.png"
        0.04
        "images/anime/output2/29.png"
        0.04
        "images/anime/output2/30.png"
        0.04
        "images/anime/output2/31.png"
        0.04
        "images/anime/output2/32.png"
        0.04
        "images/anime/output2/33.png"
        0.04
        "images/anime/output2/34.png"
        0.04
        "images/anime/output2/35.png"
        0.04
        "images/anime/output2/36.png"
        0.04
        "images/anime/output2/37.png"
        0.04
        "images/anime/output2/38.png"
        0.04
        "images/anime/output2/39.png"
        0.04
        "images/anime/output2/40.png"
        0.04
        "images/anime/output2/41.png"
        0.04
        "images/anime/output2/42.png"
        0.04
        "images/anime/output2/43.png"
        0.04
        "images/anime/output2/44.png"
        0.04
        "images/anime/output2/45.png"
        0.04
        "images/anime/output2/46.png"
        0.04
        "images/anime/output2/47.png"
        0.04
        "images/anime/output2/48.png"
        0.04
        "images/anime/output2/49.png"
        0.04
        "images/anime/output2/50.png"
        0.04
        "images/anime/output2/51.png"
        0.04
        "images/anime/output2/52.png"
        0.04
        "images/anime/output2/53.png"
        0.04
        "images/anime/output2/54.png"
        0.04
        "images/anime/output2/55.png"
        0.04
        "images/anime/output2/56.png"
        0.04
        "images/anime/output2/57.png"
        0.04
        "images/anime/output2/58.png"
        0.04
        "images/anime/output2/59.png"
        0.04
        "images/anime/output2/60.png"
        0.04
        repeat
image hito_kotoba2:
        "images/anime/output2/01.png"
        0.04
        "images/anime/output2/02.png"
        0.04
        "images/anime/output2/03.png"
        0.04
        "images/anime/output2/04.png"
        0.04
        "images/anime/output2/05.png"
        0.04
        "images/anime/output2/06.png"
        0.04
        "images/anime/output2/07.png"
        0.04
        "images/anime/output2/08.png"
        0.04
        "images/anime/output2/09.png"
        0.04
        "images/anime/output2/10.png"
        0.04
        "images/anime/output2/11.png"
        0.04
        "images/anime/output2/12.png"
        0.04
        "images/anime/output2/13.png"
        0.04
        "images/anime/output2/14.png"
        0.04
        "images/anime/output2/15.png"
        0.04
        "images/anime/output2/16.png"
        0.04
        "images/anime/output2/17.png"
        0.04
        "images/anime/output2/18.png"
        0.04
        "images/anime/output2/19.png"
        0.04
        "images/anime/output2/20.png"
        0.04
        "images/anime/output2/21.png"
        0.04
        "images/anime/output2/22.png"
        0.04
        "images/anime/output2/23.png"
        0.04
        "images/anime/output2/24.png"
        0.04
        "images/anime/output2/25.png"
        0.04
        "images/anime/output2/26.png"
        0.04
        "images/anime/output2/27.png"
        0.04
        "images/anime/output2/28.png"
        0.04
        "images/anime/output2/29.png"
        0.04
        "images/anime/output2/30.png"
        0.04
        "images/anime/output2/31.png"
        0.04
        "images/anime/output2/32.png"
        0.04
        "images/anime/output2/33.png"
        0.04
        "images/anime/output2/34.png"
        0.04
        "images/anime/output2/35.png"
        0.04
        "images/anime/output2/36.png"
        0.04
        "images/anime/output2/37.png"
        0.04
        "images/anime/output2/38.png"
        0.04
        "images/anime/output2/39.png"
        0.04
        "images/anime/output2/40.png"
        0.04
        "images/anime/output2/41.png"
        0.04
        "images/anime/output2/42.png"
        0.04
        "images/anime/output2/43.png"
        0.04
        "images/anime/output2/44.png"
        0.04
        "images/anime/output2/45.png"
        0.04
        "images/anime/output2/46.png"
        0.04
        "images/anime/output2/47.png"
        0.04
        "images/anime/output2/48.png"
        0.04
        "images/anime/output2/49.png"
        0.04
        "images/anime/output2/50.png"
        0.04
        "images/anime/output2/51.png"
        0.04
        "images/anime/output2/52.png"
        0.04
        "images/anime/output2/53.png"
        0.04
        "images/anime/output2/54.png"
        0.04
        "images/anime/output2/55.png"
        0.04
        "images/anime/output2/56.png"
        0.04
        "images/anime/output2/57.png"
        0.04
        "images/anime/output2/58.png"
        0.04
        "images/anime/output2/59.png"
        0.04
        "images/anime/output2/60.png"
        0.04
        repeat
## 基础 ##########################################################################

## 用户可读的游戏名称。此命令用来设置默认窗口标题，并且会在界面和错误报告中出
## 现。
##
## 带有 _() 的字符串表示其可被翻译。

define config.name = _("Amadeus")


## 决定上面给出的标题是否显示在标题界面屏幕。设置为 False 来隐藏标题。

define gui.show_name = True




## 放置在游戏内“关于”屏幕上的文本。将文本放在三个引号之间，并在段落之间留出空
## 行。

define gui.about = _p("""
""")


## 在构建的发布版中，可执行文件和目录所使用的短名称。此处仅限使用 ASCII 字符，并
## 且不能包含空格、冒号或分号。

define build.name = "Amadeus"


## 音效和音乐 #######################################################################

## 这三个变量控制哪些内置的混音器会默认显示给用户。将其中一个设置为 False 将隐藏
## 对应的混音器。

define config.has_sound = True
define config.has_music = True
define config.has_voice = True


## 为了让用户在音效或语音轨道上播放测试音频，请取消对下面一行的注释并设置播放的
## 样本声音。

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## 将以下语句取消注释就可以设置标题界面播放的背景音乐文件。此文件将在整个游戏中
## 持续播放，直至音乐停止或其他文件开始播放。

# define config.main_menu_music = "main-menu-theme.ogg"


## 转场 ##########################################################################
##
## 这些变量用来控制某些事件发生时的转场。每一个变量都应设置成一个转场，或者是
## None 来表示无转场。

## 进入或退出游戏菜单。
label splashscreen:
    jump start
define config.enter_transition = dissolve
define config.exit_transition = dissolve


## 各个游戏菜单之间的转场。

define config.intra_transition = dissolve


## 载入游戏后使用的转场。

define config.after_load_transition = None


## 在游戏结束之后进入主菜单时使用的转场。

define config.end_game_transition = None


## 用于控制在游戏开始标签不存在时转场的变量。作为替代，在显示初始化场景后使用
## with 语句。


## 窗口管理 ########################################################################
##
## 此命令控制对话框窗口何时显示。若为 show，对话框将总是显示。若为 hide，对话框
## 仅在对话出现时显示。若为 auto，对话框会在 scene 语句前隐藏，并在有新对话时重
## 新显示。
##
## 在游戏开始后，可以用 window show、window hide 和 window auto 语句来改变其状
## 态。

define config.window = "auto"


## 用于显示和隐藏对话框窗口的转场

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## 默认设置 ########################################################################

## 控制默认的文字显示速度。默认的 0 为瞬间，而其他数字则是每秒显示出的字符数。

default preferences.text_cps = 30


## 默认的自动前进延迟。数字越大，等待时间越长，有效范围为 0 - 30。

default preferences.afm_time = 15


## 存档目录 ########################################################################
##
## 控制 Ren'Py 放置游戏存档的特定操作系统目录。存档文件将放置在：
##
## Windows：%APPDATA\RenPy\<config.save_directory>
##
## Macintosh：$HOME/Library/RenPy/<config.save_directory>
##
## Linux：$HOME/.renpy/<config.save_directory>
##
## 该语句通常不应变更，若要变更，应为有效字符串而不是表达式。

define config.save_directory = "Amadeus-1699083661"


## 图标 ##########################################################################
##
## 在任务栏或 Dock 上显示的图标。

define config.window_icon = "gui/window_icon.png"


## 构建配置 ########################################################################
##
## 此部分控制 Ren'Py 如何将您的项目转变为发行版文件。

init python:

    ## 以下函数接受文件模式。文件模式不区分大小写，并与基础目录的相对路径相匹
    ## 配，包括或不包括 /。如果多个模式匹配，则使用第一个模式。
    ##
    ## 在一个模式中：
    ##
    ## / 是目录分隔符。
    ##
    ## * 匹配所有字符，目录分隔符除外。
    ##
    ## ** 匹配所有字符，包括目录分隔符。
    ##
    ## 例如，“*.txt”匹配基础目录中的 txt 文件，“game/**.ogg”匹配游戏目录或任何子
    ## 目录中的 ogg 文件，“**.psd”匹配项目中任何位置的 psd 文件。

    ## 将文件列为 None 来使其从构建的发行版中排除。

    ## 将文件列为 None 来使其从构建的发行版中排除。

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('**.rpy', None)
    build.classify('**.save', None)
    build.classify('audio_temp/', None)
    build.classify('gpt_save/', None)
    build.classify('saves/**.save', None)
    build.classify('**.txt', None)
    build.classify('**.json', None)
    build.classify('**.md', None)
    build.classify('saves/persistent', None)

    ## 若要封装文件，需将其列为“archive”。打包，使其无法被玩家更改

    build.classify('game/**.png', 'archive')
    build.classify('game/**.jpg', 'archive')
    build.classify('game/**.rpyc', 'archive')
    build.classify('game/**.mp3', 'archive')
    build.classify('game/**.wav', 'archive')
    build.classify('game/**.ttf', 'archive')
    build.classify('game/**.otf', 'archive')
    build.classify('game/**.ogg', 'archive')
    build.classify('game/**.webp', 'archive')
    build.classify('game/**.py', 'archive')

    ## 匹配为文档模式的文件会在 Mac 应用程序构建中被复制，因此它们同时出现在 APP
    ## 和 ZIP 文件中。

    build.documentation('*.html')
    build.documentation('*.txt')


## 执行应用内购需要一个 Google Play 许可密钥。许可密钥可以在 Google Play 开发者
## 控制台的“Monetize” > “Monetization Setup” > “Licensing”页面找到。

# define build.google_play_key = "..."


## 与 itch.io 项目相关的用户名和项目名，以 / 分隔。

# define build.itch_project = "renpytom/test-project"
