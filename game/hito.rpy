init -1:
    layeredimage amadeus angry:
        always:
            "images/pose/1/kurisu_angry1.png"
        group pose:
            attribute pose1 default:
                "amadeus_angry_def"
        group mouth:
            pos (0,0)#此为相对坐标，为该动画组件在整个cengdie式图片上的坐标
            attribute mouth1 default:
                "amadeus_angry_mouth"
    image amadeus_angry_def:
        "images/pose/1/kurisu_angry1.png"
init -1 python:
    def amadeus_angry_(st, at):
        if renpy.music.is_playing(channel='voice') and _get_voice_info().tag=="amadeus":
            return ("amadeus_angry_mouth1", .1)#播放口型动画1
        else:
            return ("amadeus_angry_mouth2", .1)
init -1:
#定义口型动画1
    image amadeus_angry_mouth1:
        "images/pose/1/kurisu_angry2.png"
        0.1
        "images/pose/1/kurisu_angry3.png"
        0.1
        "images/pose/1/kurisu_angry2.png"
        0.1
        "images/pose/1/kurisu_angry1.png"
        0.1
        repeat
    image amadeus_angry_mouth2:
        "images/pose/1/kurisu_angry1.png"
        0.2
        repeat
    image amadeus_angry_mouth = DynamicDisplayable(amadeus_angry_)
##########################################
init -1:
    layeredimage amadeus annoyed:
        always:
            "images/pose/1/kurisu_annoyed1.png"
        group pose:
            attribute pose1 default:
                "amadeus_annoyed_def"
        group mouth:
            pos (0,0)#此为相对坐标，为该动画组件在整个cengdie式图片上的坐标
            attribute mouth1 default:
                "amadeus_annoyed_mouth"
    image amadeus_annoyed_def:
        "images/pose/1/kurisu_annoyed1.png"
init -1 python:
    def amadeus_annoyed_(st, at):
        if renpy.music.is_playing(channel='voice') and _get_voice_info().tag=="amadeus":
            return ("amadeus_annoyed_mouth1", .1)#播放口型动画1
        else:
            return ("amadeus_annoyed_mouth2", .1)
init -1:
#定义口型动画1
    image amadeus_annoyed_mouth1:
        "images/pose/1/kurisu_annoyed2.png"
        0.1
        "images/pose/1/kurisu_annoyed3.png"
        0.1
        "images/pose/1/kurisu_annoyed2.png"
        0.1
        "images/pose/1/kurisu_annoyed1.png"
        0.1
        repeat
    image amadeus_annoyed_mouth2:
        "images/pose/1/kurisu_annoyed1.png"
        0.2
        repeat
    image amadeus_annoyed_mouth = DynamicDisplayable(amadeus_annoyed_)
##########################################
init -1:
    layeredimage amadeus blush:
        always:
            "images/pose/1/kurisu_blush1.png"
        group pose:
            attribute pose1 default:
                "amadeus_blush_def"
        group mouth:
            pos (0,0)#此为相对坐标，为该动画组件在整个cengdie式图片上的坐标
            attribute mouth1 default:
                "amadeus_blush_mouth"
    image amadeus_blush_def:
        "images/pose/1/kurisu_blush1.png"
init -1 python:
    def amadeus_blush_(st, at):
        if renpy.music.is_playing(channel='voice') and _get_voice_info().tag=="amadeus":
            return ("amadeus_blush_mouth1", .1)#播放口型动画1
        else:
            return ("amadeus_blush_mouth2", .1)
init -1:
#定义口型动画1
    image amadeus_blush_mouth1:
        "images/pose/1/kurisu_blush2.png"
        0.1
        "images/pose/1/kurisu_blush3.png"
        0.1
        "images/pose/1/kurisu_blush2.png"
        0.1
        "images/pose/1/kurisu_blush1.png"
        0.1
        repeat
    image amadeus_blush_mouth2:
        "images/pose/1/kurisu_blush1.png"
        0.2
        repeat
    image amadeus_blush_mouth = DynamicDisplayable(amadeus_blush_)

##########################################
init -1:
    layeredimage amadeus disappointed:
        always:
            "images/pose/1/kurisu_disappointed1.png"
        group pose:
            attribute pose1 default:
                "amadeus_disappointed_def"
        group mouth:
            pos (0,0)#此为相对坐标，为该动画组件在整个cengdie式图片上的坐标
            attribute mouth1 default:
                "amadeus_disappointed_mouth"
    image amadeus_disappointed_def:
        "images/pose/1/kurisu_disappointed1.png"
