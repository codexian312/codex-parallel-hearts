#===========================================================================================================================
# Furina variables
#===========================================================================================================================
default furina_lovepoints = 0
default furina_c1_order = 0
# {color=#d33d3d}[char.player]{/color}

#===========================================================================================================================
# Furina Video variables
#===========================================================================================================================
image furina_demo = Movie(play="scenes/furina/furina_demo.webm")






#===========================================================================================================================
# Start of Chapter 1
#===========================================================================================================================
label furina_chapter1:
    $ clear_screen()
    stop BGM_one
    play BGM_one "audio/bgm/cafe_music1.mp3" loop

    scene furina_chapter1_1 with fade
    char.player "{think}Furina had mentioned that this cafe's cakes were supposed to be exceptional.{/think}"
    char.player "{think}That alone was enough to convince her to drag me along to try them together.{/think}"
    "Unfortunately, you ended up arriving a little later than planned."
    "From a distance, it was easy to spot her. Arms cross, stiffed posture and her legs tapping impatiently against the ground"
    char.player "{think}...I'm only a few minutes late, but I can already tell she is not happy.{/think}"

    "You walk closer, and she spots you immediately."

    scene furina_chapter1_2 with dissolve
    char.player "H-hey Fur-"
    "Before you could finish greeting her, she snaps at you"
    char.furina "Finally! Do you have any idea how long I've been waiting for you?"
    char.furina "Honestly, what kind of gentleman makes a lady wait this long?"
    char.player "I didn't mean to keep you waiting. My train had some delays"
    char.player "{think}Ahh... I'm late by a few minutes and she's really letting me have it.{/think}"
    scene furina_chapter1_3 with dissolve
    char.furina "You should know better than to leave a lady standing out here all by herself."
    char.furina "Especially when there's cake involved, and I've been looking forward to it all week!"
    menu:
        "What should I say?"
        "{color=#ff0000}[char.player]{/color}: I-I'm really sorry, Furina.":
            $ furina_lovepoints += 5
            char.player "{think}Better be honest and just apologise... I hope she forgives me quickly before she really starts getting more annoyed{/think}"
            char.furina "Hmph... I suppose I can let it slide this time. Just barely."
            char.furina "You're lucky I'm in a good mood today... especially since you're only a few minutes late."
            char.player "Yes yes... I'm sorry I was late. It wo-"
            "Before you can continue, she interrupts you sharply."
            scene furina_chapter1_3_2
            char.furina "But! Next time we meet, you better be on tim— No, make that earlier than me!"
            char.player "{think}At least she forgave me quick enough, I'm glad I apologised straightaway...{/think}"
            char.player "Alright, alright... I promise to do that next time."
            char.furina "Good... now, shall we head inside before we waste any more time standing out here?"
            char.furina "I am dying to sample the cakes... I've been looking forward to this all week!"
            char.player "Lead the way, Furina."

        "{color=#ff0000}[char.player]{/color}: Heh, you don't look nearly as mad as you sound.":
            $ furina_lovepoints += 10
            # play Effects_one "audio/effects/correct.mp3" noloop
            char.player "{think}She looks so annoyed... but maybe she's not actually mad?{/think}"
            char.furina "{bi}Hmph!{/bi} I-I'm not... not mad! D-Don't get the wrong idea!" 
            scene furina_chapter1_3_1 with dissolve
            char.furina "{i}...B-but... I was looking forward to this, you know...{/i}"
            char.player "{think}Yeah, I thought as much. She's not unreasonable enough to get mad over a few minutes{/think}"
            char.player "{think}Her cheeks are definitely red... she was actually excited to see me.{/think}"
            char.player "I knew it, you were just pretending to be mad. I can see that little blush, you know."
            char.furina "Hey! That doesn't change the fact that you were a little late!"
            char.player "Alright, alright... I guess I {b}was{/b} a little late."
            char.player "Well, I'm finally here. How about we just go inside before we waste more time bickering?"
            scene furina_chapter1_3_2 with dissolve
            char.furina "Hmph... fine, you're lucky I'm in a good mood today."
            char.furina "I am dying to sample the cakes... I've been looking forward to this all week!"
            char.player "That makes me happy to hear, let's enjoy the day together."

        "{color=#ff0000}[char.player]{/color}: Relax, Furina. A few minutes isn't going to ruin the day.":
            $ furina_lovepoints -= 5
            char.player "{think}I hope she doesn't hold a grudge... she looks like she could snap any second.{/think}"
            char.furina "Relax? Standing here like a statue while I waited? You really have no shame!"
            char.furina "Do you even understand what it feels like to be kept waiting?!" 
            char.player "I'm only a few minutes late, it's not that big of a deal you think?"
            scene furina_chapter1_3_3 with dissolve
            char.furina "Not a big de- Hmph! Fine! I suppose I can forgive you this once."
            char.player "Alright, alright... let's head inside before we both get more worked up. Everyone is looking at us"
            scene furina_chapter1_3_4 with dissolve
            char.furina "{size=12}He didn't have to be so mean about it... I was super excited to see him...{/size}"
            char.player "What did you say?"
            scene furina_chapter1_3_3 with dissolve
            char.furina "{size=40}I said you better not make me wait like that again!{/size}"
            char.player "Wh-whoa! No need to scream at me, I got it..."
            scene furina_chapter1_3_4 with dissolve
            char.furina "Hmph..."

    scene black with fade
    "Furina pushes the door open first, the small bell above jingles as she steps inside"
    play Effects_one "audio/effects/shop_bell.mp3" noloop
    scene furina_chapter1_4_1 with dissolve
    char.player "{think}There she goes... leading the way, like always. She's always in such a hurry for things like this{/think}"
    "Following her, you step into the warm interior, the rich scent of baked goods and brewed coffee wrapping around you."  
    char.player "{think}This smells amazing... I can see why she was excited to drag me here.{/think}"
    "Furina scans the cafe for the best spot, checking every seat in the cafe."  
    scene furina_chapter1_4_2 with dissolve
    pause
    scene furina_chapter1_4_3 with dissolve
    pause
    scene furina_chapter1_4_4 with dissolve
    "After a careful inspection, she finally settles on a table in the middle where the sunlight hits just right."
    scene furina_chapter1_5_1 with dissolve
    scene furina_chapter1_5_2 with dissolve
    scene furina_chapter1_5_1 with dissolve
    scene furina_chapter1_5_2 with dissolve
    "She waves at you energetically, signaling for you to come over."
    char.player "Alright, alright I'm coming over now"
    scene furina_chapter1_5_3 with dissolve
    char.player "{think}Furina and I have been friends for a while now... not dating or anything, just really good friends.{/think}"
    scene furina_chapter1_5_4 with dissolve
    char.player "{think}She's always full of energy and a little bratty, but that's just how she is.{/think}"
    scene furina_chapter1_5_5 with dissolve
    char.player "{think}She came across this cafe on {bi}Pixagram{/bi} and she insisted that I come along to try it out. Well... more like demanded{/think}"
    "Sliding into the seat across from her, you can already feel the warmth of the sunlight hitting the table and the faint scent of freshly baked pastries filling the air." 
    scene furina_chapter1_6_1 with dissolve
    char.furina "Mmm... it smells so nice in here! I can already tell this place is going to be amazing."
    char.player "Yeah, the aroma of fresh pastries and rich coffee is really something."
    char.player "{think}The cafe feels cozy and warm, and the smell alone is already making my stomach growl.{/think}"  
    char.player "So? What was so important that you dragged me out here with you? Surely it wasn't just for the atmosphere, right?" 
    "Furina opens her eyes wide and points dramatically at you, a small smirk tugging at her lips."
    scene furina_chapter1_6_2 with dissolve
    char.furina "Their {bi}Chocolate Cake!{/bi} Of course! The best cake in the entire cafe!"  
    char.furina "I've been craving it all week! You better be ready to enjoy it with me!"  
    char.player "Isn't this your first time here? How do you know it's the best thing on their menu?"
    char.player "{think}Although her excitement is contagious... it's impossible not to smile at her antics.{/think}"  
    scene furina_chapter1_6_3 with dissolve
    char.furina "Just because it's my first time doesn't mean I can't have great taste!"
    char.player "{think}Her cheeks and red and puffy again, she's embarassed but trying to sound confident. How typical of her, always a little dramatic.{/think}"
    char.furina "I saw the pictures online... everyone raves about it. And I trust my instincts more than some random reviews!" 
    char.player "*Chuckles* How can you say you trust your instincts more than reviews but says everyone raves about it hahaha." 
    char.furina "Hmph! I'll have you know, I can multitask! Trusting my instincts {b}and{/b} knowing what's popular, thank you very much!"  
    "You burst out laughing even more at the contradictions in her words."  
    char.player "Pfft hahaha... how does that even make sense?"  
    "Furina looks away, her cheeks faintly pink, clearly embarrassed but trying not to show it."  
    scene furina_chapter1_6_4 with dissolve
    char.furina "{bi}W-Whatever!!{/bi} Making fun out of me, I won't take you out to other amazing places you know!"  
    char.player "{think}She's so easy to tease.{/think}"  
    char.furina "You'd better be careful, [char.player]..."  
    char.player "Alright, alright... don't get too worked up, I'm just joking!"  
    char.player "If you say it's the best, I'll take your word for it. How about I go and order for us?"
    char.player "{think}She really does take this stuff seriously. And she's so adorable when she's worked up about it.{/think}"  
    scene furina_chapter1_6_5 with dissolve
    char.furina "That's what I love to hear! You're finally getting excited about this too!"  
    char.player "Your excitement must've been rubbing off on me."  
    char.furina "Of course! I always make everything more interesting!"
    char.player "I can see that... you've got me looking forward to this chocolate cake more than I thought I would."  
    char.furina "Good! Now you'll appreciate it properly when it arrives!"  
    char.player "What do you want with it? Coffee? Tea? Any special request?"
    char.furina "I'll take a {bi}Creamy Latte, lots of milk, hold the sugar!"
    char.player "Alright, sit tight. I'll be right back"
    "You stand up from the table, giving Furina one last glance before heading toward the counter."  
    scene furina_chapter1_7_1 with dissolve
    "As you approach, the scent of freshly brewed coffee grows stronger, mixing with the sweetness of baked goods."  
    npc.staff "Hello! Welcome to Pastel Patissiere Cafe! What can I get for you?"
    char.player "Hi! I'm here for one of your chocolate cakes. My friend here has been talking about it nonstop."
    npc.staff "I'm sorry, but which one are you referring to? We have a few chocolate cakes to choose from."
    "The staff gestures toward the display case, where several chocolate cakes are neatly arranged."
    scene furina_chapter1_7_2 with dissolve
    npc.staff "We currently have our Classic Chocolate Cake, Dark Chocolate Truffle Cake, and our Triple Chocolate Mousse Cake."
    char.player "{think}Crap... I don't know what it was called, I forgot to ask as well...{/think}"
    char.player "{think}Right! Furina mentioned this place because of a recent review.{/think}"
    char.player "{think}Everyone was talking about one specific cake...{/think}"
    char.player "I heard there was a lot of praise going around for one of your chocolate cakes recently. That's what we came here for."
    npc.staff "Ah, yes! That would be our new addtion, the Triple Chocolate Mousse Cake."
    "As the staff finishes speaking, your gaze drifts back toward the display case."
    scene furina_chapter1_7_3 with dissolve
    char.player "{think}That should be it... right? I'm pretty sure this is the one she mentioned.{/think}"
    char.player "I'll have that then, please."
    npc.staff "Understood. And would you like anything to drink with that?"
    char.player "Yes, I'll have..."

    menu:
        "Tea or Coffee"

        "Coffee":
            $ furina_c1_order += 1
            menu:
                npc.staff "What type of coffee would you like?"
                "Espresso":
                    pass
                "Cappuccino":
                    pass
                "Latte":
                    $ furina_c1_order += 1
                    pass
                "Macchiato":
                    pass
                
            menu:
                npc.staff "How much milk would you like?"
                "No milk":
                    pass
                "Regular":
                    pass
                "Lots of milk":
                    $ furina_c1_order += 1
                    pass

            menu:
                npc.staff "How much sugar would you like?"
                "No sugar":
                    $ furina_c1_order += 1
                    pass
                "One spoon":
                    pass
                "Two spoons":
                    pass   

        "Tea":
            menu:
                npc.staff "What type of tea would you like?"
                "Black tea":
                    pass
                "Chamomile tea":
                    pass
                "Herbal tea":
                    pass
                "Darjeeling tea":
                    pass

            menu:
                npc.staff "How much milk would you like?"
                "No milk":
                    pass
                "Regular":
                    pass
                "A splash of milk":
                    pass

            menu:
                npc.staff "How much sugar would you like?"
                "No sugar":
                    pass
                "One spoon":
                    pass
                "Two spoons":
                    pass

        
    scene furina_chapter1_7_1 with dissolve
    npc.staff "Great! I'll get that prepared for you right away."
    char.player "{think}Finally, all the ordering is done. Now to wait... I hope I got the orders right.{/think}"
    npc.staff "We'll bring it over to your table shortly after. Thank you."
    char.player "Thank you."
    "Settling back into your seat, you glance around the cafe. It's mostly empty, just a few early customers scattered around."

    scene furina_chapter1_8_1 with dissolve
    char.furina "I'm so excited! I can't wait to try it!"
    char.player "Yeah, it looked amazing from the display. You really know the best spots, huh?"
    char.furina "Of course! I always find the best treats."
    char.player "Hahaha, that I can believe."
    char.player "Now that I'm settled in, seems like we got here pretty early. Look at this place, there's hardly anyone here."
    scene furina_chapter1_8_2 with dissolve
    char.furina "I know, right? Perfect timing! No long lines, no noisy crowds... just us and the sweet treats!"
    char.player "Yeah, it's actually kind of nice. Feels almost like we have the whole place to ourselves."
    char.furina "Exactly! Now we can really enjoy our orders without anyone bothering us."
    char.player "True. And it's quieter too. Makes it feel more relaxed than I expected."
    scene furina_chapter1_5_5 with dissolve
    char.furina "Mhm! This is exactly why I wanted to come early. Less chaos, more cake appreciation!"
    char.player "Yes, now I understand why you wanted me to come this early. It was worth it"
    char.player "So, while we wait, how's your week been?"
    scene furina_chapter1_8_3 with dissolve
    char.furina "Ugh, so busy... The amount of work I had to do to be free today..."  
    scene furina_chapter1_6_5 with dissolve
    char.furina "But finally! A chance to escape all the boring stuff and come here!"
    char.player "Yeah, and I get to witness your... antics up close without anyone staring."  
    scene furina_chapter1_6_2 with dissolve
    char.furina "Ha! Jealous much? You wish you had my charm, [char.player]."  
    char.player "Oh, I see... your charm is in full effect today. I should probably take notes."  
    char.furina "Pfft! As if you could keep up with me. I'm basically a walking spectacle!"  
    char.player "{think}Classic Furina. Always acting like the world revolves around her.{/think}" 
    scene furina_chapter1_6_3 with dissolve
    char.furina "Well? Aren't you going to acknowledge how fun I make everything? You should be thanking me!"  
    char.player "Fine, fine... thank you, Furina, for making this little outing infinitely more entertaining." 
    scene furina_chapter1_6_1 with dissolve
    char.furina "That's better! See? You know how to behave when I'm around. I'm proud of you." 
    char.player "{think}Now that I think about it, we've had a few of these \"outings\" already. I wonder if she thinks this is a date?{/think}"

    menu:
        char.player "Should I ask her about it?"
        "Yes":
            $ furina_lovepoints += 5
            char.player "{think}Maybe I should just ask...{/think}"
            char.player "Hey, Furina... do you think of these outings as... you know, dates?"
            "Her cheeks flare bright red as she looks away, clearly embarrassed but trying to hide it behind her hands."  
            scene furina_chapter1_9_1 with dissolve
            char.furina "W-Why would you ask something like that?!"
            char.player "Well... I've just always wondered. You're always the one to drag me out to these places."
            char.player "And we never really talked about it before. Honestly, I don't really mind either way."
            char.player "I enjoy your company and being around you is never boring."
            "Furina fidgets, tapping her foot and glancing up at you through her lashes, a mixture of defiance and flustered excitement on her face."  
            scene furina_chapter1_9_2 with dissolve
            char.furina "H-Hmph! D-Don't get the wrong idea, okay?! I'm not doing this just because... because I like spending time with you... or anything!"  
            char.furina "I-I'm just... okay with you being here, that's all!"  
            char.player "Okay okay, I got it. {think}Look at her acting all defensive, but still enjoying my company.{/think}"
            char.furina "B-but... w-what do you mean by... 'it doesn't really matter to you either way'?!"  
            char.player "Well... It's no lie I love spending time with you, that's all. If you want to think of this as a date, I don't mind at all. That's what I'm trying to say."
            "Furina freezes for a moment, her cheeks turning bright red, and she glares at you, flustered but also a little pleased." 
            scene furina_chapter1_9_3 with dissolve
            char.furina "I g-guess it can be a d-da-"
            "Before Furina could finish what she was saying, the staff interrupts her by placing the dessert and drink on your table."
        "No":
            char.player "{think}Nah... probably best not to push it.{/think}"
            "After a short wait, the staff returns carrying a tray with your dessert and drink."
            

    npc.staff "Here you go. A Triple Chocolate Mousse Cake, and your drinks. Please enjoy!"
    scene furina_chapter1_10_1 with dissolve
    char.player "Thank you!"
    "Furina's eyes widen as she leans slightly over the table, staring at the cake with pure delight."  
    char.furina "W-Wow... it looks even better than in the pictures!"  
    "She tilts her head, examining every layer, her hands clasped together as if she can't believe it's actually here."  
    scene furina_chapter1_10_2 with dissolve
    char.furina "The chocolate... the mousse... the layers! It's perfect! I'm so glad we came!"  
    char.player "{think}Wow... she really goes all out when it comes to chocolate, doesn't she?{/think}"
    char.player "It does look incredible. I can see why you were so excited to come here."
    char.player "{think}I'm glad this was the right one{/think}"
    "Furina grab holds of the coffee and takes a sip"  
    scene furina_chapter1_10_3 with dissolve
    "Furina grabs the coffee, lifting it carefully to her lips. She takes a small sip, her eyes narrowing as she tastes it." 
    if furina_c1_order == 4:
        scene furina_chapter1_10_yes with dissolve
        char.furina "Hm... Not bad... actually, this is perfect! {bi}Just the way I like it!{/bi}" 
        "She sets the cup down with a satisfied smirk, happily sipping away."
        char.player "{think}Looks like I got the order just right... well done, me.{/think}"
        char.furina "See? I knew you could handle it! Don't get used to me being impressed this easily, though."
        char.player "I'll take the praise where I can get it."
        char.furina "*Chuckles* Don't get ahead of yourself now."
         
    else:
        scene furina_chapter1_10_no with dissolve
        char.furina "{bi}[char.player]?!{/bi} This isn't what I asked for!"
        $ furina_lovepoints -= 5
        "She sets the cup down with a frown, crossing her arms and glaring at you, clearly displeased."
        char.player "{think}Oops... looks like I messed up the order.{/think}"
        char.furina "Hmph! I can't believe you got it wrong... You better pay more attention next time!"

    scene furina_chapter1_11_1 with dissolve
    char.furina "Let's try the cake, I hope it's as good as people said it was!"
    "Furina carefully picks up a fork, leaning over slightly as she eyes the Triple Chocolate Mousse. Her eyes sparkle with anticipation."  
    char.furina "Okay... here goes nothing."
    scene black with fade
    "She takes her first bite, chewing slowly as if savoring every flavor. Her eyes widen, and a delighted gasp escapes her."  
    scene furina_chapter1_11_2 with dissolve
    char.furina "Let's try the cake, I hope it's as good as people said it was!"  
    char.furina "{i}Mmm! W-wow... this is incredible! Just as good as everyone said!{/i}"  
    char.player "{think}She's really enjoying it. Her excitement makes it impossible not to smile.{/think}"  
    char.player "Looks like it was worth coming here, huh?"  
    char.furina "Of course! I told you, I know the best treats! Hmph! You better savor yours properly too!"  
    "Furina leans back, crossing her arms but still sneaking bites with a grin, clearly savoring the moment."  
    scene furina_chapter1_11_3 with dissolve
    char.furina "*Excitedly* Well?! What do you think of it?!"
    char.player "Mmm... the mousse is so rich and velvety... the texture of the cake is perfect with delicate flavors. Even though it's sweet it's not all that sweet, it's just... right."
    char.furina "I told you I know the best treats!"
    char.player "You're right... seeing you this excited makes it even better."
    char.furina "You better savor yours properly too! I'm not sharing mine if you eat it carelessly!"
    char.player "Don't worry... I'm enjoying it just as much as you are."
    char.furina "I wouldn't have it any other way!"
    char.player "The layers are balanced perfectly, and the chocolate isn't overwhelming. I can definitely see why people rave about this place."
    scene furina_chapter1_11_1 with dissolve
    char.furina "W-Wait... you actually notice all that?! You're taking this cake seriously... I didn't think you had it in you!"
    char.player "Of course... you've dragged me around enough to train my taste buds by now."  
    char.furina "Hmph! I guess you {b}can{/b} appreciate a good cake after all... Don't get too proud of yourself though! I'm still the expert here, got it?!"
    char.player "Hahaha... alright alright"
    scene black with fade
    "Both of you keep enjoying the cake, laughing and teasing each other with each bite. Furina comments on the small details of the mousse and playfully mocks you if you miss anything."  
    "Time flies. The last crumbs of mousse are gone, coffee cups are empty, and the warm morning sun spreads across the table. You both lean back, feeling satisfied, and laugh softly at each other's jokes."
    scene furina_chapter1_6_1 with dissolve
    char.furina "Whew... I suppose that's enough sugar for one morning."  
    char.player "Yeah, I agree. That cake was really good, I'd definitely come here again with you."  
    scene furina_chapter1_6_3 with dissolve
    char.furina "Who said I would be inviting you again?!"
    char.furina "...though, I most likely will"
    char.player "Hahaha I know that, I would never say no to you."
    char.furina "*Blushing* I think about time we get moving... this place is starting to get crowded, and I don't want our perfect little morning ruined!"
    char.player "Right behind you. Let's go before it gets too busy."  

    scene furina_chapter1_end1 with fade
    "Walking together toward the bus station, the conversation drifts lazily between small things, laughter, and work."
    char.player "So... what's your plan after this?" 

    if furina_lovepoints >= 15:
        scene furina_chapter1_end2 with dissolve
        char.furina "I was thinking I could ask you something... but I'm not sure if I should..."  
        char.player "{think}She seems hesitant... did something happen...? Wait. Did {bi}I{/bi} do something?"  
        char.furina "N-nothing! Forget it! It's not important!" 
        char.player "Are you sure? You seem... unsure. If there's anything I did, you can tell me, you know" 
        scene furina_chapter1_end3 with dissolve
        char.furina "I w-was just thinking... about what you said earlier in the cafe..."
        char.player "{think}Which part is she talking about?{/think}"  
        char.furina "A-about not minding if... we thought of this as a date."  
        char.player "{think}Ah... so that's what she's hesitating about. I guess she's more conscious of it now that I mentioned it{/think}"  
        char.player "Should I not have said that earlier? I'm sorry if I made you uncomfortable."
        char.player "I meant it though. If you want to think of this as a date, I don't mind at all."  
        scene furina_chapter1_end4 with dissolve
        "Furina stiffens, her cheeks heating up, and she crosses her arms, huffing loudly."  
        char.furina "H-Hey! Don't jump to conclusions! It's not like I hate the idea or anything...!"
        char.player "I'm not jumping to anything. I just wanted to be honest."
        char.player "I like being with you. That's all."
        char.furina "R-really...? You don't find me a-annoying?"
        "She tries to sound casual, but her voice wavers just slightly."
        char.player "Not even close."
        char.player "You're loud, dramatic, stubborn... but that's part of what makes you you."
        char.player "Things feel more vivid when you're around. Besides, why would I let you drag me to places if I didn't enjoy being with you."
        scene furina_chapter1_end5 with dissolve
        "Furina looks away quickly, pressing her lips together."
        char.player "{think}She really does worry about how she comes acros, huh? Who would've known...{/think}"
        char.furina "I always thought you just put up with me... I-if that's the case..."
        char.furina "I mean...-"
        char.player "{think}Does she really have to be this nervous, I'm on edge listening to her too.{/think}"
        char.furina "It'd be a waste for us to part ways now, right? And it's still midday..."
        char.furina "So if you're not busy or anything..."
        scene furina_chapter1_end6 with dissolve
        "She peeks at you from the corner of her eye, cheeks faintly flushed, her shoulders slightly tense as if bracing herself."
        "For a brief moment, she looks almost nervous, like she's afraid of what your answer might be."
        char.furina "I could stay with you a bit longer. Not because I'm attached to you or anything!"
        char.player "{think}She makes it sound casual, but I can tell it took her a lot just to say that.{/think}"
        char.player "{think}Maybe I'll suggest this now and see how she reacts... hopefully it won't be too much{/think}"
        char.player "How about we go back to my place for a bit?"
        char.player "If you want to, that is."
        scene furina_chapter1_end7 with dissolve
        "Furina freezes, her eyes widening just a little."
        char.furina "Y-your place...?"
        char.furina "I mean... it's not like I have a problem with it or anything!"
        char.furina "I've just never been there before, that's all..."
        scene furina_chapter1_end8 with dissolve
        "She shifts her weight from one foot to the other, debating with herself."
        char.furina "Not that I'm nervous! Obviously!"
        "A brief silence follows, broken only by the distant sounds of the street."
        char.player "{think}She didn't say no...{/think}"
        char.player "Alright, it's settled then. Let's get going before it gets too late."
        scene furina_chapter1_end7 with dissolve
        char.furina "W-wha? U-um..um... O-okay...!"
        jump furina_demoContent

        
        #demo jumps straight to house
        #real jumps to train for 1.5

    else:
        scene furina_chapter1_end9 with dissolve
        char.furina "I think I'll just head home... it's been a long morning, and I'm feeling a little tired. Thanks for coming along, though!"  
        char.player "Of course! I had a really good time, Furina." 
        scene furina_chapter1_end10 with dissolve 
        char.furina "Hmph! Don't think this means I'm going to ask you out all the time... but yeah, it was nice. I'll see you another time."
        char.player "{think}You've always asked me every time you want to go somewhere though haha, not that I should mention it."
        char.player "Alright, see you next time."  
        scene furina_chapter1_end11 with dissolve
        "She gives a small smile, a faint blush on her cheeks, and you walk together the rest of the way to the bus station."
        "After a brief goodbye, she boards her bus, leaving you with a warm, lingering feeling from the morning spent together."
        jump end_demo
    


#===========================================================================================================================
# Demo content tease
#===========================================================================================================================

label furina_demoContent:

    scene furina_demo loop with fade
    char.player "A-are you sure you're ready for this, Furina...?"
    char.player "It's not too late to back out you know"
    char.furina "W-who do you think I-I am... I'm fine... I want this."
    char.furina "{sc=3}You can p-put it in..."
    "Furina's voice wavered, trembling slightly as she looked down towards your erected cock."
    "She fidgeted, biting her lips, and whispered"
    char.furina "{sc=3} s-slowly...okay...?"
    char.player "Alright, Furina... here I go."
    jump end_demo
    $ renpy.run(ShowMenu("save"))
    return














      
    