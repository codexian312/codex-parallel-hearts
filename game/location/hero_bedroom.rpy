

label hero_bedroom:
    scene hero_bedroom_1 with fade
    play BGM_one "audio/bgm/bedroom_bgm.mp3" loop
    window hide

    "The familiar scent of home greets you as soon as you close the door behind you. The distant noises of the city feel far away now."
    "Dropping your bag on the floor, you kick off your shoes and feel the tension of the week slowly leave your shoulders."
    you "{think}Finally, no emails, no meetings, no deadlines. Just me, some snacks, and my new game.{/think}"
    you "{think}And it's Friday... I've got the whole weekend to get lost in this.{/think}"
    "You set your bag down and head to the bathroom. The warm water in the shower eases the stiffness from the long week, washing away the fatigue along with the day's stress."
    scene hero_shower_1 with fade
    "Steam fills the small space, fogging the mirror slightly, and for a few quiet minutes, you just let yourself relax."
    scene hero_shower_2 with fade
    "Feeling refreshed, you towel off and change into something comfortable."
    scene hero_bedroom_1 with fade
    you "{think}Alright... ready to finally dive into [Codex].{/think}"
    you "I hope it lives up to the hype... everyone's been talking about it so much. I just hope it's not overrated..."
    show screen object_computer
    pause

