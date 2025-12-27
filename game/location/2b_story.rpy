#===========================================================================================================================
# Furina variables
#===========================================================================================================================
default nier_lovepoints = 0
default nier_c1_order = 0
default nier_chapter1_done = False
default nier_chapter1_doneMessage = ""
default nier_bonus1_seen = False

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

label nier_gameover:
    scene black with fade
    "You have failed the mission."
    return

#===========================================================================================================================
# Start of Chapter 1
#===========================================================================================================================
label nier_chapter1:
    $ clear_screen()
    dev "{size=40}{color=#d33d3d}WARNING{/color}: If you are sensitive to static, consider lowering sound volume."
    dev "You have been warned."
    play Ambience_one "audio/ambience/gunfire_ambience.mp3" loop volume 0.8
    play BGM_one "audio/bgm/combat_bgm.mp3" loop volume 0.3
    scene black with fade
    "Gunfire and impact noise bleed through the channel as you open the operator connection."
    "The sound comes through unevenly, rising and falling without warning."
    char.player "Unit 2B. Respond. Confirm status."
    "The channel answers with distortion."
    char.player "Unit 2B, please report."
    "Interference swells, then recedes."
    play Effects_one "audio/effects/radio_static.mp3" noloop volume 2
    scene nier_c1_a1 with dissolve
    char.nier "Connection qua... ty is ...raded, Operat..."
    char.player "{think} Is something interfering with our communications?"
    char.player "Your signal is breaking up. Say again."
    play Effects_one "audio/effects/radio_static.mp3" noloop volume 2
    char.nier "Connec... quality is degraded, ...tor."
    char.nier "Unit 2B operational. En... rema... hostiles."
    char.player "Status unclear, please hold."
    char.player "{think}It's getting worse, something is definitely at work. I cannot get a clean lock on her."
    char.player "Stand by. I am switching us to a secondary channel."
    char.player "Hold your position."
    play Effects_one "audio/effects/radio1.mp3" noloop volume 1.5
    char.player "I am adjusting the connection. Let me know if this is clearer."
    play Effects_one "audio/effects/radio_static.mp3" noloop volume 1.5
    char.nier "Signal is... unstable."
    char.player "Understood."
    play Effects_one "audio/effects/radio2.mp3" noloop volume 1.5
    char.player "Remain where you are. Adjusting again."
    char.player "Do not advance until I confirm."
    play Effects_one "audio/effects/radio_static.mp3" noloop volume 1.6
    char.nier "Connection... fluctuating."
    char.player "{think} Still not holding..."
    char.player "Stand by."
    play Effects_one "audio/effects/radio1.mp3" noloop volume 1.5
    char.player "Rerouting."
    char.player "Confirm when you receive me."
    play Effects_one "audio/effects/radio_static.mp3" noloop volume 1.2
    char.nier "Connection... improved."
    char.nier "Receiving you clearly."
    char.player "Affirmative. I have you now, continue your report."
    show nier_comms1 at truecenter with dissolve
    "A visual feed comes online, unstable and grainy, struggling to hold her position."
    "Fragments of ruined structures and drifting smoke frame her movements."
    char.nier "Minor deviations detected."
    char.nier "Internal temperature regulation is lagging."
    char.nier "Motor response feedback is distorted."
    char.player "{think} Prolonged engagement. She has been fighting for too long, her system's strain accumulating."
    char.player "How is your combat effectiveness holding?"
    char.player "Understood."
    char.player "{think} She says she is fine. That does not mean she should stay."
    char.player "{think} Pushing further will only make this worse."
    char.player "I am adjusting mission parameters. Await further instructions."
    char.nier "Acknowledged, awaiting further orders."
    "Silence overtakes the channel as you weight your options."
    char.player "Disengage from forward hostiles and withdraw to the temporary YoRHa safehouse."
    play Effects_one "audio/effects/radio_static.mp3" noloop volume 1.2
    char.nier "Operator, I assess that continued engagement remains within acceptable—"
    char.player "Negative."
    char.player "Your current condition does not support extended combat."
    char.player "Withdraw."
    play Effects_one "audio/effects/radio2.mp3" noloop volume 1.3
    char.player "Coordinates transmitting now."
    char.nier "..."
    hide nier_comms1 at truecenter with dissolve
    stop Ambience_one fadeout 2.0
    "The visual feed follows her as she turns away from the engagement zone, then cuts out as distance and interference take over."
    char.nier "Acknowledged, Operator."
    char.player "{think} She did not sound pleased to hear that order. She always pushes herself past what she should."
    char.player "{think} If it were any other Operator... they would not have told her to retreat."
    char.player "{think} For most, the mission would have mattered more than what it would cost her."
    char.player "I will rendezvous with you at the safehouse. Before you disengage, re-confirm your condition."
    char.player "Report any damage that will require treatment or repair."
    char.nier "...Negative for critical damage."
    char.nier "Sustained load has caused internal strain."
    char.player "Understood. {think}Is she hiding some stuff on purpose...? I'll find out when I see her."
    "The channel has already gone silent, but your gaze lingers on the terminal."
    char.player "{think} Last time, she pushed beyond her limits because the Command ordered it."
    char.player "{think} The mission succeeded, but she barely did."
    "The line was already disconnected but you still look up towards the terminal and mutters"
    char.player "We are not disposable pawns for YoRHa, 2B."
    char.player "I will make sure you survive. Even if I do not."
    char.player "{think} Command would say she can be restored. As if that makes it the same."
    "You stand from the console, fingers lingering for a moment before pulling away."
    char.player "Not this time..."
    "You turn toward the exit. Preparations are already underway. Supplies, tools, whatever she might need. There is nothing more to wait for. You head out for the rendezvous point."
    $ stop_allsound()

    scene nier_c1_b1 with fade
    play Ambience_one "audio/ambience/stealth_ambience.mp3" loop fadein 1.0 volume 0.7
    "The bunker door seals behind you. You try to shut it as quietly as possble as metal clunks softly against each other."
    "You move down the narrow steps, boots scraping softly against the concrete."
    char.player "{think}Surface protocols: minimal movement, minimal contact."
    char.player "{think}Any patrol units wandering gets a visual lock on me won't hesitate. I won't live long to see 2B."
    play Effects_one "audio/effects/footsteps_long.mp3" noloop
    scene nier_c1_b2 with dissolve
    "The alley opens ahead, framed by metal fence and brick walls."
    play Effects_one "audio/effects/robot_noise1.mp3" noloop volume 1.5
    "You slow near the exit as you start to hear mechanical sounds coming from nearby."
    char.player "{think}Recon drones. If they see me first... it's already over."
    "To your left, a rusted ladder runs up the side of a low structured building."
    "You weight the options quickly."
    scene nier_c1_b2_1 with dissolve
    menu:
        "Where do you go?"
        "Go straight and exit the alley":
            scene nier_c1_b3 with dissolve
            "You commit and move forward, nervousness builds up as you cross the threshold of the alley."
            "The sound you heard grows louder as you come face to face with two patrol units."
            char.player "-?!"
            play Effects_one "audio/effects/camera_flash.mp3" noloop
            scene nier_c1_b3_1 with dissolve
            pause 0.5
            play Effects_one "audio/effects/camera_flash.mp3" noloop
            scene nier_c1_b3_2 with dissolve
            "Both of the drone units has spotted you, their optical sensors flare to life."
            npc.drone "Irregular signal detected. Classification: hostile. Commencing elimination."
            char.player "S-shit! I'm spotted...!"
            play Effects_one "audio/effects/laser_single.mp3" noloop
            queue Effects_one "audio/effects/laser_single.mp3" noloop
            "Energy discharge tears through you as the drones execute their directive."
            "Signal lost..."
            jump nier_gameover 


        "Go up the ladder":
            scene nier_c1_b2_2 with dissolve
            "scene is staring at ladder looking up"
            "You stop at the base of the ladder and tilt your head upward. The metal frame disappears into the shadow above."
            char.player "{think}Recon drones favor ground-level sweeps, I should survey a bit before proceeding in the open."
            "Deciding to gather more information, you grip the ladder and begin to climb."
            scene nier_c1_b2_3 with dissolve
            "Each rung creaks softly beneath your weight."
            "You pause once, listening."
            play Effects_one "audio/effects/robot_noise2.mp3" noloop volume 1.5
            char.player "{think}There's definitely a few of them in the area, I should proceed with caution."
            scene nier_c1_b2_4 with dissolve
            "From the rooftop, the street below comes into view."
            "Three... no. Four drone units patrol the area in slow, overlapping paths."
            "Their sensors sweep rhythimcally through the streets."
            char.player "{think}Patrol cycle confirmed."
            char.player "{think}Open movement below would result in immediate termination."
            "You lower yourself slightly, keeping your silhouette below the edge of the structure."
            char.player "{think}I can't just brute force this, I need to study their patterns properly."
            pass

    menu:
        "What do you do?"
        "Study the drones patterns and bypass it":
            scene nier_c1_b4_1 with dissolve
            "The drones continue their patrol below."
            char.player "{think}If I can map our their routes correctly, I should be able to commit to a path they won't spot me."
            char.player "{think}They shouldn't be random..."
            scene nier_c1_b4_2 with dissolve
            "One unit sweeps the street, its sensors beam lingering before rotating away."
            char.player "{think}That's one of the units that was in fron of the alley entrance."
            scene nier_c1_b4_3 with dissolve
            "One unit flew pass the entrance and pauses longer than the rest. The other two drone moves towards different part of the town."
            char.player "{think}There's a delay... right after the second unit turns."
            "You keep watching..."
            "The lead drone rotates away and all their positions have resetted to the start of your mapping."
            char.player "{think}There's definitely a window I can fit in for sure. Let's review."
            char.player "{think}First unit scans the alley directly, if I'm going to move, it hast to be after that scan."
            char.player "{think}The second drone does not scan the alley but clears the entrance. That's my exit."
            char.player "{think}A third drone approaches from the opposite direction. If I go straight, I'll cross it's scan."
            char.player "{think}That leaves only {b}one{b} direction to go..."
            "You commit the sequence to memory."

            menu:
                "When do you leave the alley?"
                "Leave before the first unit finishes scanning":
                    play Effects_one "audio/effects/camera_flash.mp3"
                    scene nier_c1_spotted with dissolve
                    "You move too early."
                    "The scanning beam snaps back toward the alley."
                    "Your timing was off and you were spotted by the drone."
                    npc.drone "Irregular signal detected. Classification: hostile. Commencing elimination."
                    char.player "F-fuck!"
                    play Effects_one "audio/effects/laser_single.mp3"
                    jump nier_gameover

                "Leave immediately after the first unit finishes scanning":
                    "You steady yourself at the edge of the alley."
                    "The first scan passes."
                    scene nier_c1_b4_4 with dissolve
                    pass

                "Wait until the second unit comes":
                    play Effects_one "audio/effects/camera_flash.mp3"
                    scene nier_c1_spotted with dissolve
                    "You moved too late."
                    "The patrol cycle resets and another scan sweeps the alley."
                    "Your delay costs you the opening."
                    npc.drone "Irregular signal detected. Classification: hostile. Commencing elimination."
                    char.player "Shit—!"
                    play Effects_one "audio/effects/laser_single.mp3"
                    jump nier_gameover


            menu:
                "What do you wait for?"
                "Move as soon as the first unit turns away":
                    play Effects_one "audio/effects/camera_flash.mp3"
                    scene nier_c1_spotted with dissolve
                    "You step out too soon."
                    "Another unit catches you as you step out of the alley."
                    "Your movement is immediately detected."
                    npc.drone "Irregular signal detected. Classification: hostile. Commencing elimination."
                    char.player "N-no—!"
                    play Effects_one "audio/effects/laser_single.mp3"
                    jump nier_gameover

                "Move between patrol units":
                    play Effects_one "audio/effects/camera_flash.mp3"
                    scene nier_c1_spotted with dissolve
                    "You misjudge the spacing."
                    "Two scans converge on the alley at once."
                    "There's nowhere to hide."
                    npc.drone "Irregular signal detected. Classification: hostile. Commencing elimination."
                    char.player "Damn it!"
                    play Effects_one "audio/effects/laser_single.mp3"
                    jump nier_gameover

                "Move after the second unit passes":
                    "The second drone glides past the alley without scanning."
                    "The entrance clears."
                    pass
            menu:
                "Which direction do you go?"
                "Turn right":
                    scene nier_c1_b4_5 with dissolve
                    "You turn right immediately, keeping low."
                    "A scan sweeps the street behind you missing you entirely."
                    char.player "{think}Clear."
                    jump nier_c1_safehouse

                "Go left":
                    play Effects_one "audio/effects/camera_flash.mp3"
                    scene nier_c1_spotted with dissolve
                    "You turn left, back toward the path you just cleared."
                    "A scan sweeps the area behind you."
                    "You step directly back into its range."
                    npc.drone "Irregular signal detected. Classification: hostile. Commencing elimination."
                    char.player "—!"
                    play Effects_one "audio/effects/laser_single.mp3"
                    jump nier_gameover

                "Go forward":
                    play Effects_one "audio/effects/camera_flash.mp3"
                    scene nier_c1_spotted with dissolve
                    "You move forward into the street."
                    "A third drone approaches from the opposite direction."
                    "Its sensor beam sweeps across your path mid-step."
                    npc.drone "Irregular signal detected. Classification: hostile. Commencing elimination."
                    char.player "Shit—!"
                    play Effects_one "audio/effects/laser_single.mp3"
                    jump nier_gameover




        "Give up." if not nier_bonus1_seen:
            "...Wait."
            "You really picked this option?"
            "Like."
            "Actually for real?"
            "No take-backs?"
            "..."
            "Wow."
            "I mean, I'm not mad."
            "Just... disappointed."
            "But hey-"
            "2B still needs you."
            "So straighten up."
            "Take a breath."
            "She didn't come this far just for you to quit now."
            "Here. Consider this your encouragement."
            scene nier_bonus1 with dissolve
            "Be better. Don't betray that ass."
            $ nier_bonus1_seen = True
            # dev "I got bored."
            jump nier_gameover



    
    char.player "{think}"

label nier_c1_safehouse:
    scene black with fade

    "After narrowingly escape the patrol units initally, their numbers dialed down."
    "You only had to evade one or two of them on your way to the safe house"
    "detected, 2b saved"


    # "why not fulfil mission"
    # "why care"
    # "weapon"
    # "2b starts questioning"
    

    "Currently WIP"
    jump codex_charSelection


      
