#===========================================================================================================================
# Python Init
#===========================================================================================================================
init python:
    #=======================================================================================================================
    # Channel Logging
    #=======================================================================================================================
    renpy.music.register_channel("Ambience_one", mixer="music")
    renpy.music.register_channel("Ambience_two", mixer="music")
    renpy.music.register_channel("BGM_one", mixer = "music")
    renpy.music.register_channel("BGM_two", mixer = "music")
    renpy.music.register_channel("Effects_one", mixer="sfx")
    renpy.music.register_channel("Effects_two", mixer="sfx")
    renpy.music.register_channel("Effects_three", mixer="sfx")
    renpy.music.register_channel("Voice", mixer="voice")




#===========================================================================================================================
# Characters
#===========================================================================================================================
define dev = "{color=#c4fbff}Aeries{/color}"
define Codex = "{color=#f75ed4}Codex{/color}"
define Codexp = "{color=#f75ed4}Codex: Parallel Hearts{/color}"
define char.randomOne = Character("???", color="#858aca")
define you = Character("You")
define npc.staff = Character("Staff")

default persistent.player_name = ""
define char.furina = Character("Furina", color="#9bd6e0")
define char.bella = Character("Isabella", color="#eeec83")



#===========================================================================================================================
# Start of game / End of game
#===========================================================================================================================
label start:
    dev "Hey! Thanks for picking up my game to try it out. I'm [dev] and this is my first visual novel, or game rather!"
    dev "Let me tell you a little bit about the game. Codex: Parallel Hearts is a story where you can meet and interact with characters inspired by some of your favourite characters!"
    dev "You will experience these stories firsthand, going on dates and forming connections with your chosen character from the [Codex]"
    dev "This project is just the beginning! I hope you enjoy exploring the Codex and these reimagined worlds as much as I enjoyed creating them."
    dev "Your choices, your stories, your hearts, welcome to the [Codex]"

    dev "Disclaimer: This is a demo version. Gameplay and story do not represent the final or released version of the game."
    
    jump hero_bedroom

label end_update:
    dev "You have reached the end of this update! Stay tuned for the next version."  
    dev "If you'd like to support me in making this game, head over to my Patreon."  
    dev "Thanks so much for playing my game, I hope you enjoyed it!"

label end_demo:
    scene black with fade
    dev "You have reached the end of the demo! Stay tuned for the next version."  
    dev "If you'd like to support me in making this game, head over to my Patreon."  
    dev "Thanks so much for playing my game, I hope you enjoyed what little content it had!"
    return
