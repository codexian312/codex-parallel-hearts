screen object_computer:
    modal True
    imagebutton:
        xpos 991
        ypos 416
        idle "UI/obj_computer.png"
        hover "UI/objSelect_computer.png"
        action [
            Hide("object_computer"),
            Show("computer_screen")
        ]

screen computer_screen:
    modal True
    add "bedrooms/hero/computer_screen.png"

    imagebutton:
        xpos 388
        ypos 284
        idle "bedrooms/hero/codex_icon.png"
        hover "bedrooms/hero/codex_iconSelect.png"
        action Jump("codex_start")