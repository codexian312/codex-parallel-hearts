#===========================================================================================================================
# Custome styles
#===========================================================================================================================
init python:
    import random
    #===========================================================================================================================
    # Think Style
    #===========================================================================================================================
    style.think_style = Style(style.default)
    style.think_style.color = "#ffffff80"  
    style.think_style.bold = False
    style.think_style.italic = True 

    def think_tag(tag, argument, contents):
        return [(renpy.TEXT_TAG, "={}".format("think_style"))] + contents + [(renpy.TEXT_TAG, "/=think_style")]

    config.custom_text_tags["think"] = think_tag

    #===========================================================================================================================
    # Bold + Italics Style
    #===========================================================================================================================

    style.bi_style = Style(style.default)
    style.bi_style.bold = True
    style.bi_style.italic = True

    def bi_tag(tag, argument, contents):
        return [(renpy.TEXT_TAG, "={}".format("bi_style"))] + contents + [(renpy.TEXT_TAG, "/=bi_style")]

    config.custom_text_tags["bi"] = bi_tag
    #===========================================================================================================================
    # Scared/Shaky text
    #===========================================================================================================================
    class ScareText(renpy.Displayable):
        def __init__(self, child, square=5, **kwargs):
            super(ScareText, self).__init__(**kwargs)
            self.child = child
            self.square = square

        def render(self, width, height, st, at):
            xoff = (random.random() - 0.5) * self.square
            yoff = (random.random() - 0.5) * self.square

            child_render = renpy.render(self.child, width, height, st, at)
            self.width, self.height = child_render.get_size()
            render = renpy.Render(self.width, self.height)
            render.subpixel_blit(child_render, (xoff, yoff))
            renpy.redraw(self, 0)
            return render

        def visit(self):
            return [self.child]

    def scare_tag(tag, argument, contents):
        if argument == "":
            argument = 5
        new_list = []
        for kind, text in contents:
            if kind == renpy.TEXT_TEXT:
                for char in text:
                    char_disp = ScareText(renpy.text.text.Text(char), int(argument))
                    new_list.append((renpy.TEXT_DISPLAYABLE, char_disp))
            else:
                new_list.append((kind, text))
        return new_list

    config.custom_text_tags["sc"] = scare_tag
