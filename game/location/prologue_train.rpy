#===========================================================================================================================
# Video variables
#===========================================================================================================================
image train_ride = Movie(play="scenes/train/train_ride.webm")

#===========================================================================================================================
# Prologue train ride
#===========================================================================================================================
label prologue_train:
    scene train_ride loop with fade
    stop Ambience_one
    you "{think}I hate leaving work at this time, especially on Friday. The train is always so crowded{/think}"
    you "{think}Luckily I managed to get a seat this time{/think}"
    pause
