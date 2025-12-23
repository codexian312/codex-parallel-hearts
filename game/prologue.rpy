#===========================================================================================================================
# Video variables
#===========================================================================================================================
image train_ride = Movie(play="scenes/train/train_ride.webm", loop=True)

#===========================================================================================================================
# Prologue
#===========================================================================================================================



label prologue_1:
    $ clear_screen()
    scene prologue_office_1 with fade 
    play Ambience_one "audio/ambience/office_groove.mp3" loop
    "The office was quiet this late in the day. The light from the screens flickered faintly, reflecting off the polished desks."
    "The soft clicks of keyboards filled the room, with the air conditioning vents running steadily followed by the printer occasionally in the distance."
    you "{think}Almost time to clock out... It's been one of those long, endless days.{/think}"
    you "{think}Just a few more tasks, and then freedom... {/think}"
    "You lean back on your chair, stretching your shoulders against the stiffness of hours spent staring at spreadsheets" 
    "Even the printer seemed exhausted, grinding out one more copy of an endless report."
    scene prologue_office_2 with dissolve
    char.randomOne "Hey! Don't forget to send me that report before you leave."
    you "Yeah, it's almost done. I'll send it to you soon"
    scene prologue_office_3 with dissolve
    you "{think} That's Isabella... she's my closest colleague. We started this job around the same time.{/think}"
    you "{think}Over the past few years we've become the kind of coworkers who share laughs, small office jokes and coffee breaks together.{/think}"
    scene prologue_office_4 with dissolve
    char.bella "Ugh... These reports keep getting longer every week, I swear..."
    char.bella "Thank god it's Friday, feels like I've been staring at spreadsheets forever."
    scene prologue_office_1 with dissolve 
    "A yawn escapes before you even notice. Your back aches from sitting so long, and your mind drifts toward the evening ahead."
    char.bella "Well, you're almost free so hang in there a little longer."
    you "Yeah... can't wait to go home"
    scene prologue_office_2 with dissolve
    "She gives a small smile, and it's enough to make the long day feel lighter"
    char.bella "So, do you have anything planned for the weekend?"
    you "Not much, just planning to relax after a long week. Maybe finally try that new game everyone's been talking about."
    char.bella "Oh? Which one? There are so many hyped games coming out lately."
    you "Uhh... I don't remember the full name, but it was something like '[Codex]', I think?"
    you "It's advertised as a real-life sim visual novel, where you get to experience the world firsthand."
    scene prologue_office_5 with dissolve
    char.bella "Ah, [Codexp], right? I've been looking forward to trying it too."
    you "Yeah, everyone's been talking about it nonstop, especially how the characters feel so alive."
    you "Hold on... you actually know about [Codex]? I thought it was the kind of game mostly meant for a male audience."
    scene prologue_office_2 with dissolve
    char.bella "Of course I know it! I've been curious too. It's not like I live under a rock, so I figured I'd see what the hype is about."
    you "{think}I didn't expect her to actually know about it, let alone willing to try.{/think}"
    char.bella "Though... I have to admit, it does feel kind of targeted. I mean, the sexual content is pretty obvious, and I don't think there's a single male character you can pursue."
    you "Yeah, true... it's definitely aimed that way. I'm surprised you're even willing to give it a try though."
    scene prologue_office_4 with dissolve
    char.bella "From what I've heard, the stories and character interactions are supposed to be really engaging. I love a good read!"
    "She smirks, and for a moment the stress of the day fades a little."
    scene prologue_office_1 with dissolve
    you "{think}She really does make these long office hours more bearable... {/think}"
    you "I've been looking forward to it all week, can't wait to dive in tonight."
    you "I'll text you about it when I get the chance"
    scene prologue_office_6 with dissolve
    char.bella "You're not... going to be playing it for two days straight... are you?"
    char.bella "Just don't get too hooked too fast, I'd hate to see you turning into a zombie by Monday"
    you "*Chuckles* Don't worry, I'll pace myself. Probably..."
    scene prologue_office_7 with dissolve
    "She laughes softly"
    "Your gaze drifts back to your monitor, quickly scanning through the last few tasks that need finishing. The soft clicks of keyboards and Isabella's laughter fills the room."
    you "{think}Almost done... just gotta send to Isabella and another to the manager...{/think}"
    scene prologue_office_1 with dissolve
    char.bella "Got your email! Let me finish this quickly then that's us done for the week."
    char.bella "I'll wrap things up quickly so you can go enjoy your evening with the game!"
    you "No rush on that, wouldn't want to piss off the higherups for malpractice do we?"
    char.bella "Haha, fair point. Don't want to get in trouble on the last day of the week."
    you "Aren't you going to try the game this weekend? Weren't you interested in it too?"
    scene prologue_office_2 with dissolve
    char.bella "That I am of course, but my sister is coming to visit this week. I'll probably be busy spending time with her to actually play though."
    you "Got it. Family time is important, can't argue with that."
    char.bella "Yeah and... I can't exactly play that kind of game with my sister around"
    you "Also can't argue with that..."
    "Both of you chuckle softly, the sound echoing in the quiet office"
    scene prologue_office_1 with dissolve
    char.bella "Alright! That's everything done for the week! Sorry to keep you waiting"
    you "Not at all, I don't mind spending time like this with you. It's one of the things I love about at work"
    scene prologue_office_blush with dissolve
    char.bella "*Smiling while blushing* Just 'one' of the many things?"
    you "{think}She's blushing, how cute{/think}"
    you "Top 3 for sure"
    char.bella "Hahaha okay okay. I should finish up and head out, I need to pick up my sister at the airport"
    scene prologue_office_2 with dissolve
    "She gives a final smile before gathering her things and heading towards the elevator"
    you "Alright, have a safe trip. Tell your sister I said hi"
    char.bella "Have a nice weekend, enjoy your game!"
    you "Thanks, Bella. you too."
    scene prologue_office_empty with dissolve
    play Effects_one "audio/effects/footstep_short.mp3" noloop volume 2
    you "{think}Finally... done for the day. Time to close up, head home, and finally see what this [Codex] is all about."

    scene train_ride with fade
    play Ambience_one "audio/ambience/train_ambience.mp3" loop
    "The train pulls out of the station, metal wheels grinding against the tracks as the cars fill with noise"
    you "{think}I hate leaving work at this time, especially on Friday. The train is always so crowded"
    you "{think}Luckily I managed to get a seat this time"
    "You lean back slightly, watching the city lights streak past the windows."
    you "{think}After a day like today, my thoughts still drift back to Bella. I'm genuinely shocked she was excited for the game."
    you "{think}I still remember the first time we met."
    you "{think}It was our first day at the company, everything felt so overwhelming. We were basically dragged around as a pair getting trained at the same time."
    stop Ambience_one fadeout 1.0

    show prologue_memory_1 with dissolve
    play Ambience_two "audio/ambience/office_groove.mp3" loop
    npc.boss "Alright everyone, if I could get your attention for a moment."
    "The chatter in the room slowly dies down as people turn toward you."
    npc.boss "We have two new members joining the team starting today."
    show prologue_memory_2 with dissolve
    "You both glance at each other, offering an awkward but reassuring smile."
    npc.boss "I expect everyone to help them settle in and show them how things work around here."
    npc.boss "Why do you not come up here and introduce yourselves."
    
    $ char.playerInput = renpy.input("Enter your name:").strip()
    
    if not char.playerInput:
        dev "No name entered. Defaulting to \"Hero\"."
        $ char.player = "Hero"
    else:
        $ char.player = char.playerInput
    $ persistent.player_name = char.player
    $ char.player = Character(char.player, color="#ff0000")

    show prologue_memory_3 with dissolve
    char.player "Uh, hello everyone. My name is [char.player]. It is nice to meet you all."
    "A few polite nods and murmurs follow."
    npc.boss "And you."
    char.bella "Hi. I am Isabella, I'm looking forward to working with all of you."
    "Her voice is calm, but you can tell she is more nervous than you are."
    show prologue_memory_4 with dissolve
    npc.boss "Good. Welcome to the team. You two will be training together for the next few weeks."
    show prologue_memory_2 with dissolve
    char.bella "*Softly* Guess we are in this together."
    char.player "*Soft chuckle* Looks like it."
    npc.boss "For now, just follow me. I will give you a quick tour and get you settled."
    "The meeting breaks up, and people slowly return to their desks."

    scene train_ride loop with fade
    stop Ambience_two fadeout 1.0
    play Ambience_one "audio/ambience/train_ambience.mp3" loop
    "The memory fades as the train rocks gently beneath you."
    char.player "{think}Hard to believe that was 2 years ago. Back then, she was just a stranger standing beside me."
    char.player "{think}We barely exchanged a few words, both of us were busy trying to learn everything together."
    char.player "{think}Somewhere along the way, those awkward introductions turned into familiar routines."
    char.player "{think}Coffee breaks that started as small talk became something I looked forward to."
    char.player "{think}Now it is hard to imagine the office without her."
    play Effects_one "audio/effects/phone_buzz.mp3" noloop
    char.player "Hm?"
    "You take your phone out and check the screen."
    show phone_ui at top with dissolve
    char.player "{think}It's a message from Bella. What does she want?"
    show bella_text_pre1 at top with dissolve
    char.player "{think}An image?"
    play Effects_one "audio/effects/screen_tap.mp3" noloop volume 4
    "You tap on the message."
    
    hide phone_ui
    hide bella_text_pre1
    show phone_bella_airport1 at top with dissolve
    char.player "{think}Looks like she made it in time. Glad she got there before the plane landed."
    char.player "{think}At least she will not be rushing."
    "You turn the phone off and slip it back into your pocket."
    play Effects_one "audio/effects/phone_lock.mp3" noloop
    hide phone_bella_airport1 with dissolve
    "The train begins to slow, the familiar announcement echoing through the car."
    char.player "{think}This is my stop."
    "You stand up as the doors slide open, stepping out with the flow of people."
    stop Ambience_one
    jump hero_bedroom
