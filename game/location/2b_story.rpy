#===========================================================================================================================
# Furina variables
#===========================================================================================================================
default nier_lovepoints = 0
default nier_c1_order = 0
default nier_chapter1_done = False
default nier_chapter1_doneMessage = ""

# {color=#d33d3d}[char.player]{/color}

#===========================================================================================================================
# 2B Video variables
#===========================================================================================================================




label nier_chapterSelect:
    $ clear_screen()
    menu:
        "Chapter 1 - WIP[ ' - Completed' if nier_chapter1_done else '' ]":
            play Effects_one "audio/effects/game_start.mp3" noloop volume 2
            jump nier_chapter1
        "Chapter 2 - WIP" if nier_chapter1_done == True:
            "Currently WIP"
            jump hero_bedroom


#===========================================================================================================================
# Start of Chapter 1
#===========================================================================================================================
label nier_chapter1:
    $ clear_screen()
    $ stop_allsound()
    "Currently WIP"
    jump codex_charSelection


      
    