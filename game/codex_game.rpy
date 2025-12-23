#===========================================================================================================================
# Codex game variables
#===========================================================================================================================
default initial_startup = False

#===========================================================================================================================
# Game screen scripts
#===========================================================================================================================

# Page Tracker

default route_page = 1
define max_pages = 2  # DON'T FORGET TO INCREASE

# Fixed card positions
define card_positions = [(140, 190), (734, 190), (1328, 190)]

# Cards per page dictionary
define route_cards = {
    1: [
        {"image":"UI/furina_card.png", "hover":"UI/furina_cardSelect.png", "jump":"furina_chapterSelect"},
        # {"image":"UI/no_card.png", "hover":"UI/no_card.png", "jump":"wip_message"},
        # {"image":"UI/no_card.png", "hover":"UI/no_card.png", "jump":"WIP"}
    ],

    2: [
        # {"image":"UI/no_card.png", "hover":"UI/no_card.png", "jump":"WIP"},
        # {"image":"UI/no_card.png", "hover":"UI/no_card.png", "jump":"WIP"},
        # {"image":"UI/no_card.png", "hover":"UI/no_card.png", "jump":"WIP"}
    ]
    # Add pages DON'T FORGET TO INCREASE
}

# ------------------------------
# Page background, arrows, page number
# ------------------------------
screen route_pageSelect():
    add "UI/select_page[route_page].png" xpos 831 ypos 33

    # Back arrow
    if route_page > 1:
        imagebutton:
            idle "UI/select_back.png"
            hover "UI/select_backSelect.png"
            xpos 723 ypos 55
            action SetVariable("route_page", route_page - 1)

    # Next arrow
    if route_page < max_pages:
        imagebutton:
            idle "UI/select_next.png"
            hover "UI/select_nextSelect.png"
            xpos 1143 ypos 55
            action SetVariable("route_page", route_page + 1)

    # Back Button
    imagebutton:
        xpos 5
        ypos 33
        idle "UI/menu_back.png"
        hover "UI/menu_backSelect.png"

        action Jump("hero_bedroom")

# ------------------------------
# Character cards
# ------------------------------
screen route_cards_screen():

    # Loop over positions and cards together using zip
    python:
        positions = card_positions
        cards = route_cards.get(route_page, [])

        # Generate a list of dictionaries for each card to show
        cards_to_show = []
        for pos, card in zip(positions, cards):
            cards_to_show.append({
                "x": pos[0],
                "y": pos[1],
                "idle": card["image"],
                "hover": card["hover"],
                "jump": card["jump"]
            })

    # Now display them using imagebutton blocks
    for c in cards_to_show:
        imagebutton:
            xpos c["x"]
            ypos c["y"]
            idle c["idle"]
            hover c["hover"]
            action [
                Play("Effects_one", "audio/effects/mouse_click.mp3", loop=False),
                Jump(c["jump"])
            ]

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
        Codex "Authenticating login details. Please wait a moment..."
        Codex "..."
        Codex "......"
        Codex ".........Confirmed."
        Codex "Welcome player {b}[char.player]{/b}. Have fun and immerse yourself in everything this adventure has to offer."
        char.player "Alright... let's dive in and see what this is all about."
        $ initial_startup = True

        jump codex_charSelection


    Codex "Welcome back player [char.player] to [Codexp]. Please enjoy your story."
    jump codex_charSelection
    

# ------------------------------
# Label to show route selector
# ------------------------------
label codex_charSelection:
    scene codex_menublur with dissolve
    show screen route_pageSelect
    show screen route_cards_screen
    $ ui.interact()
    return
