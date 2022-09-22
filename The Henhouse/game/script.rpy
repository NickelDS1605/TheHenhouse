﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define omni = Character("Unknown")
define bella = Character("Bella")
define ed = Character("Edward")
define brooke = Character("Brooke")
define andy = Character("Andy")
define isha = Character("Isha")
define me = Character("Self")
define q = Character("???")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # This is the introduction.

    #input for name
    $ player_name = renpy.input("What is your name?")
    #removes extra spaces
    $ player_name = player_name.strip()

    omni "It's finally time, %(player_name)s!"

    omni "Today, you are moving into your new home."

    omni "Aren't you excited??"


    omni "Here is the map to your house, good luck!"

    #Personal dialog as you walk along to the shops
    

    #Isha shows up
    #show isha worry

    #think this
    "What a strange woman"
    "Perhaps we could help her?"

    #outloud
    me "Ma'am are you alright?"

    #isha responds
    q "I'm so sorry I didn't see you there!!"
    #show isha cry

    me "Hey hey it's ok"
    me "What's wrong miss?"

    q "My store is supposed to open this week but my delivery of bird seed still isnt here"
    q "If I don't get it in the next two days, I'm never going to get this shop open."
    #cries for a little bit
    q "wait"
    q "I'm being very rude sorry"
    #show isha smile
    q "Apologies for my outburst, my name is Isha Woodcock."

    #internal dialogue bc that was random
    "That was... certainly unexpected"
    #respond !!
    me "Hello Isha, it's very nice to meet you."
    isha "We don't get many strangers around these parts, what are you doing around here?"

    me "Well I'm %(player_name)s, and I just moved here."
    me "I'm trying to find my house, but I don't know how to read the map"
    me "Can you help?"

    #show map
    isha "Oh why of course! Let me see it."
    isha "Ah I see! This is simple. All you have to do is walk down the xœìÝÏëäÌ¬ð¶ó° and head towards _ˆ×f ‡Ë°‡Å Ø]"

    me "Uhhhhhhhhhhhhhhhhhhhhhhhhhhh"
    #insert font change + scene change
    omni "run"
    #abrupt scene change again to forest/town path

    "What just happened?"
    #insert a look look maybe?
    "How did I get here?"
    "There's something strange about this place..."
    #choice here!!!
    menu: 
        "What should I do?"

        "Try to leave":
            #will either leave it as this
            #or add an error screen and make people rollback maybe?
            #i like this as an error screen, will go back and change later(i have note in google doc)
            jump errorleave

        "Follow map":
            "If I get to the town I might be able to find people who can help me."
    
    label errorleave:
        #insert scene change
        omni "Go back"
        jump nextchoice

    label nextchoice:
        #back to prev scene
        menu:
            "What should I do?"

            "Try to leave":
                jump errorleave

            "Follow map":
                "If I get to the town I might be able to find people who can help me."

    #another scene change obvi
    #just keep walking just keep walking
    #pause
    #two vamps show up in distance
    "Hmm..."
    "Maybe they can help me?"

    #walk towards em
    "He-Hello?"
    #they turn towards you
    bella "Omg hi!! Are you the new resident we've heard so much about??"

    me "I believe so... how did you hear about me?"

    bella "Oh word gets around fast in these small towns, %(player_name)s"

    ed "Darling."

    bella "Of course!! How could we be so rude. I'm Bella Swan and this is my fiance, Edward Spurling."
    bella "We're so excited to finally meet you!"

    #suspicious vamp ed
    # edward "What brings you to this town?"

    #choice here!!
    $ sus = True
    menu: 
        ed "What brings you to this town?"

        "I'm not quite sure yet":
            #suspicious glance
            ed "Are you supposed to be here?"
            me "Uhm"
            $ sus = True
            

        "I got a job here!":
            ed "People typically don't just \"get\" jobs around here."
            $ sus = True
            

        "Run away":
            $ sus = False

    if sus:
        "im not sure yettttt"


    
    
    # This ends the game.
    return