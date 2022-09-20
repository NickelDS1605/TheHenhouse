# The script of the game goes in this file.

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

    omni "Today, you are moving into your new home"

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
    q "I'm so sorry I didn't see you there"
    #show isha cry

    me "Hey hey it's ok"
    me "What's wrong miss?"

    q "My store is supposed to open this week but my delivery of bird seed still isnt here"
    q "If I don't get it in the next two days, I'm never going to get this shop open."
    #cries for a little bit
    q "wait"
    q "I'm being very rude sorry"
    #show isha smile
    q "My apologies for my outburst, my name is Isha Woodcock."

    #internal dialogue bc that was random
    "That was... certainly unexpected"
    #respond !!
    me "Hello Isha, it's very nice to meet you."
    q "We don't get many strangers around these parts, what are you doing around here?"

    me "Well I'm %(player_name)s, and I just moved here."
    me "I'm trying to find my house, but I don't know how to read the map"
    me "Can you help?"

    #show map
    q "Oh why of course! All you have to do is walk down the xœìÝÏëäÌ¬ð¶ó° and head towards _ˆ×f ‡Ë°‡Å Ø]"

    me "Uhhhhhhhhhhhhhhhhhhhhhhhhhhh"
    #insert font change
    omni "run"
    #abrupt scene change or possible run montage
    
    # This ends the game.

    return