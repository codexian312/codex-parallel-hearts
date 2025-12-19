#===========================================================================================================================
# Thinking {think}{/think}
#===========================================================================================================================
init python:
    style.think_style = Style(style.default)
    style.think_style.color = "#ffffff80"  
    style.think_style.bold = False
    style.think_style.italic = True 

    def think_tag(tag, argument, contents):
        return [(renpy.TEXT_TAG, "={}".format("think_style"))] + contents + [(renpy.TEXT_TAG, "/=think_style")]

    config.custom_text_tags["think"] = think_tag
