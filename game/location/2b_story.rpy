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
image nier_c1_f6 = Movie(play="scenes/nier/nier_c1_f6.webm", loop=True)
image nier_c1_f9 = Movie(play="scenes/nier/nier_c1_f9.webm", loop=True)
image nier_c1_f30 = Movie(play="scenes/nier/nier_c1_f30.webm", loop=True)
image nier_c1_g2 = Movie(play="scenes/nier/nier_c1_g2.webm", loop=True)
image nier_c1_g3 = Movie(play="scenes/nier/nier_c1_g3.webm", loop=True)
image nier_c1_g4 = Movie(play="scenes/nier/nier_c1_g4.webm", loop=True)
image nier_c1_g11 = Movie(play="scenes/nier/nier_c1_g11.webm", loop=True)
image nier_c1_g13 = Movie(play="scenes/nier/nier_c1_g13.webm", loop=True)
image nier_c1_g14 = Movie(play="scenes/nier/nier_c1_g14.webm", loop=True)
image nier_c1_g15 = Movie(play="scenes/nier/nier_c1_g15.webm", loop=True)
image nier_c1_g16 = Movie(play="scenes/nier/nier_c1_g16.webm", loop=False)




label nier_chapterSelect:
    $ clear_screen()
    menu:
        "Chapter 1 - Recon Mission[ ' - Completed' if nier_chapter1_done else '' ]":
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
    dev "{size=40}{color=#d33d3d}WARNING{/color}: If you are sensitive to static, beeping and such. Consider lowering \"Sound\" volume."
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
    play Effects_one "audio/effects/radio1.mp3" noloop volume 1.2
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
    char.player "{think} If it were Command... they would not have told her to retreat."
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
    char.player "No more..."
    "You turn toward the exit. Preparations are already underway."
    "Supplies, tools, whatever she might need. There is nothing more to wait for. You head out for the rendezvous point."
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
                    play Effects_one "audio/effects/camera_flash.mp3" noloop
                    scene nier_c1_spotted with dissolve
                    "You move too early."
                    "The scanning beam snaps back toward the alley."
                    "Your timing was off and you were spotted by the drone."
                    npc.drone "Irregular signal detected. Classification: hostile. Commencing elimination."
                    char.player "F-fuck!"
                    play Effects_one "audio/effects/laser_single.mp3" noloop
                    jump nier_gameover

                "Leave immediately after the first unit finishes scanning":
                    "You steady yourself at the edge of the alley."
                    "The first scan passes."
                    scene nier_c1_b4_4 with dissolve
                    pass

                "Wait until the second unit comes":
                    play Effects_one "audio/effects/camera_flash.mp3" noloop
                    scene nier_c1_spotted with dissolve
                    "You moved too late."
                    "The patrol cycle resets and another scan sweeps the alley."
                    "Your delay costs you the opening."
                    npc.drone "Irregular signal detected. Classification: hostile. Commencing elimination."
                    char.player "Shit—!"
                    play Effects_one "audio/effects/laser_single.mp3" noloop
                    jump nier_gameover


            menu:
                "What do you wait for?"
                "Move as soon as the first unit turns away":
                    play Effects_one "audio/effects/camera_flash.mp3" noloop
                    scene nier_c1_spotted with dissolve
                    "You step out too soon."
                    "Another unit catches you as you step out of the alley."
                    "Your movement is immediately detected."
                    npc.drone "Irregular signal detected. Classification: hostile. Commencing elimination."
                    char.player "N-no—!"
                    play Effects_one "audio/effects/laser_single.mp3" noloop
                    jump nier_gameover

                "Move between patrol units":
                    play Effects_one "audio/effects/camera_flash.mp3" noloop
                    scene nier_c1_spotted with dissolve
                    "You misjudge the spacing."
                    "Two scans converge on the alley at once."
                    "There's nowhere to hide."
                    npc.drone "Irregular signal detected. Classification: hostile. Commencing elimination."
                    char.player "Damn it!"
                    play Effects_one "audio/effects/laser_single.mp3" noloop
                    jump nier_gameover

                "Move after the second unit passes":
                    "The second drone glides past the alley without scanning."
                    "The entrance clears."
                    pass
            menu:
                "Which direction do you go?"
                "Turn right":
                    scene nier_c1_b4_5 with dissolve
                    "You turn right immediately."
                    "A third drone pivots towards you, activating it's sensor mid rotation."
                    scene nier_c1_b4_6 with dissolve
                    play Effects_one "audio/effects/dodge.mp3" noloop
                    "The scan sweeps the area in front of it."
                    "You stay low, pressing yourself down as the beam passes just overhead."
                    char.player "{think}Clear. That was too close..."
                    char.player "{think}I need to move fast. Before more units converge."
                    $ stop_allsound()
                    jump nier_c1_safehouse

                "Go left":
                    play Effects_one "audio/effects/camera_flash.mp3" noloop
                    scene nier_c1_spotted with dissolve
                    "You turn left, back toward the path you just cleared."
                    "A scan sweeps the area behind you."
                    "You step directly back into its range."
                    npc.drone "Irregular signal detected. Classification: hostile. Commencing elimination."
                    char.player "—!"
                    play Effects_one "audio/effects/laser_single.mp3" noloop
                    jump nier_gameover

                "Go forward":
                    play Effects_one "audio/effects/camera_flash.mp3" noloop
                    scene nier_c1_spotted with dissolve
                    "You move forward into the street."
                    "A third drone approaches from the opposite direction."
                    "Its sensor beam sweeps across your path mid-step."
                    npc.drone "Irregular signal detected. Classification: hostile. Commencing elimination."
                    char.player "Shit—!"
                    play Effects_one "audio/effects/laser_single.mp3" noloop
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
            # dev "I got bored and made some encouragement."
            jump nier_gameover