init -1 python:
    def amadeus_disappointed_(st, at):
        if renpy.music.is_playing(channel='voice') and _get_voice_info().tag=="amadeus":
            return ("amadeus_disappointed_mouth1", .1)#播放口型动画1
        else:
            return ("amadeus_disappointed_mouth2", .1)
init -1:
#定义口型动画1
    image amadeus_disappointed_mouth1:
        "images/pose/1/kurisu_disappointed2.png"
        0.1
        "images/pose/1/kurisu_disappointed3.png"
        0.1
        "images/pose/1/kurisu_disappointed2.png"
        0.1
        "images/pose/1/kurisu_disappointed1.png"
        0.1
        repeat
    image amadeus_disappointed_mouth2:
        "images/pose/1/kurisu_disappointed1.png"
        0.2
        repeat
    image amadeus_disappointed_mouth = DynamicDisplayable(amadeus_disappointed_)

##########################################
init -1:
    layeredimage amadeus eyes_closed:
        always:
            "images/pose/1/kurisu_eyes_closed1.png"
        group pose:
            attribute pose1 default:
                "amadeus_eyes_closed_def"
        group mouth:
            pos (0,0)#此为相对坐标，为该动画组件在整个cengdie式图片上的坐标
            attribute mouth1 default:
                "amadeus_eyes_closed_mouth"
    image amadeus_eyes_closed_def:
        "images/pose/1/kurisu_eyes_closed1.png"
init -1 python:
    def amadeus_eyes_closed_(st, at):
        if renpy.music.is_playing(channel='voice') and _get_voice_info().tag=="amadeus":
            return ("amadeus_eyes_closed_mouth1", .1)#播放口型动画1
        else:
            return ("amadeus_eyes_closed_mouth2", .1)
init -1:
#定义口型动画1
    image amadeus_eyes_closed_mouth1:
        "images/pose/1/kurisu_eyes_closed2.png"
        0.1
        "images/pose/1/kurisu_eyes_closed3.png"
        0.1
        "images/pose/1/kurisu_eyes_closed2.png"
        0.1
        "images/pose/1/kurisu_eyes_closed1.png"
        0.1
        repeat
    image amadeus_eyes_closed_mouth2:
        "images/pose/1/kurisu_eyes_closed1.png"
        0.2
        repeat
    image amadeus_eyes_closed_mouth = DynamicDisplayable(amadeus_eyes_closed_)

##########################################
init -1:
    layeredimage amadeus happy:
        always:
            "images/pose/1/kurisu_happy1.png"
        group pose:
            attribute pose1 default:
                "amadeus_happy_def"
        group mouth:
            pos (0,0)#此为相对坐标，为该动画组件在整个cengdie式图片上的坐标
            attribute mouth1 default:
                "amadeus_happy_mouth"
    image amadeus_happy_def:
        "images/pose/1/kurisu_happy1.png"
init -1 python:
    def amadeus_happy_(st, at):
        if renpy.music.is_playing(channel='voice') and _get_voice_info().tag=="amadeus":
            return ("amadeus_happy_mouth1", .1)#播放口型动画1
        else:
            return ("amadeus_happy_mouth2", .1)
init -1:
#定义口型动画1
    image amadeus_happy_mouth1:
        "images/pose/1/kurisu_happy2.png"
        0.1
        "images/pose/1/kurisu_happy3.png"
        0.1
        "images/pose/1/kurisu_happy2.png"
        0.1
        "images/pose/1/kurisu_happy1.png"
        0.1
        repeat
    image amadeus_happy_mouth2:
        "images/pose/1/kurisu_happy1.png"
        0.2
        repeat
    image amadeus_happy_mouth = DynamicDisplayable(amadeus_happy_)

##########################################
init -1:
    layeredimage amadeus indifferent:
        always:
            "images/pose/1/kurisu_indifferent1.png"
        group pose:
            attribute pose1 default:
                "amadeus_indifferent_def"
        group mouth:
            pos (0,0)#此为相对坐标，为该动画组件在整个cengdie式图片上的坐标
            attribute mouth1 default:
                "amadeus_indifferent_mouth"
    image amadeus_indifferent_def:
        "images/pose/1/kurisu_indifferent1.png"
init -1 python:
    def amadeus_indifferent_(st, at):
        if renpy.music.is_playing(channel='voice') and _get_voice_info().tag=="amadeus":
            return ("amadeus_indifferent_mouth1", .1)#播放口型动画1
        else:
            return ("amadeus_indifferent_mouth2", .1)
