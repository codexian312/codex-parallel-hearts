#===========================================================================================================================
# Phone (WIP)
#===========================================================================================================================
screen phone_icon:
    imagebutton:
        xpos 1882
        ypos 5
        idle "phone/phone_icon.png"
        hover "phone/phone_hover.png"
        action [Hide("phone_icon"), Show("phone_ui")]

screen phone_ui:
    modal True
    
    imagebutton:
        idle "phone/phone_ui.png"
        xpos 1419
        ypos 22
