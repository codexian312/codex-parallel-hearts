#===========================================================================================================================
# Furina variables
#===========================================================================================================================
default tatsumaki_lovepoints = 0
default tatsumaki_c1_order = 0
default tatsumaki_chapter1_done = False
default tatsumaki_chapter1_doneMessage = ""

# {color=#d33d3d}[char.player]{/color}

#===========================================================================================================================
# Tatsumaki Video variables
#===========================================================================================================================




label tatsumaki_chapterSelect:
    $ clear_screen()
    menu:
        "Chapter 1 - WIP[ ' - Completed' if tatsumaki_chapter1_done else '' ]":
            play Effects_one "audio/effects/game_start.mp3" noloop volume 2
            jump tatsumaki_chapter1
        "Chapter 2 - WIP" if tatsumaki_chapter1_done == True:
            "Currently WIP"
            jump hero_bedroom


#===========================================================================================================================
# Start of Chapter 1
#===========================================================================================================================
label tatsumaki_chapter1:
    $ clear_screen()
    "Currently WIP"
    jump codex_charSelection


      
    