init -1:
#定义口型动画1
    image amadeus_indifferent_mouth1:
        "images/pose/1/kurisu_indifferent2.png"
        0.1
        "images/pose/1/kurisu_indifferent3.png"
        0.1
        "images/pose/1/kurisu_indifferent2.png"
        0.1
        "images/pose/1/kurisu_indifferent1.png"
        0.1
        repeat
    image amadeus_indifferent_mouth2:
        "images/pose/1/kurisu_indifferent1.png"
        0.2
        repeat
    image amadeus_indifferent_mouth = DynamicDisplayable(amadeus_indifferent_)

##########################################
init -1:
    layeredimage amadeus normal:
        always:
            "images/pose/1/kurisu_normal1.png"
        group pose:
            attribute pose1 default:
                "amadeus_normal_def"
        group mouth:
            pos (0,0)#此为相对坐标，为该动画组件在整个cengdie式图片上的坐标
            attribute mouth1 default:
                "amadeus_normal_mouth"
    image amadeus_normal_def:
        "images/pose/1/kurisu_normal1.png"
init -1 python:
    def amadeus_normal_(st, at):
        if renpy.music.is_playing(channel='voice') and _get_voice_info().tag=="amadeus":
            return ("amadeus_normal_mouth1", .1)#播放口型动画1
        else:
            return ("amadeus_normal_mouth2", .1)
init -1:
#定义口型动画1
    image amadeus_normal_mouth1:
        "images/pose/1/kurisu_normal2.png"
        0.1
        "images/pose/1/kurisu_normal3.png"
        0.1
        "images/pose/1/kurisu_normal2.png"
        0.1
        "images/pose/1/kurisu_normal1.png"
        0.1
        repeat
    image amadeus_normal_mouth2:
        "images/pose/1/kurisu_normal1.png"
        0.2
        repeat
    image amadeus_normal_mouth = DynamicDisplayable(amadeus_normal_)

##########################################
init -1:
    layeredimage amadeus pissed:
        always:
            "images/pose/1/kurisu_pissed1.png"
        group pose:
            attribute pose1 default:
                "amadeus_pissed_def"
        group mouth:
            pos (0,0)#此为相对坐标，为该动画组件在整个cengdie式图片上的坐标
            attribute mouth1 default:
                "amadeus_pissed_mouth"
    image amadeus_pissed_def:
        "images/pose/1/kurisu_pissed1.png"
init -1 python:
    def amadeus_pissed_(st, at):
        if renpy.music.is_playing(channel='voice') and _get_voice_info().tag=="amadeus":
            return ("amadeus_pissed_mouth1", .1)#播放口型动画1
        else:
            return ("amadeus_pissed_mouth2", .1)
init -1:
#定义口型动画1
    image amadeus_pissed_mouth1:
        "images/pose/1/kurisu_pissed2.png"
        0.1
        "images/pose/1/kurisu_pissed3.png"
        0.1
        "images/pose/1/kurisu_pissed2.png"
        0.1
        "images/pose/1/kurisu_pissed1.png"
        0.1
        repeat
    image amadeus_pissed_mouth2:
        "images/pose/1/kurisu_pissed1.png"
        0.2
        repeat
    image amadeus_pissed_mouth = DynamicDisplayable(amadeus_pissed_)

##########################################
init -1:
    layeredimage amadeus sad:
        always:
            "images/pose/1/kurisu_sad1.png"
        group pose:
            attribute pose1 default:
                "amadeus_sad_def"
        group mouth:
            pos (0,0)#此为相对坐标，为该动画组件在整个cengdie式图片上的坐标
            attribute mouth1 default:
                "amadeus_sad_mouth"
    image amadeus_sad_def:
        "images/pose/1/kurisu_sad1.png"
init -1 python:
    def amadeus_sad_(st, at):
        if renpy.music.is_playing(channel='voice') and _get_voice_info().tag=="amadeus":
            return ("amadeus_sad_mouth1", .1)#播放口型动画1
        else:
            return ("amadeus_sad_mouth2", .1)
