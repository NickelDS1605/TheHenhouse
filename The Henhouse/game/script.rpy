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

    #bella avatars
    image neutralbella = "NeutralBella.png"

    #andy avatars
    image neutralandy =  "NeutralAndy.png"
    image freakandy = "FreakOutAndy.png"

    #brooke avatars
    image neutralbrooke = "BrookeNeutral.png"

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
    $ error = False
    menu: 
        "What should I do?"

        "Try to leave":
            #will either leave it as this
            #or add an error screen and make people rollback maybe?
            #i like this as an error screen, will go back and change later(i have note in google doc)
            $ error = True
            jump errorleave

        "Follow map":
            "If I get to the town I might be able to find people who can help me."
            
            
    $ nextchoice = False
    label errorleave:
        if error:
            #insert scene change
            omni "Go back"
            $ nextchoice = True
        

    if nextchoice:
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

    bella "Oh right! How could we be so rude. I'm Bella Swan and this is my fiance, Edward Spurling."
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
    $ funny = False
    if sus:
        #bella juts in
        bella "That's no way to treat a stranger dear"
        bella "Forgive my fiance, I'm afraid we aren't very used to having company."
        bella "It's getting quite late, we'd better let you on your merry way!"
        bella "We hope to see you again %(player_name)s!"
        ed "It can be difficult to see in the dark and we wouldn't want you to get hurt."
        bella "Yes! Be sure to follow the map, and not stray from the path."
        bella "Also avoid strangers! It can be dangerous out here."
        me "Thank you for all your advice! I'll be sure to be safe."
        #scene change
        "Could they have known about Isha?"
        "Maybe they can help me figure this out"
    else:
        #scene change
        $ funny = True
        "I can't tell him I don't know"
        "He looks dangerous"
        "I have to get out of here."
        omni "Why do you want to leave?"
        omni "We haven't done anything to hurt you have we?"
        menu:
            "Should I respond?"
            
            "No, keep walking":
                omni "Please talk to me %(player_name)s, it was our hope that you would be happy here."

            "How can you say that???":
                omni "I know things can be confusing right now, but it's only because you aren't settled in yet."
                omni "I know you'll be happy once you get comfortable around here."
        me "I am not happy here, please let me go."
        omni "I'm afraid that isn't possible."
        omni "We still have so much to do."
        #scene change, reset to before
        "I can't stay here"

    
    menu:
        "Do I have any options other than follow the map?"

        "no":
            me "Guess I better follow the map then..."

    #walking walking wlking
    #following the map
    #suddenly!!!!
    #map blows away
    me "NOO!"
    "The map moves too fast for me to catch it"
    "Crap!"
    "Which way was I supposed to be going?"
    if funny:
        me "Hey!"
        me "Creepy voice guy!!"
        me "Can you help???"
        "     "
        "         "
        "      "
        "Great."
    "Okay."
    "I think the path led this way..."
    #walking
    #scene change to middle of town
    show neutralbrooke
    "Ah!"
    "She should know something."
    me "Hi, my name is %(player_name)s, I'm new in town."
    me "Can you help me find the way to my house?"
    #she shows no emotions
    q "Hi there!"
    q "How may I help you?"
    me "Err"
    me "I lost the map to my house, and was wondering if you help me find the way?"
    q "Hmm..."
    #####REMEMMEERS THIS NAME THSI IS IMPORTANt
    $ brookemarr = False
    menu:
        q "Would you mind sitting with me for a few minutes first?"

        "Sure":
            $ brookemarr = True
            # TODO: yea marriage

        "No, I need to get home.":
            $ brookemarr = False
            #show her being upset / or character thing she has no chagne on her face
            #decide later
            q "Oh..."
            q "The house is at the end of the yellow path down there."
            #she dissapears ish (?)
    hide neutralbrooke
    "Time to go find my house!"
    "I wonder how she knew where it was?"
    #walking walking walking
    #if marr = false is longer
    "Wait I never got her name!"
    "Dang it."
    #rustle rustle
    "Wh"
    "What was that"
    #oof ah fall
    show freakandy
    me "S-Sir?"
    me "Are you alright?"
    show neutralandy
    q "Oh yes thank you!"
    q "I'm afraid my rose bushes aren't agreeing with me tonight."
    # andy smiles + chuckles?
    me "Do you really think that gardening in the middle of the night is a great choice?"
    #pause
    #wowww bitch
    q "I'm sorry who are you again?"
    "Oh no"
    me "My name is %(player_name)s!"
    me "I just moved into town!"
    q "It's nice to meet you %(player_name)s! I'm Andy Finch, the town gardener."
    #CHOICE 
    $ night = False
    $ andypoints = 0
    menu:
        andy "Tending to the roses helps me communicate with them, they respond much better."

        "How fascinating! Looks like its working!":
            andy "Thank you so much!"
            andy "If you ever need someone to tend to your garden, I'd be happy to do so!"
            $ andypoints += 1
            $ night = True

        "I'm... not sure thats how that works.":
            #show him being sad now
            $ andypoints -= 1
            andy "Uh"
            andy "We all have our own opinions I'm sure."
            #dont cry dont cry dont cry
            #now show sudden smile
    andy "Oh! You must be my new neighbor! How are you getting settled in?"
    me "Actually I'm trying to find my house right now !"
    me "Do you know where it is?"
    # TODO: insert color namew of house here
    andy "Of course! You're the ## house right here."
    #move background left
    #show house
    me "OMG Thank you!"
    me "I've been traveling all day and I'm really tired so I think I better go head inside."
    if night:
        me "Goodnight Andy!"
        andy "You too %(player_name)s!"
        #dissapears into rose bushes
    else:
        andy "Goodnight."
    hide neutralandy
    
    #show front door of house
    "It looks cute"
    #show interior of houes?
    omni "Do you like it???"
    omni "We all worked hard on it."
    me ""
    me "What do you mean 'we'?"
    me "Are there more of you?"
    omni "Well I can't watch you all the time can I? I have a life you know."
    me "WHAT"
    omni "Anyways, you still haven't answered."
    # TODO: learn how to save background preferences
    $ needschanges = False
    menu:
        omni "Do you like your house?"

        "Yes":
            #keep it
            omni "Yay!"
        "No":
            #gives options for new backgrounds
            $ needschanges = True
            omni "Oh no!"

    if needschanges:
        omni "How can we help?"
        #background choices
        #menu:

    omni "I'm glad that's all settled now!"
    omni "Be sure to get a good night's sleep, we have a lot to do tomorrow."

    #show the bedroom
    menu:
        "Should I get a good night's sleep like they said?"

        "Yes":
            #fade to black nap time
            "I want to be prepared for tomorrow."
        "No":
            "Why."
            "Why would you pick this option."
            #fade to black

    ####DAY TWO BITCHESSSSSSSSSSSSSS
    ###LOOOKIE HERE
    ## INSERTING A BREAK

    #show bedroom
    #birds chirping >:)
    #walk to kitchen
    omni "Hello %(player_name)s!"
    omni "Welcome to the Henhouse!"
    omni "Although it isn't our intention to control your every move, we do have some rules and regulations in place to keep you safe."
    omni "You may only travel to TWO places each day."
    omni "There may be some of the town residents in these places, as you saw last night."
    $ question = False

    menu: 
        omni "Do you have any questions?"

        "Yes":
            omni "It's good to be prepared!"
            $ question = True
        "No":
            omni "Oh my! Good luck today!"
            
            
    
        
    label questionmenu:
        if question:
            menu:
                omni "Do you have any questions?"

                "How will I know where each resident is?":
                    omni "You won't know where the residents are unless you've played before and memorized it."
                    jump questionmenu
                    
                "Why can I only go to two places a day?":
                    omni "Because there are only so many hours in a day silly!"
                    jump questionmenu
                    
                "How many days do I have here?":
                    omni "You have six more days here, last night was your first night playing our game."
                    jump questionmenu

                "What happens after I finish the game?":
                    omni "The choices you make, such as your commentary on Andy's gardening methods last night will determine what special ending you get!"
                    jump questionmenu
                    
                "What can I do in this game?":
                    omni "You will go through each day, and sometimes you will get to make choices in your conversations."
                    omni "These choices can lead to different endings and unlock new aspects of every character you meet."
                    jump questionmenu
                    
                "How do I restart the game?":
                    omni "If you wish to restart at any point you can open the file The Henhouse is downloaded under and delete all save files in the saves folder."
                    "(HINT: If you can't find anyone each day we recommend clicking the back button and going to different places!)"
                    jump questionmenu
                
                "I have no more questions.":
                    omni "Great!"
                    omni "Let's get started."
    
    ###DAY 2 PLAYTHROUGH TIME
    $ daytwoplays = 0
    $ visitedTown = False
    $ visitedGarden = False
    $ visitedChurch = False
    $ visitedStore = False
    $ visitedShop = False
    $ visitedGrave = False
    $ visitedSchool = False
    $ visitedMemorial = False
    label daytwo:
        if daytwoplays < 2:
            menu:
                #show map
                omni "Where would you like to go today?"

                "Town Square":
                    if visitedTown:
                        omni "You've already been here"
                        jump daytwo
                    else:
                        #facing the fountain
                        $ visitedTown = True
                        $ daytwoplays += 1
                        jump daytwo
        
                "Gardens":
                    "lalalalalala"
                    if visitedGarden:
                        omni "You've already been here"
                        jump daytwo
                    else:
                        $ visitedGarden = True
                        $ daytwoplays += 1
                        jump daytwo

                "Church":
                    if visitedChurch:
                        omni "You've already been here"
                        jump daytwo
                    else:
                        $ visitedChurch = True
                        $ daytwoplays += 1
                        "We're going to meet the pastor"
                        "he's very excited to meet you"
                        "ask to officiate wedding for lucky couple?"
                        jump daytwo
        
                "Grocery Store":
                    "lallalalalaal"
                    if visitedStore:
                        omni "You've already been here"
                        jump daytwo
                    else:
                        $ visitedStore = True
                        $ daytwoplays += 1
                        jump daytwo

                "Shopping Center":
                    "lalalalalalalallala"
                    if visitedShop:
                        omni "You've already been here"
                        jump daytwo
                    else:
                        $ visitedShop = True
                        $ daytwoplays += 1
                        jump daytwo
        
                "Graveyard":
                    if visitedGrave:
                        omni "You've already been here"
                        jump daytwo
                    else:
                        "we're walking around so so much"
                        "recognize names"
                        "bird names as well????"
                        "curious"
                        $ visitedGrave = True
                        $ daytwoplays += 1
                        jump daytwo

                ##finished !!!
                "School":
                    if visitedSchool:
                        omni "You've already been here"
                        jump daytwo
                    else:
                        #show schoolroom
                        omni "You literally met zero kids yesterday."
                        omni "Why would you pick this option????"
                        $ visitedSchool = True
                        $ daytwoplays += 1
                        jump daytwo

                "Memorial":
                    if visitedMemorial:
                        "we're gunna put special info here"
                    else:
                        $ visitedMemorial = True
                        "error"
                        $ daytwoplays += 1
                        jump daytwo
    

    ###NUMBA THREEE
    $ daythreeplays = 0
    label daythree:
        $ visitedTown = False
        $ visitedGarden = False
        $ visitedChurch = False
        $ visitedStore = False
        $ visitedShop = False
        $ visitedGrave = False
        $ visitedSchool = False
        $ visitedMemorial = False
        if daythreeplays < 2:
            menu:
                #show map
                omni "Where would you like to go today?"

                "Town Square":
                    if visitedTown:
                        omni "Isn't this place a little too familiar for you?"
                        jump daythree
                    else:
                        "lalalallaal"
                        $ visitedTown = True
                        $ daythreeplays += 1
                        jump daythree
        
                "Gardens":
                    if visitedGarden:
                        omni "Isn't this place a little too familiar for you?"
                        jump daythree
                    else:
                        "lalalalalala"
                        $ visitedGarden = True
                        $ daythreeplays += 1
                        jump daythree

                "Church":
                    if visitedChurch:
                        omni "Isn't this place a little too familiar for you?"
                        jump daythree
                    else:
                        "lalalalalalla"
                        $ visitedChurch = True
                        $ daythreeplays += 1
                        jump daythree
        
                "Grocery Store":
                    if visitedStore:
                        omni "Isn't this place a little too familiar for you?"
                        jump daythree
                    else:
                        "lallalalalaal"
                        $ visitedStore = True
                        $ daythreeplays += 1
                        jump daythree

                "Shopping Center":
                    if visitedShop:
                        omni "Isn't this place a little too familiar for you?"
                        jump daythree
                    else:
                        "lalalalalalalallala"
                        $ visitedShop = True
                        $ daythreeplays += 1
                        jump daythree
        
                "Graveyard":
                    if visitedGrave:
                        omni "Isn't this place a little too familiar for you?"
                        jump daythree
                    else:
                        "lalalalalala"
                        $ visitedGrave = True
                        $ daythreeplays += 1
                        jump daythree
        
                "School":
                    if visitedSchool:
                        omni "Isn't this place a little too familiar for you?"
                        jump daythree
                    else:
                        "lalalalalal"
                        $ visitedSchool = True
                        $ daythreeplays += 1
                        jump daythree

                "Memorial":
                    if visitedMemorial:
                        omni "I'm not quite sure I'm allowed to let you in here."
                        omni "Not after what happened last time..."
                        jump daythree
                    else:
                        "error"
                        $ visitedMemorial = True
                        $ daythreeplays += 1
                        jump daythree
            


    ##### NUMBO 4 FOURRRR
    $ dayfourplays = 0
    ##label dayfour:

    #### 4.5
    ##### THIS DAY ISNT REALLLL
    $ dayhalfplays = 0
    ##label dayhalf:
        
    ##### NOW THATS MAMBO NUMBER 5 BABYYY
    ### (a lil bit of jessica in my life)
    $ dayfiveplays = 0
    ##label dayfive:
        
    
    # This ends the game.
    return