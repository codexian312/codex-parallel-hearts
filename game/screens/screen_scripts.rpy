#===========================================================================================================================
# Custom screen scripts set up
#===========================================================================================================================

init python:
    def clear_screen():
        screens = ["object_computer", "computer_screen", "route_pageSelect", "route_cards_screen",
        "phone_icon", "phone_ui", "object_bed"]
        for s in screens:
            renpy.hide_screen(s)