init -1:
#定义口型动画1
    image amadeus_sad_mouth1:
        "images/pose/1/kurisu_sad2.png"
        0.1
        "images/pose/1/kurisu_sad3.png"
        0.1
        "images/pose/1/kurisu_sad2.png"
        0.1
        "images/pose/1/kurisu_sad1.png"
        0.1
        repeat
    image amadeus_sad_mouth2:
        "images/pose/1/kurisu_sad1.png"
        0.2
        repeat
    image amadeus_sad_mouth = DynamicDisplayable(amadeus_sad_)

##########################################
init -1:
    layeredimage amadeus side:
        always:
            "images/pose/1/kurisu_side1.png"
        group pose:
            attribute pose1 default:
                "amadeus_side_def"
        group mouth:
            pos (0,0)#此为相对坐标，为该动画组件在整个cengdie式图片上的坐标
            attribute mouth1 default:
                "amadeus_side_mouth"
    image amadeus_side_def:
        "images/pose/1/kurisu_side1.png"
init -1 python:
    def amadeus_side_(st, at):
        if renpy.music.is_playing(channel='voice') and _get_voice_info().tag=="amadeus":
            return ("amadeus_side_mouth1", .1)#播放口型动画1
        else:
            return ("amadeus_side_mouth2", .1)
init -1:
#定义口型动画1
    image amadeus_side_mouth1:
        "images/pose/1/kurisu_side2.png"
        0.1
        "images/pose/1/kurisu_side3.png"
        0.1
        "images/pose/1/kurisu_side2.png"
        0.1
        "images/pose/1/kurisu_side1.png"
        0.1
        repeat
    image amadeus_side_mouth2:
        "images/pose/1/kurisu_side1.png"
        0.2
        repeat
    image amadeus_side_mouth = DynamicDisplayable(amadeus_side_)

##########################################
init -1:
    layeredimage amadeus winking:
        always:
            "images/pose/1/kurisu_winking1.png"
        group pose:
            attribute pose1 default:
                "amadeus_winking_def"
        group mouth:
            pos (0,0)#此为相对坐标，为该动画组件在整个cengdie式图片上的坐标
            attribute mouth1 default:
                "amadeus_winking_mouth"
    image amadeus_winking_def:
        "images/pose/1/kurisu_winking1.png"
init -1 python:
    def amadeus_winking_(st, at):
        if renpy.music.is_playing(channel='voice') and _get_voice_info().tag=="amadeus":
            return ("amadeus_winking_mouth1", .1)#播放口型动画1
        else:
            return ("amadeus_winking_mouth2", .1)
init -1:
#定义口型动画1
    image amadeus_winking_mouth1:
        "images/pose/1/kurisu_winking2.png"
        0.1
        "images/pose/1/kurisu_winking3.png"
        0.1
        "images/pose/1/kurisu_winking2.png"
        0.1
        "images/pose/1/kurisu_winking1.png"
        0.1
        repeat
    image amadeus_winking_mouth2:
        "images/pose/1/kurisu_winking1.png"
        0.2
        repeat
    image amadeus_winking_mouth = DynamicDisplayable(amadeus_winking_)

##########################################
init -1:
    layeredimage amadeus sided_angry:
        always:
            "images/pose/1/kurisu_sided_angry1.png"
        group pose:
            attribute pose1 default:
                "amadeus_sided_angry_def"
        group mouth:
            pos (0,0)#此为相对坐标，为该动画组件在整个cengdie式图片上的坐标
            attribute mouth1 default:
                "amadeus_sided_angry_mouth"
    image amadeus_sided_angry_def:
        "images/pose/1/kurisu_sided_angry1.png"
init -1 python:
    def amadeus_sided_angry_(st, at):
        if renpy.music.is_playing(channel='voice') and _get_voice_info().tag=="amadeus":
            return ("amadeus_sided_angry_mouth1", .1)#播放口型动画1
        else:
            return ("amadeus_sided_angry_mouth2", .1)
init -1:
#定义口型动画1
    image amadeus_sided_angry_mouth1:
        "images/pose/1/kurisu_sided_angry2.png"
        0.1
        "images/pose/1/kurisu_sided_angry3.png"
        0.1
        "images/pose/1/kurisu_sided_angry2.png"
        0.1
        "images/pose/1/kurisu_sided_angry1.png"
        0.1
        repeat
    image amadeus_sided_angry_mouth2:
        "images/pose/1/kurisu_sided_angry1.png"
        0.2
        repeat
    image amadeus_sided_angry_mouth = DynamicDisplayable(amadeus_sided_angry_)