label nier_c1_safehouse:
    scene black with fade
    "After narrowingly escaping the patrol units, their presence beings to thin."
    "Only one or two drones remain active along your route to the safehouse."
    "An older memory surfaces as you close in on the entrance."
    scene nier_c1_flashback1 with dissolve
    play Ambience_one "audio/ambience/mystery_ambience.mp3" loop volume 0.8 fadein 1.0
    "The command room is brightly lit."
    "Terminals display a ruined sector map."
    play Effects_one "audio/effects/radio1.mp3" noloop volume 1.5
    "A data node blinks near the center."
    npc.command "This operation is a simple retrieval mission."
    npc.command "A machine server unit has been identified in the target zone."
    npc.command "Stored data is believed to be intact. You will secure the data and return."
    scene nier_c1_flashback4 with dissolve
    char.player "What about enemy presence?"
    npc.command "Limited."
    npc.command "Machine forces will be diverted."
    npc.command "A separate unit will draw attention from the sector to create an opening."
    char.player "{think}An opening..."
    npc.command "YoRHa No.2 Type B will infiltrate the zone."
    npc.command "She will secure access to the server."
    npc.command "Her Operator will provide overwatch and extraction."
    play Effects_one "audio/effects/radio2.mp3" noloop volume 1.5
    "2B's route highlights on the display."
    scene nier_c1_flashback3 with dissolve
    char.nier "Understood. I will proceed once the diversion begins."
    scene nier_c1_flashback5 with dissolve
    char.player "If the diversion holds."
    char.player "What about enemy backup forces?"
    npc.command "Backup response is projected to be limited."
    char.player "Projected from incomplete scans."
    char.player "What about units outside the sensor range?"
    npc.command "No additional forces have been detected."
    char.player "Detected does not mean absent."
    scene nier_c1_flashback3 with dissolve
    char.nier "Command. If unaccounted units appear I will respond."
    char.player "{think}2B?!"
    npc.command "Enemy presence remains within acceptable parameters."
    npc.command "Proceed according to assignment."
    "The terminal display flickers."
    play Effects_one "audio/effects/radio_static.mp3" noloop volume 1.5
    "The command feed cuts abruptly."
    scene nier_c1_flashback2 with dissolve
    "Only mission data remains on the screen."
    char.player "{think}Of course. Never the full scope with them."
    char.nier "Mission parameters received."
    char.nier "We should prepare to deploy."
    scene nier_c1_flashback5 with dissolve
    char.player "I was expecting more detail."
    char.nier "The objective is clear."
    char.player "The objective is, the path to it isn't."
    char.nier "Uncertainty is expected on missions."
    char.player "That's true, But risk is one thing. Blind risk is another."
    char.nier "Command believes the risk is acceptable."
    char.player "Command isn't the one walking into it."
    char.nier "Neither are you alone."
    scene nier_c1_flashback6 with dissolve
    char.player "I know."
    char.player "That's exactly why I'm worried."
    char.nier "I will not act recklessly enough to affect you, Operator."
    char.player "You don't think you do."
    scene nier_c1_flashback7 with dissolve
    char.nier "..."
    char.nier "I will adjust if conditions change. I will get ready for deployment."
    scene nier_c1_flashback8 with dissolve
    "2B turns and moves toward the exit. Her footsteps fade into the corridor."
    char.player "{think}It's not me I'm worried about..."
    scene black with fade
    "After a short moment to collect your thoughts, you head out to prepare for deployment."
    $ stop_allsound()
    
    scene nier_c1_c1 with dissolve
    play Ambience_one "audio/ambience/underground_ambience.mp3" loop volume 0.8 fadein 1.0
    "You stop in front of the bunker door. The metal surface is cold."
    char.player "{think}What \"simple retrieval mission\"? That enemy base had an army waiting."
    "You reach for the valve and turn it slowly"
    "It resists under your grip but still moves slightly as metal grinds against metal."
    scene nier_c1_c2 with dissolve
    char.player "{think}Did the diversion even work...?"
    "You turn the valve again as the resistance lessens."
    scene nier_c1_c3 with dissolve
    char.player "{think}That was a suicide mission, had 2B pushed further..."
    "You tighten your grip and turn the valve one last time."
    scene nier_c1_c1 with dissolve
    char.player "{think}That should be open. Given how tight the valve was, 2B probably isn't here yet."
    char.player "*Quietly* I hope she's safe."
    "You step back and pull the door open but-"
    play Effects_one "audio/effects/camera_flash.mp3" noloop
    scene nier_c1_c4 with dissolve
    "A sharp beam washes over your back."
    npc.drone "Unregistered unit detected."
    npc.drone "Engaging."
    char.player "{think}-!"
    scene nier_c1_c5 with dissolve
    play Effects_one "audio/effects/body_fall.mp3" noloop
    "You turn to face the drone but lose your footing and fall back against the bunker door you just opened."
    char.player "{think}This isn't funny...! Shit! What do I do?!"
    char.player "{think}Think. {size=35}Think!{/size} {size=45}Think!!!{/size}"
    play Effects_one "audio/effects/charged_laser.mp3" noloop
    scene nier_c1_c6 with dissolve
    "The drone's core flares as it prepares to fire."
    "But before it can-"
    play Effects_one "audio/effects/sword_slash.mp3" noloop
    scene nier_c1_c7 with dissolve
    "A flash of steel cuts through the drone mid-charge."
    "The charging sound cuts off instantly."
    scene nier_c1_c8 with dissolve
    play Effects_one "audio/effects/crash.mp3" noloop
    "The drone collapses to the ground."
    "The drone drops at your feet, smoke spilling from it, and behind it stands 2B with her blade still raised."
    char.player "?!"
    "You remain against the bunker door as the drone lies motionless at your feet."
    scene nier_c1_c9 with dissolve
    "2B lowers her blade and the weapon locks back into place."
    "She stands behind the fallen machine, calm as if nothing unusual happened."
    char.nier "Are you unharmed?"  
    char.player "I'm fine. Thanks to you." 
    scene nier_c1_c10 with dissolve
    "You push yourself upright, eyes still on the fallen drone."
    char.player "That was closer than I expected. I couldn't even hear it because of the valve."
    scene nier_c1_c11 with dissolve
    "2B's gaze lingers on the machine for a moment."
    char.nier "The patrol density was higher than projected."
    char.nier "I was pursued for a while. It took time to break contact."
    char.player "{think}That explains why I got here before her. They funneled the pressure onto her route."
    scene nier_c1_c12 with dissolve
    menu:
        nier2bmenu "Thankfully the location was nearby for me. Who set the location to here?"
        "{color=#d33d3d}[char.player]{/color}: Command did.":
            char.player "Command selected it."
            scene nier_c1_c13 with dissolve
            "2B studies you for a moment."
            char.nier "That is unusual."
            char.nier "Command typically prioritizes operational safety over individual units."
            char.player "{think}...She knows that's not the full truth."
            char.nier "Regardless, we are both here. Let's move inside."
            $ stop_allsound()

        "{color=#d33d3d}[char.player]{/color} I did.":
            $ nier_lovepoints += 10
            char.player "I set it closer to your extraction path."
            char.player "If things went wrong, you needed somewhere you could reach fast."
            scene nier_c1_c13 with dissolve
            "2B turns to look at you."
            char.nier "That placed it closer to the enemy perimeter."
            char.player "Yeah."
            char.player "But distance favors whoever's being hunted."
            char.player "Shorter route means less time exposed."
            char.player "Especially when a certain someone pushes herself past optimal limits."
            char.nier "..."
            scene nier_c1_c12 with dissolve
            "She pauses, considering it."
            scene nier_c1_c14 with dissolve
            char.nier "You... altered the rendezvous location?"
            char.player "I did."
            char.nier "You acted without authorization."
            char.player "I know."
            char.nier "That decision compromised your operational safety."
            char.player "It did."
            char.player "{think}As long as she made it here alive, the risk was worth it."
            scene nier_c1_c15 with dissolve
            "A brief silence settles between you as she looks away with her arms cross, processing what you just said."
            char.nier "..."
            char.nier "I do not understand."
            scene nier_c1_c12 with dissolve
            char.nier "You increased your own exposure."
            char.nier "That was not required for mission success."
            char.player "{think}She doesn't sound upset. She just... doesn't see why."
            char.nier "Such decisions are... inefficient and illogical for the mission."
            "Her voice trails off slightly, trying to understand your dangerous decision."
            char.player "Maybe. But missions aren't the only thing that matters."
            scene nier_c1_c16 with dissolve
            char.player "I hope it makes sense to you someday."
            char.player "But right now, you need maintenance."
            scene black with fade
            "You turn away first."
            "2B remains where she is, still processing."
            char.nier "..."
            play Effects_one "audio/effects/footstep_short.mp3" noloop volume 2
            queue Effects_one "audio/effects/footstep_short.mp3" noloop volume 1.5
            "Then, after a moment, you hear her footsteps follow."
            $ stop_allsound()

        "{color=#d33d3d}[char.player]{/color} I'm not sure.":
            char.nier "Noted. Let's hurry in."
            char.player "Right."
            $ stop_allsound()

    scene nier_c1_d1 with dissolve
    play Ambience_one "audio/ambience/thinking_ambience.mp3" loop fadein 1.0
    "The safehouse lights activate as you enter. Dust settles slowly, disturbed by your movement."
    "2B steps inside after you, briefly scanning the interior as the door seals shut behind her."
    "For a moment, neither of you speaks."
    scene nier_c1_d2 with dissolve
    "You move toward the console while she remains near the entrance."
    "She tries to straighten her posture, but the damage is evident."
    scene nier_c1_d3 with dissolve
    "You glance back at her."
    char.player "Sit."
    "The word comes out sharper than you intend."
    char.player "{think}Why did I say that so harshly?"
    char.player "{think}Wait... I think I already know the answer."
    "Her gaze meets yours, calm and unwavering."
    char.nier "My condition does not prohibit continued standing."
    "You exhale quietly."
    menu:
        "What do you say?"
        "{color=#d33d3d}[char.player]{/color}: Just sit.":
            $ nier_lovepoints += 5
            char.player "Diagnostics will be faster this way."
            char.nier "Affirmative."

        "{color=#d33d3d}[char.player]{/color}: Sit. That's an order.":
            $ nier_lovepoints -= 0
            char.nier "..."
            char.nier "Command received."

        "{color=#d33d3d}[char.player]{/color}: Please relax while I run diagnosis.":
            $ nier_lovepoints += 10
            char.player "I'll handle the rest, just comfortably rest."
            char.nier "Compliance confirmed."

    scene nier_c1_d4 with dissolve
    "She follows the order, lowering herself onto one of the beds as you continue toward the terminal."
    play Effects_one "audio/effects/wood_creak.mp3" noloop
    "You hear a soft creak behind you as she adjusts her posture."
    scene nier_c1_d5 with dissolve
    "You bring up the local diagnostics on the terminal."
    "Most values stabilize as expected except one."
    scene nier_c1_d6 with dissolve
    npc.terminal "Thermal dispersion efficiency remains below nominal."
    npc.terminal "Core temperature continues to climb. 88.0... 88.4..."
    char.player "{think}Her temperature is still rising."
    scene nier_c1_d7 with dissolve
    "You watch the values tick upward on the display. 88.6... 88.9..."
    char.player "{think}Combat load has already ended."
    char.player "{think}Her body should be venting heat, not accumulating it."
    char.player "{think}So why is it not dispersing."
    "Noticing the shift in your posture, 2B turns her head toward you."
    scene nier_c1_d8 with dissolve
    char.nier "Operator."
    scene nier_c1_d9 with dissolve
    char.nier "{size=15}Is there an issue?"
    "Too focused in reading, you didn't notice 2B calling for you."
    "You scan deeper into the diagnostic layers."
    scene nier_c1_d10 with dissolve
    char.player "{think}If it keeps rising, it will become dangerous."
    npc.terminal "Thermal output response delayed."
    npc.terminal "Multiple subsystems report acute strain."
    scene nier_c1_d11 with dissolve
    "You pull up the mission timeline."
    "Her diagnostic graph spikes sharply."
    "The rise begins well before you ordered her to retreat."
    char.player "{think}This is it."
    char.player "{think}She overexerted herself during that exchange."
    char.player "{think}Her systems are overloaded and cannot regulate properly."
    char.player "{think}So the heat is not being expelled."
    scene nier_c1_d12 with dissolve
    "Your expression tightens."
    "Behind you, there is a faint shift of movement."
    scene nier_c1_d13 with dissolve
    char.nier "Operator. Requesting status update."
    "You finally look away from the terminal."
    menu:
        "What do you say?"
        "{color=#d33d3d}[char.player]{/color}: Wait, give me a moment.":
            $ nier_lovepoints +5 
            char.player "I'm still reviewing the data."
            char.nier "Understood."

        "{color=#d33d3d}[char.player]{/color}: You shouldn't have pushed yourself.":
            $ nier_lovepoints += 10
            char.player "Your systems are under a lot strain."
            char.player "Standby for further details."
            char.nier "Acknowledged."

        "{color=#d33d3d}[char.player]{/color}: Not now, 2B!":
            $ nier_lovepoints -= 0
            char.player "I need to concentrate."
            char.nier "...Understood."

    scene nier_c1_d14 with dissolve
    "She lowers her gaze, posture still and compliant."
    scene nier_c1_d15 with dissolve
    char.player "{think}If it keeps rising, her condition will worsen."
    char.player "{think}I need to intervene."
    char.player "{think}But how...?"
    scene nier_c1_d16 with dissolve
    "You step away from the terminal and approach her, thinking of every possible solution that would help."
    char.player "{think}Automatic regulation is compromised."
    char.player "{think}Her body right now doesn't have the facilities to self-repair, therefore..."
    scene nier_c1_d17 with dissolve
    char.player "{think}Manual control might still be possible. However..."
    scene nier_c1_d18 with dissolve
    "You stop and kneel in front of her."
    char.player "2B, listen to me."
    char.player "You overexerted yourself during the last engagement."
    char.player "Your systems are strained and cannot regulate thermal output properly."
    "She looks down at you, expression neutral but attentive."
    char.player "The heat is building because your control feedback is delayed."
    char.player "Left alone, it will continue to rise."
    scene nier_c1_d19 with dissolve
    char.nier "No abnormal sensation detected. Requesting confirmation of operational risks."
    char.player "Your sensory feedback is lagging behind internal conditions."
    char.player "You will not feel the change until it reaches a critical threshold."
    char.player "By then, you will be unable to operate."
    scene nier_c1_d20 with dissolve
    "All of the sudden she averts your gaze and goes silent, still processing."
    scene nier_c1_d21 with dissolve
    char.nier "Understood. What action do you recommend."
    char.player "You are still synchronized to my command authority at close range."
    char.player "As a field operator, I can issue priority inputs directly to your control layer."
    scene nier_c1_d22 with dissolve
    "She watches you closely as you stand up."
    char.player "It is an emergency function."
    char.player "Normally it is never used outside of Command supervision."
    char.nier "Clarify how this applies to my current condition."
    char.player "Your systems cannot stabilize themselves."
    char.player "Through direct synchronization, I can act as an external reference."
    char.player "This will allow your control layer to reroute and disperse the excess heat safely."
    scene nier_c1_d23 with dissolve
    "You pause briefly, then continue."
    char.nier "There are no records of this procedure within available databases."
    char.nier "This configuration is uncommon."
    char.player "That is because it is not standard."
    scene nier_c1_d24 with dissolve
    char.player "I am one of a small number of Field Operators assigned under a classified trial."
    char.player "Command is still experimenting with the role."
    char.player "That is why there are no records available."
    "She remains still for a moment, eyes unfocused as internal calculations run."
    char.nier "You disclosed classified information. Command would not approve."
    menu:
        "What do you say?"
        "{color=#d33d3d}[char.player]{/color}: Command has already been informed. (Lie)":
            scene nier_c1_d23 with dissolve
            $ nier_lovepoints -= 5
            char.player "They have given permission to proceed with the treatment."
            char.nier "That's... unusual."
            char.player "Let's not waste any more time."
            
        "{color=#d33d3d}[char.player]{/color}: I am prioritizing your safety":
            scene nier_c1_d23 with dissolve
            $ nier_lovepoints += 5
            char.player "I know. But this procedure depends on trust and compliance."
            char.player "Consequences from Command doesn't matter right now."
            char.nier "I... don't follow."
            char.player "Just trust me for now okay?"
            char.nier "Understood, Operator."

        "{color=#d33d3d}[char.player]{/color}: There isn't time for approval.":
            scene nier_c1_d23 with dissolve
            char.player "It's an emergency situation, I am making that call."
            char.nier "Understood."
    
    scene nier_c1_d25 with dissolve
    char.nier "Contiuation, please clarify the requirement."
    char.player "The affected pathways require direct access."
    char.player "Any barrier will interfere with proper heat transfer."
    scene nier_c1_d26 with dissolve
    "You gesture briefly, indicating the necessary areas without touching yet."
    scene nier_c1_d27 with dissolve
    "She follows the motion, then looks back to you."
    scene nier_c1_d26 with dissolve
    char.nier "Confirm. Is removal of required layers really necessary to proceed?"
    char.player "It is necessary for the procedure to be done without risk."
    "She does not respond immediately."
    scene nier_c1_d27 with dissolve
    "Her gaze lowers slightly, unfocused, internal diagnostics running in silence."
    "A moment passes longer than strictly required."
    scene nier_c1_d26 with dissolve
    char.nier "Risk assessment updated."
    "She looks back to you."
    char.nier "Probability of successful stabilization increases with compliance."
    char.nier "Perform the procedure, Operator."
    char.player "{think}She came to terms with it faster than I thought she would..."
    char.player "Good. Now do you want me to or-"
    scene nier_c1_e1 with dissolve
    "Before you can finish the sentence, 2B rises from the bed without further hesitation."
    char.player "-?"
    scene nier_c1_e2 with dissolve
    play Effects_one "audio/effects/clothes_drop.mp3" noloop volume 2
    "She swiftly removes her dress as you indicated, setting them aside neatly."
    char.player "{think}What the-?!"
    scene nier_c1_e3 with dissolve
    "Once finished, she looks at you for confirmation."
    "Her body stands in front of you. Nothing but her panties left."
    char.player "{think}T-Thats... What is this feeling...?"
    "You can't help but stare at her body. Something you've never seen before."
    "A new sensation forms within you as you look at..."
    scene nier_c1_e4 with dissolve
    "Her breasts..."
    scene nier_c1_e5 with dissolve
    "Her slender waist and the hands covering her panties."
    char.nier "Proper procedure prepared. Awaiting guidance, Operator."
    char.player "H-huh. Oh..."
    scene nier_c1_e6 with dissolve
    "As 2B prepares herself for treatment, you snap back to reality and begin telling her what to do."
    char.player "O-okay. Lay down on the bed face up, and try not to move."
    scene nier_c1_e7 with dissolve
    "At your direction, she lies back on the bed, positioning herself flat on her back."
    char.player "Alright... let's begin."

    scene nier_c1_f1 with dissolve
    "You sit beside the bed, forcing yourself to focus despite the unfamiliar sight before you."
    "She lies still, exposed and silent, posture composed but unmistakably vulnerable."
    char.player "{think}I've never seen this defenseless before."
    scene nier_c1_f2 with dissolve
    "You hesitate, hands hovering for a brief moment before settling carefully against her breasts."
    char.player "{think}I'm trying to focus on the task, but... why is my heart beating this fast?"
    "Noticing your hesitation, 2B turns to look at you with a confused look."
    scene nier_c1_f3 with dissolve
    char.nier "Operator... Your vital indicators show irregularity. Is there an issue?"
    char.player "N-no... I am just... nervous. This is a first for me too. {think}Focus! 2B's life is on the line here."
    scene nier_c1_f2 with dissolve
    char.nier "Understood. If my cooperation is insufficient, please advise."
    char.player "Just stay still as much as possible. It will be easier to direct."
    "With uncertainty, you finally begin."
    scene nier_c1_f4 with dissolve
    "The heat beneath your touch is immediate and concentrated, far warmer than expected, a clear sign of the strain her systems are under."
    char.nier "N-ngh-?"
    "2B lets out a soft sound as you firmly grab her body"
    char.player "{think}Wow... I never expected them to be this sof- No!"
    char.player "{think}Focus. So... this is where majority of the heat is trapped."
    char.player "I'm going to guide it outward. Stay relaxed and don't resist."
    scene nier_c1_f5 with dissolve
    char.nier "A-acknowledged."
    scene nier_c1_f6 with dissolve
    "You begin to move your hands slowly away from her center, applying gentle, even pressure, not forcing the heat but encouraging it to follow your motion."
    char.player "{think}Slow... Careful."
    "A faint tension passes through her body, subtle but present, though she makes no sound and does not pull away."
    char.nier "Internal temperature variance detected."
    scene nier_c1_f7 with dissolve
    char.player "Good, it's responding well."
    scene nier_c1_f8 with dissolve
    "You reposition, one hand steady at her chest while the other guides along her body, the warmth lessening at her core."
    scene nier_c1_f9 with dissolve
    char.nier "kgh- Arh- O-operator..."
    char.player "Remain still. Minor discomfort is within boundaries."
    char.nier "Mmfg- U-un... Understood... Ng-"
    char.player "It's nearly over... hang in there for a little longer."
    "Again. You start to get a feeling you haven't felt before. Your pulse accelerates, your face turning red."
    char.player "{think}W-what is happening...? The more I touch her... and hearing her make these sounds..."
    char.nier "T-thermal load decreasing, sta-... stability improving."
    "You gradually ease the pressure, keeping your hands in place a moment longer to ensure the balance holds."
    scene nier_c1_f8 with dissolve
    char.player "You're stabilizing. Almost done."
    char.nier "Core temperature returning to nominal range. Synchronization remains active."
    scene nier_c1_f10 with dissolve
    "You finally lift your hands away, the unnatural warmth fading."
    char.player "{think}It worked."
    char.player "Remain at rest. Your systems will finish compensating on their own."
    scene nier_c1_f11 with dissolve
    char.nier "Understood. ...Thank you, Operator."
    scene nier_c1_f10 with dissolve
    "The room falls quiet again, the crisis passed. For now."
    char.player "{think}It's finally over... She'll stabilize by herself."
    char.player "{think}Hopefully next time I can stop her before it gets this serious."
    if nier_lovepoints < 20:
        jump nier_failedRoute
    char.nier "Operator."
    "Her voice breaks the silence, calm, but subtly different from before."
    char.player "Yes? {think}She sounds different. Still recovering... or something else."
    char.nier "I am reviewing your recent actions. You repositioned the safehouse closer to my operational zone and delayed reporting to Command."
    "Remaining still as her systems continue to recover, she continues."
    char.nier "You have also violated Command protocol by performing this procedure on me."
    char.nier "I do not understand."
    char.player "Like I said before, I hoped you'd understand eventu-"
    "She cuts you off."
    char.nier "Clarification requested. These actions increase risk to you."
    char.nier "YoRHa doctrine does not prioritize individual units."
    scene nier_c1_f12 with dissolve
    "She slowly sits upright, eyes lifting to meet yours. Her breast sways as she moves."
    char.nier "Why do you... care for me?"
    char.player "{think}The fact that she's asking me outright... it means she's slowly changing too."
    char.player "...Before I answer that, I need to ask you something."
    char.nier "...What is it?"
    char.player "Are you sure you want to know?"
    char.player "The answer isn't logical. It might not make sense to you. It's also not something Command would approve of."
    char.player "Once I say it, you can't unhear it."
    scene nier_c1_f13 with dissolve
    char.nier "..."
    scene nier_c1_f12 with dissolve
    char.nier "I am requesting clarification because I do not understand your behavior."
    char.nier "If understanding requires non-operational context, I will accept it."
    char.nier "That uncertainty is... bothering me."
    char.player "{think}Wow..."
    scene nier_c1_f14 with dissolve
    char.nier "If this will explain it... then I want to hear it."
    char.player "Alright, I understand."
    "You compose yourself before starting to explain."
    scene nier_c1_f15 with dissolve
    "She turn towards you, waiting to listen attentively. You catch glimpses of her single clothing as she turns."
    char.player "I'm sure the reason is shorter and simpler than you imagined"
    char.player "I care about you, and I don't want you to die."
    char.nier "..."
    scene nier_c1_f16 with dissolve
    char.nier "YoRHa units can be resotred through data uploads."
    char.nier "Please clarify."
    char.player "If you fall before a full upload, what comes back isn't you."
    char.player "It's a version missing everything since the last sync."
    scene nier_c1_f17 with dissolve
    "2B falls silent"
    char.player "Your decisions. Your damage. This moment. Everything gets lost, forever."
    scene nier_c1_f16 with dissolve
    char.nier "That is within acceptable operational parame-"
    scene nier_c1_f18 with dissolve
    char.player "Not to me."
    char.player "That isn't you. That's a version Command is satisfied with."
    char.player "An endless soldier that keeps going."
    char.player "But are you even truly alive at that point? Or just another Unit?"
    scene nier_c1_f19 with dissolve
    char.nier "I... understand that now, but..."
    char.nier "...why me?"
    char.nier "Why did you choose to intervene for this unit specifically?"
    scene nier_c1_f20 with dissolve
    char.player "{think}I knew this was coming."
    char.player "I didn't choose you. Not at first."
    scene nier_c1_f21 with dissolve
    char.nier "Requesting more information."
    char.player "Listen, I've worked with a lot of units."
    char.player "Different models. Different assignments."
    char.player "Some followed orders perfectly. Some pushed past their limits because they thought they were supposed to."
    scene nier_c1_f19 with dissolve
    char.nier "And the outcome?"
    char.player "{think}She probably already knows the answer."
    char.player "At the end of a mission, there is always another one. No matter how damaged you are."
    char.player "However... There wasn't always another unit for that mission"
    scene nier_c1_f22 with dissolve
    "Her face shifts down, realizing what you are implying."
    char.nier "..."
    char.player "Eventually, they were all gone."
    scene nier_c1_f23 with dissolve
    char.nier "What about you?"
    char.player "I've never been reset, nor have I died."
    char.player "But I've watched it happen enough times to recognize the signs."
    "A brief silence follows, heavier than the words that came before."
    scene nier_c1_f24 with dissolve
    char.player "2B, you're the longest-standing unit I've worked with."
    char.player "You've pushed past your limits more times than I can count."
    char.nier "...I am still operational."
    char.player "Exactly. At some point, I got attached."
    char.player "You're the only unit who's been there from the start."
    scene nier_c1_f25 with dissolve
    "She doesn't respond right away, gaze shifting slightly as the words settle."
    char.player "I don't want to lose you when it could've been prevented."
    char.nier "Operator... I understand your point now."
    char.nier "This perspective is... unfamiliar."
    char.nier "But it does not feel... incorrect."
    char.player "{think}That's more than I expected."
    char.player "You don't have to resolve it now, nor I want you to agree with my philosophy."
    char.player "Your systems are still stabilizing."
    char.player "Get some rest. We'll talk later."
    scene nier_c1_f24 with dissolve
    char.nier "...Understood."

    if nier_lovepoints >= 35:
        scene nier_c1_f27 with dissolve
        "Before her head hits the pillow. 2B's sensors activated at once, her head turning toward you."
        char.nier "Operator, your biometric readings are irregular. Heart rate elevated to 118 beats per minute."
        char.nier "Pulse at 105, and body temperature climbing. The changes localize to the lower area."
        scene nier_c1_f28 with dissolve
        "Her voice cut through as she descends from the bed, her boots clicking softly."
        scene nier_c1_f29 with dissolve
        char.player "I'm okay, 2B. Probably just relieved that you're okay."
        scene nier_c1_f30 with dissolve
        "Your eyes clicked to her chest before darting away, the sight of her nipples only worsening the throb in your pants."
        char.player "{think}What the hell is this?!"
        "Unnoticed to you, the bulge grew more pronounced, your cock fully erect."
        scene nier_c1_f31 with dissolve
        char.nier "Negative, Operator. I detect further escalation."
        scene nier_c1_f32 with dissolve
        "2B closed the distance, causing you to drop onto the bed."
        scene nier_c1_f33 with dissolve
        "She kneels before you as her breasts hung forward brushing her arms."
        char.nier "Do you require assistance?"
        "Your hand instinctively cover your lap."
        char.player "-?! N-no, it's... I don't know what's wrong. It just started after looking at you."
        scene nier_c1_f34 with dissolve
        char.nier "Accessing archived data... Male physiology, pre-collapse records."
        "A brief pause follows as 2B stares blankly at you."
        char.nier "Analysis complete. This response indicates sexual arousal."
        char.nier "To alleviate, stimulation must lead to climax, involving ejaculation from the penis."
        scene nier_c1_f35 with dissolve
        "Your eyes widened at her words."
        char.player "S-sexual... what? 2B, are you serious?"
        scene nier_c1_f36 with dissolve
        "You trailed off as she reached for your shorts, yanking it off firmly."
        char.nier "YoRHa protocol mandates support for operator well-being."
        char.player "Yes but, surely that doesn't mean pre-collapse methods."
        char.nier "You also helped me with irregular methods. Database dictates that, if not taken care of, it will not go away."
        scene nier_c1_f37 with dissolve
        play Effects_one "audio/effects/clothes_drop.mp3" noloop
        "Her fingers worked efficiently, tugging your pants open and freeing your rigid cock."
        char.nier "Selecting available options..."
        char.nier "\"Titjob\" procedure selected from database. Enveloping the penis between breasts for friction-based stimulation."
        char.player "Wait, tit- oh god..."
        scene nier_c1_f38 with dissolve
        "You gripped her shoulders as she leaned in, cupping her breasts and pressing them around your cock."
        "The warm, soft flesh molded to you, squeezing your cock tightly."
        char.player "2B, this is... fuck, that's incredible."
        scene nier_c1_g2 with dissolve
        "She begins sliding her tits up and down, coating her skin with your leaking fluids."
        char.nier "Vocal response positive. Continuing."
        "Her blindfold concealed her face, but her body moved with precision, nipples dragging along your shaft on each pass."
        "You groaned, hips twitching upwards."
        char.player "It- ah... it feels so tight... and warm."
        char.player "It's sucking me in. K-keep going, please don't stop."
        char.nier "Affirmative. Increasing pressure."
        scene nier_c1_g3 with dissolve
        "2B compressed her breasts harder, her arms flexing to heighten the grip."
        char.player "{think}Her boobs are covering my cock... it feels go good. I hope this goes on forever."
        "The head of your cock ermerged from her cleavage with every upward stroke, only to vanish again."
        char.nier "Heart rate increased. Blood circulation changed. Ejaculation imminent?"
        char.player "Yes- shit, yes, 2B. Something... something is building up."
        "Your voice cracked, thighs tensing, and your hands grabbing the bedsheets as you thrust shallowly into her tits."
        char.player "{think}F-fuck-! I can't stop myself from making noises... She's increasing her speed even more!"
        scene nier_c1_g4 with dissolve
        char.nier "Change in temperature detected. Proceeding to completion."
        "She quickened the pace, milking your cock with relentless squeezes."
        char.player "Fuck, som-something's c-coming!"
        char.player "...I can feel it-!"
        char.nier "Do not hold back, Operator. Everything is within expectations. Please proceed to ejaculation."
        char.nier "C-c-"
        "As if given permission. Your cum surged suddenly as you cry out"   
        scene nier_c1_g5 with dissolve
        "Ropes of semen shot from the tip, painting her cheek and dripping between from her lips in hot spurts."
        scene nier_c1_g6 with dissolve
        "2B held steady, easing her grip as your spasms faded. She rose, semen trailing down her chest."
        scene nier_c1_g7 with dissolve
        char.nier "Orgasms achieved. Mission support fulfilled. Operator vitals sta-..."
        scene nier_c1_g8 with dissolve
        "She pauses. Your cum still dripping from her face."
        char.player "?"
        scene nier_c1_g9 with dissolve
        char.nier "Operator. Your vitals are not stabalizing. Re-checking database..."
        char.player "{think}That felt so good... I didn't know sensations like those existed."
        char.nier "Completed. It seems you still require more assistence, please lie down. I will conduct the next step."
        char.player "{think}There's a next step?! Fuck..."
        char.player "U-understood... I'll leave it up to you..."
        char.nier "Affirmative."
        scene nier_c1_g10 with dissolve
        "2B slides off her last piece of clothing as she straddles you swiftly, facing away, her pale ass cheeks parting as she positioned herself over your hips."
        "Her voluptuous ass staring at you. Her pussy exposed for you to see."
        char.nier "Begining intercourse. Data shown this is the most effective method for calming down an erection. Shall I proceed?"
        char.player "Fuck yes... please do."
        char.nier "Achknowledge."
        scene nier_c1_g12 with dissolve
        "The tip of your cock slowly goes inside her as she accepts your request."
        char.nier "Nngh- I-insertion complete..."
        char.player "{think}Shi-it! Th-this sensation..."
        scene nier_c1_g11 with dissolve
        "She leaned forward slightly, bracing her hands on your thighs, and started riding you."
        "Her ass bounced with each descent, cheeks flexing and spreading."
        scene nier_c1_g13 with dissolve
        char.player "This- ah- feels even b-better... Your ass is perfect, so tight around me."
        "You thrust up to meet her, fingers digging into the softness of her ass."
        char.player "H-harder 2B. Ride me harder..."
        char.nier "Affirmative. Ad-adjusting pace for increase intensity."
        scene nier_c1_g14 with dissolve
        "She accelerated, slamming down with percision, her pussy gripping and releasing your cock in waves."
        "Wet slaps echoed in the bay as her as ripples from the impacts."
        char.nier "Vitals u-updating, arousal peaking again."
        char.player "D-don't stop- I'm gonna cum again soon! It's like your pussy is sucking me dry...!"
        "Your balls tightened, the pressure building up yet again as you watch her ass grind against you."
        char.nier "Ejaculation detected as imminent. C-continuing to facilitate climax."
        scene nier_c1_g15 with dissolve
        "2B ground down harder as you bucked wildly crying out."
        char.player "I-I feel it again! 2B, yes- cumming inside you!"
        "She circles her hips to rub her inner walls against your cock, her ass cheeks pressing flush against you on every thrust."
        char.nier "Operator, you can shoot it out inside this Unit."
        char.player "F-"
        "Hearing her words..."
        scene nier_c1_g16 with dissolve
        "Thick spurts of cum flooded her depths, her pussy contracting to draw it all in."
        scene nier_c1_g17 with dissolve
        "Your legs shake as you both climax together. Your cum slowly drips down on your cock."
        scene nier_c1_g18 with dissolve
        "As she gets off, semen trickled from her pussy down her thighs."
        char.nier "Operator... You r-released so much... "
        char.nier "Second orgasm achieved. Vitals stabilizing at baseline. Mission support complete."
        char.player "*Panting heavily* That was... incredible. I've never felt anything like that..."
        char.nier "Likewise, Operator. I also felt... different."
        scene black with fade
        char.player "{think}That is a good sign, I really hope we that do that again..."
        "She gets off you and sets by the bedside."
        scene nier_c1_g19 with dissolve
        char.nier "Thank you for always looking out for me, Operator. I will be more careful in the future."
        char.player "I'll continue to do so. Don't die on me 2B..."
        char.nier "Achknowledge... that means I might forget... about this..."
        char.player "T-that too... I err..."
        char.player "I hope I can count on you again the next time this... err... happens."
        scene nier_c1_g20 with dissolve
        "2B looks away with a small blush."
        char.nier "A-affirmative... Operator."
        char.nier "This unit requests to go clean up and rest until stable."
        char.player "You don't have to ask me for that, 2B. Go ahead."
        char.nier "Thank you, Operator."
        char.player "{think}It's subtle, but I can see she's slowly changing. She's showing a bit more emotion than her usual self."
        char.player "{think}I hope it stays that way..."
        $ nier_chapter1_done = True
        $ nier_cardHover = "UI/nier_cardSelect2.png"
        scene black with fade
        $ nier_lovepoints = 0
        dev "You have finished Chapter 1 of 2B's story! I hope you enjoyed this, her story will continue in another update!"
        jump codex_charSelection

        

    else:
        jump nier_failedRoute



    


label nier_failedRoute:
    scene black with fade
    "She lies back, eyes closing, the tension in her posture gradually easing as the room settles into quiet once more."
    "You spend time looking after 2B as her system starts to reconfigure."
    dev "Hmm... maybe you went wrong somewhere? How about you try other dialogue options."
    $ nier_lovepoints = 0
    jump codex_charSelection

#===========================================================================================================================
# Start of Chapter 2
#===========================================================================================================================