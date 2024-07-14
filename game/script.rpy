# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
# $ Thomas = Character('Zeil', color="#E03B8B")
default Thomas = Character('Thomas', color="#E03B8B")
default Jake = Character('Protagonist', color="#E03B8B")         
default UberDriver = Character('Uber Driver', color="#E03B8B")
default Waiter = Character('Waiter', color="#E03B8B")
default Narrator = Character('Narrator', color="#E03B8B")
# The game starts here.

transform half_size: 
    zoom 0.84

label start:
    "Jake" "Okay, deep breath. This is going to be fine. It’s just a Computer Science major I matched with on Prowlr™. He’s coming all the way from Long Island to meet me… that’s gotta mean something, right?"
    "Jake" "What could possibly go wrong!?"

    "(sound of a train approaching)"

    menu:
        "No Running Away":
            jump goodpath1

        "Run Away":
            jump badpath1
    
    label badpath1:
        "Jake" "Well, I could say the wrong thing… or wear the wrong outfit, or the waiter’ll forget our orders and we’ll starve or a piano could fall on us while we eat and we’ll die - not from the impact BUT FROM THE SHOCK OF A DATE GONE SO HORRIBLY WRONG OH GHOD I CNA’T DO THIIISSSS!!!!"
        "(Jake's anxiety builds up, listing out various worries.)"
        "Jake" "I… I just can’t do this… I’m sorry!"
        return

    label goodpath1:
        "Jake" "Okay, deep breath. It’ll go fine!! I’m gonna be fine. It’s just a date."
        "Jake" "Now, should I call an Uber or take the train?"

    menu:
        "Take the Train":
            jump goodpath2

        "Call an Uber":
            jump badpath2 

    label badpath2:
        "Jake" "I cannot be late for this - gotta call an Uber. My battery’s a bit low, so I’ll have to turn off my Life180 location tracker… What could go wrong?"
        "UberDriver" "Hop in, buddy! Where to?"
        "Many things could go wrong. Jake would discover this right as the sleeping agent sprinkled onto their seat wore off, allowing them to wake up just in time to watch as their Uber driver harvested their remaining organs. Whoopsies."
        return

    label goodpath2:
        "Jake" "Boy do I love trains. The next train leaves in five minutes! I better get going quick!!"
        "Jake sprints off towards the train station"
        "Jake" "I should probably text him and let him know I’m at the station."
        scene bg street at half_size
        with fade
        "Jake" "Where is he? I can't see him anywhere!"
        "(Footsteps approaching)"
        "(Your date taps you on your shoulder!)"
        "Jake" "WAHH!? Where did yo- how?"
        show thomas happy at center
        "Thomas" "Hi (said in a way that only a godlike sexdonis like him can say~)"
        "Jake" "(Quick, say something a CS major could find funny!)"
        "Jake" "How do Linux users greet each other? Hello, Wor–"
        "Thomas" "I'd just like to interject for a moment. What you're referring to as Linux, is in fact, GNU/Linux, or as I've recently taken to calling 
it, GNU plus Linux."
        "Thomas" "Linux is not an operating system unto itself, but 
rather another free component of a fully functioning GNU system made 
useful by the GNU corelibs, shell utilities and vital system components 
comprising a full OS as defined by POSIX."
        "Jake" "(Oh no, he didn’t get the joke at all. What did I get myself into!?)"
        "Jake" "(Smooth, Jake... Real smooth.)"
        "Jake and Thomas walks over to a popular (and authentic!) italian restaurant and were seated at a table. They engage in pleasant conversation and the mometnts just fly by, however..."
        "Jake" "(It's been hours and the waiter still has not visited our table! What should I do?!)"

    menu:
        "Call the Waiter":
            jump goodpath3

        "Don't Call the Waiter":
            jump badpath3
    
    label badpath3:
        "Jake" "Erm… I guess I’m just too shy to call the waiter over! uwu"
        "Thomas" "(Throws up and dies of cringe!)"
    
    label goodpath3:
        "Jake" "Oh waiter!!!"
        hide thomas happy 
        show waiter at center
        "Waiter" "Welcome to generic restaurant, we serve food. What could you possibly want from me?"
    
    menu:
        "Let's order spaghetti with extra penicillin!":
            jump badpath4
        "We'll order burgers at this fine Itallian establishment!":
            jump goodpath4
    
    label badpath4:
        "Jake" "Two burgers with extra penicillin please!"
        "Waiter" "I'll get that for you right away!"
        hide waiter
        "Narrator" "True to his word, the waiter brings out the penicillin burgers expeditiously and then proceeds to serve the other tables."
        show thomas happy at center
        "Thomas" "Oh boy! I love penicillin!"
        "Narrator" "Little did Thomas know, he was in for a rude awakening!"
        "Jake" "How's your burger, babes?"
        show thomas allergy at center
        "Thomas" "*Choking noises*"
        "Jake" "THOMAS!!! NOOOOOOOO!!!!!"
        show thomas dead at center
        "Narrator" "Thomas has died due to his previously unknown Penicillin allergy!"
        return

    label goodpath4:
        "Jake" "I’ll have one normal burger for me and one sexy burger for my date please. *wink*"
        show thomas blushing at center
        "Thomas" "Oh my! What a normal and attractive person!"
        return
        



        

        



