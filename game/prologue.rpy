#===========================================================================================================================
# Prologue
#===========================================================================================================================
label prologue_1:
    scene prologue_office_1 with fade 
    play Ambience_one "audio/ambience/Office_Groove.mp3" loop
    "The office was quiet late in the day. The light from the screens flickered faintly, reflecting off the polished desks."
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
    char.bella "That I am of course, but my sister is coming to visit this week. I'll be busy catering her to spend time by myself"
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
    you "{think}Finally... done for the day. Time to close up, head home, and finally see what this [Codex] is all about."

    jump prologue_train