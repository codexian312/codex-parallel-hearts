#===========================================================================================================================
# Real life custom bedroom UI
#===========================================================================================================================



    #===========================================================================================================================
    # Computer (IRL)
    #===========================================================================================================================
screen object_computer:
    imagebutton:
        xpos 991
        ypos 416
        idle "UI/obj_computer.png"
        hover "UI/objSelect_computer.png"
        action [
            Hide("object_computer"),
            Show("computer_screen")
        ]

    #===========================================================================================================================
    # Computer SCREEN (IRL)
    #===========================================================================================================================
screen computer_screen:
    modal True
    add "bedrooms/hero/computer_screen.png"

    imagebutton:
        xpos 388
        ypos 284
        idle "bedrooms/hero/codex_icon.png"
        hover "bedrooms/hero/codex_iconSelect.png"
        action [Play("Effects_one", "audio/effects/mouse_click.mp3", loop=False), Jump("codex_start")]

    imagebutton:
        xpos 1400
        ypos 280
        idle "bedrooms/hero/patreon_icon.png"
        hover "bedrooms/hero/patreon_iconSelect.png"
        action [
            Play("Effects_one", "audio/effects/mouse_click.mp3", loop=False),
            OpenURL("https://www.patreon.com/AeriesGames")
        ]

    imagebutton:
        xpos 1400
        ypos 380
        idle "bedrooms/hero/discord_icon.png"
        hover "bedrooms/hero/discord_iconSelect.png"
        action [
            Play("Effects_one", "audio/effects/mouse_click.mp3", loop=False),
            OpenURL("https://discord.gg/7V9TRA9a")
        ]

    imagebutton:
        xpos 355
        ypos 872
        idle "bedrooms/hero/power_icon.png"
        hover "bedrooms/hero/power_iconSelect.png"
        action [
            Play("Effects_one", "audio/effects/mouse_click.mp3", loop=False),
            Hide("computer_screen"),
            Show("object_computer")
        ]



screen object_bed:
    imagebutton:
        xpos 0
        ypos 374
        idle "UI/obj_bed.png"
        hover "UI/objSelect_bed.png"
        action [
            Hide("object_bed"),
            Jump("real_life")
        ]
