



label codex_start:
    $ clear_screen()
    scene black with fade
    Codex "Welcome to Codex: Parallel Hearts, a real life simulation visual novel"
    
    
    "Please enter login details"
    $ char.playerInput = renpy.input("Enter your name:")
    $ char.playerInput = char.player.strip()