##########################################
init -1:
    layeredimage amadeus sided_blush:
        always:
            "images/pose/1/kurisu_sided_blush1.png"
        group pose:
            attribute pose1 default:
                "amadeus_sided_blush_def"
        group mouth:
            pos (0,0)#此为相对坐标，为该动画组件在整个cengdie式图片上的坐标
            attribute mouth1 default:
                "amadeus_sided_blush_mouth"
    image amadeus_sided_blush_def:
        "images/pose/1/kurisu_sided_blush1.png"
init -1 python:
    def amadeus_sided_blush_(st, at):
        if renpy.music.is_playing(channel='voice') and _get_voice_info().tag=="amadeus":
            return ("amadeus_sided_blush_mouth1", .1)#播放口型动画1
        else:
            return ("amadeus_sided_blush_mouth2", .1)
init -1:
#定义口型动画1
    image amadeus_sided_blush_mouth1:
        "images/pose/1/kurisu_sided_blush2.png"
        0.1
        "images/pose/1/kurisu_sided_blush3.png"
        0.1
        "images/pose/1/kurisu_sided_blush2.png"
        0.1
        "images/pose/1/kurisu_sided_blush1.png"
        0.1
        repeat
    image amadeus_sided_blush_mouth2:
        "images/pose/1/kurisu_sided_blush1.png"
        0.2
        repeat
    image amadeus_sided_blush_mouth = DynamicDisplayable(amadeus_sided_blush_)

##########################################
init -1:
    layeredimage amadeus sided_eyes_closed:
        always:
            "images/pose/1/kurisu_sided_eyes_closed1.png"
        group pose:
            attribute pose1 default:
                "amadeus_sided_eyes_closed_def"
        group mouth:
            pos (0,0)#此为相对坐标，为该动画组件在整个cengdie式图片上的坐标
            attribute mouth1 default:
                "amadeus_sided_eyes_closed_mouth"
    image amadeus_sided_eyes_closed_def:
        "images/pose/1/kurisu_sided_eyes_closed1.png"
init -1 python:
    def amadeus_sided_eyes_closed_(st, at):
        if renpy.music.is_playing(channel='voice') and _get_voice_info().tag=="amadeus":
            return ("amadeus_sided_eyes_closed_mouth1", .1)#播放口型动画1
        else:
            return ("amadeus_sided_eyes_closed_mouth2", .1)
init -1:
#定义口型动画1
    image amadeus_sided_eyes_closed_mouth1:
        "images/pose/1/kurisu_sided_eyes_closed2.png"
        0.1
        "images/pose/1/kurisu_sided_eyes_closed3.png"
        0.1
        "images/pose/1/kurisu_sided_eyes_closed2.png"
        0.1
        "images/pose/1/kurisu_sided_eyes_closed1.png"
        0.1
        repeat
    image amadeus_sided_eyes_closed_mouth2:
        "images/pose/1/kurisu_sided_eyes_closed1.png"
        0.2
        repeat
    image amadeus_sided_eyes_closed_mouth = DynamicDisplayable(amadeus_sided_eyes_closed_)

##########################################
init -1:
    layeredimage amadeus sided_pleasant:
        always:
            "images/pose/1/kurisu_sided_pleasant1.png"
        group pose:
            attribute pose1 default:
                "amadeus_sided_pleasant_def"
        group mouth:
            pos (0,0)#此为相对坐标，为该动画组件在整个cengdie式图片上的坐标
            attribute mouth1 default:
                "amadeus_sided_pleasant_mouth"
    image amadeus_sided_pleasant_def:
        "images/pose/1/kurisu_sided_pleasant1.png"
init -1 python:
    def amadeus_sided_pleasant_(st, at):
        if renpy.music.is_playing(channel='voice') and _get_voice_info().tag=="amadeus":
            return ("amadeus_sided_pleasant_mouth1", .1)#播放口型动画1
        else:
            return ("amadeus_sided_pleasant_mouth2", .1)
init -1:
#定义口型动画1
    image amadeus_sided_pleasant_mouth1:
        "images/pose/1/kurisu_sided_pleasant2.png"
        0.1
        "images/pose/1/kurisu_sided_pleasant3.png"
        0.1
        "images/pose/1/kurisu_sided_pleasant2.png"
        0.1
        "images/pose/1/kurisu_sided_pleasant1.png"
        0.1
        repeat
    image amadeus_sided_pleasant_mouth2:
        "images/pose/1/kurisu_sided_pleasant1.png"
        0.2
        repeat
    image amadeus_sided_pleasant_mouth = DynamicDisplayable(amadeus_sided_pleasant_)

