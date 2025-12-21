#===========================================================================================================================
# Codex game variables
#===========================================================================================================================
default initial_startup = False



#===========================================================================================================================
# Launch Codex game
#===========================================================================================================================
label codex_start:
    $ clear_screen()
    #===========================================================================================================================
    # Checking if new player
    #===========================================================================================================================
    if not initial_startup:
        scene black with fade
        "You sit down in front of the laptop, adjusting yourself so it feels right."
        "The glow of the monitor lights up the room, casting long shadows across the walls of your room."
        "You feel a quiet excitement as the startup screen for the game appears."

        play BGM_one "audio/bgm/game_bgm1.mp3"
        scene game_mainmenu with blinds
        Codex "Welcome to [Codexp], a real-life simulation visual novel."
        Codex "In this world, every choice you make shapes the relationships, storylines, and your own unique experience."
        Codex "You'll meet characters with distinct personalities, explore different locations, and make decisions that have real consequences."
        Codex "Some choices may lead to friendship, some to rivalry, and others... might make your heart race."
        Codex "Please enter your login details to begin your journey."

        $ char.playerInput = renpy.input("Enter your name:").strip()
        
        if not char.playerInput:
            dev "No name entered. Defaulting to \"Hero\"."
            $ char.player = "Hero"
        else:
            $ char.player = char.playerInput

        $ persistent.player_name = char.player
        $ char.player = Character(char.player, color="#ff0000")
        $ initial_startup = True

        Codex "Welcome player {b}[char.player]{/b}. Have fun and immerse yourself in everything this adventure has to offer."
        dev "This is a demo release of the game. Only Furina's first content is available."

        char.player "Alright... let's dive in and see what this is all about."
        jump furina_chapter1


    Codex "Welcome back plauer [char.player] to [Codexp]. Please enjoy your story."
    return
    # jump codex_charSelection


