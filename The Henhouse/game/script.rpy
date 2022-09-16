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

    omni "It's finally time!"

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

    # This ends the game.

    return