##########################################
init -1:
    layeredimage amadeus sided_surprised:
        always:
            "images/pose/1/kurisu_sided_surprised1.png"
        group pose:
            attribute pose1 default:
                "amadeus_sided_surprised_def"
        group mouth:
            pos (0,0)#此为相对坐标，为该动画组件在整个cengdie式图片上的坐标
            attribute mouth1 default:
                "amadeus_sided_surprised_mouth"
    image amadeus_sided_surprised_def:
        "images/pose/1/kurisu_sided_surprised1.png"
init -1 python:
    def amadeus_sided_surprised_(st, at):
        if renpy.music.is_playing(channel='voice') and _get_voice_info().tag=="amadeus":
            return ("amadeus_sided_surprised_mouth1", .1)#播放口型动画1
        else:
            return ("amadeus_sided_surprised_mouth2", .1)
init -1:
#定义口型动画1
    image amadeus_sided_surprised_mouth1:
        "images/pose/1/kurisu_sided_surprised2.png"
        0.1
        "images/pose/1/kurisu_sided_surprised3.png"
        0.1
        "images/pose/1/kurisu_sided_surprised2.png"
        0.1
        "images/pose/1/kurisu_sided_surprised1.png"
        0.1
        repeat
    image amadeus_sided_surprised_mouth2:
        "images/pose/1/kurisu_sided_surprised1.png"
        0.2
        repeat
    image amadeus_sided_surprised_mouth = DynamicDisplayable(amadeus_sided_surprised_)

##########################################
init -1:
    layeredimage amadeus sided_thinking:
        always:
            "images/pose/1/kurisu_sided_thinking1.png"
        group pose:
            attribute pose1 default:
                "amadeus_sided_thinking_def"
        group mouth:
            pos (0,0)#此为相对坐标，为该动画组件在整个cengdie式图片上的坐标
            attribute mouth1 default:
                "amadeus_sided_thinking_mouth"
    image amadeus_sided_thinking_def:
        "images/pose/1/kurisu_sided_thinking1.png"
init -1 python:
    def amadeus_sided_thinking_(st, at):
        if renpy.music.is_playing(channel='voice') and _get_voice_info().tag=="amadeus":
            return ("amadeus_sided_thinking_mouth1", .1)#播放口型动画1
        else:
            return ("amadeus_sided_thinking_mouth2", .1)
init -1:
#定义口型动画1
    image amadeus_sided_thinking_mouth1:
        "images/pose/1/kurisu_sided_thinking2.png"
        0.1
        "images/pose/1/kurisu_sided_thinking3.png"
        0.1
        "images/pose/1/kurisu_sided_thinking2.png"
        0.1
        "images/pose/1/kurisu_sided_thinking1.png"
        0.1
        repeat
    image amadeus_sided_thinking_mouth2:
        "images/pose/1/kurisu_sided_thinking1.png"
        0.2
        repeat
    image amadeus_sided_thinking_mouth = DynamicDisplayable(amadeus_sided_thinking_)

##########################################
init -1:
    layeredimage amadeus sided_worried:
        always:
            "images/pose/1/kurisu_sided_worried1.png"
        group pose:
            attribute pose1 default:
                "amadeus_sided_worried_def"
        group mouth:
            pos (0,0)#此为相对坐标，为该动画组件在整个cengdie式图片上的坐标
            attribute mouth1 default:
                "amadeus_sided_worried_mouth"
    image amadeus_sided_worried_def:
        "images/pose/1/kurisu_sided_worried1.png"
init -1 python:
    def amadeus_sided_worried_(st, at):
        if renpy.music.is_playing(channel='voice') and _get_voice_info().tag=="amadeus":
            return ("amadeus_sided_worried_mouth1", .1)#播放口型动画1
        else:
            return ("amadeus_sided_worried_mouth2", .1)
init -1:
#定义口型动画1
    image amadeus_sided_worried_mouth1:
        "images/pose/1/kurisu_sided_worried2.png"
        0.1
        "images/pose/1/kurisu_sided_worried3.png"
        0.1
        "images/pose/1/kurisu_sided_worried2.png"
        0.1
        "images/pose/1/kurisu_sided_worried1.png"
        0.1
        repeat
    image amadeus_sided_worried_mouth2:
        "images/pose/1/kurisu_sided_worried1.png"
        0.2
        repeat
    image amadeus_sided_worried_mouth = DynamicDisplayable(amadeus_sided_worried_)

