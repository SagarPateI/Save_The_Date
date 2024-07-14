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

transform background_size: 
    zoom 0.84

transform newSize:
    zoom 1.5

transform halfSize:
    zoom 0.5

label start:
    "Jake" "Okay, deep breath. This is going to be fine. It’s just a Computer Science major I matched with on Prowlr™. He’s coming all the way from Long Island to meet me... that’s gotta mean something, right?"
    "Jake" "What could possibly go wrong!?"

    "(sound of a train approaching)"

    menu:
        "No Running Away":
            jump goodpath1

        "Run Away":
            jump badpath1
    
    label badpath1:
        "Jake" "Well, I could say the wrong thing… or wear the wrong outfit, or the waiter’ll forget our orders and we’ll starve or a piano could fall on us while we eat and we’ll die - not from the impact BUT FROM THE SHOCK OF A DATE GONE SO HORRIBLY WRONG OH GOD I CAN’T DO THIIISSSS!!!!"
        "(Jake’s anxiety builds up, listing out various worries.)"
        "Jake" "I... I just can’t do this… I’m sorry!"
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
        "Jake" "I cannot be late for this - gotta call an Uber. My battery’s a bit low, so I’ll have to turn off my Life180 location tracker... What could go wrong?"
        "UberDriver" "Hop in, buddy! Where to?"
        "Narrator" "Many things could go wrong. Jake would discover this right as the sleeping agent sprinkled onto their seat wore off, allowing them to wake up just in time to watch as their Uber driver harvested their remaining organs. Whoopsies."
        return

    label goodpath2:
        "Jake" "Boy do I love trains. The next train leaves in five minutes! I better get going quick!!"
        "Narrator" "Jake sprints off towards the train station"
        "Jake" "I should probably text him and let him know I’m at the station."
        scene bg street at background_size
        with fade
        "Jake" "Where is he? I can’t see him anywhere!"
        "Narrator""(Footsteps approaching)"
        "Narrator" "(Your date taps you on your shoulder!)"
        "Jake" "WAHH!? Where did yo- how?"
        show thomas happy
        "Thomas" "Hi (said in a way that only a godlike sexdonis like him can say~)"
        "Jake" "(Quick, say something a CS major could find funny!)"
        "Jake" "How do Linux users greet each other? Hello, Wor–"
        "Thomas" "I’d just like to interject for a moment. What you’re referring to as Linux, is in fact, GNU/Linux, or as I’ve recently taken to calling 
it, GNU plus Linux."
        "Thomas" "Linux is not an operating system unto itself, but 
rather another free component of a fully functioning GNU system made 
useful by the GNU corelibs, shell utilities and vital system components 
comprising a full OS as defined by POSIX."
        "Jake" "(Oh no, he didn’t get the joke at all. What did I get myself into!?)"
        "Jake" "(Smooth, Jake... Real smooth.)"
        "Narrator" "Jake and Thomas walk over to a popular (and authentic!) italian restaurant and were seated at a table. They engage in pleasant conversation and the mometnts just fly by, however..."
        "Jake" "(It’s been hours and the waiter still has not visited our table! What should I do?!)"

    menu:
        "Call the Waiter":
            jump goodpath3

        "Don’t Call the Waiter":
            jump badpath3
    
    label badpath3:
        "Jake" "Erm… I guess I’m just too shy to call the waiter over! uwu"
        hide thomas happy
        show thomas dead
        "Thomas" "(Throws up and dies of cringe!)"
    
    label goodpath3:
        "Jake" "Oh waiter!!!"
        hide thomas happy 
        show waiter at center
        show waiter at halfSize
        "Waiter" "Welcome to generic restaurant, we serve food. What could you possibly want from me?"
    
    menu:
        "Let’s order spaghetti with extra penicillin!":
            jump badpath4
        "We’ll order burgers at this fine Itallian establishment!":
            jump goodpath4
    
    label badpath4:
        "Jake" "Spaghetti with extra penicillin please!"
        "Waiter" "I’ll get that for you right away!"
        hide waiter
        "Narrator" "True to his word, the waiter brings out the penicillin spaghetti expeditiously and then proceeds to serve the other tables."
        show thomas happy
        "Thomas" "Oh boy! I love penicillin!"
        hide thomas happy
        "Narrator" "Little did Thomas know, he was in for a rude awakening!"
        "Jake" "How’s your burger, babes?"
        show thomas allergy
        "Thomas" "*Choking noises*"
        "Jake" "THOMAS!!! NOOOOOOOO!!!!!"
        show thomas dead
        "Narrator" "Thomas has died due to his previously unknown Penicillin allergy!"
        return

    label goodpath4:
        "Jake" "I’ll have one normal burger for me and one sexy burger for my date please. *wink*"
        hide waiter
        show thomas blushing
        "Thomas" "Oh my! What a normal and attractive person!"
        hide thomas blushing
        show waiter at center
        show waiter at halfSize
        "Waiter" "*chuckles* Right away, sir!"
        hide waiter
        "Narrator" "The waiter bows and exits stage left just as the burgers appear miraculously on the table. Talk about quality italian service!"
        "Narrator" "The date between Jake and Thomas seems to be going well! They are talking, laughing and having a great time!"
        "Narrator" "You’ve gained relationship points with Thomas!"
        "Narrator" "Just kidding, we don’t have any mechanics like that in this video game!"
        "Jake" "Those were the greatest burgers I’ve ever had! I can’t believe they came from an italian restaurant!"
        "Jake" "Though, I have a question... Why did you put mustard on your burger?"
        show thomas neutral
        "Thomas" "I just think mustard is the greatest condiment in the world."
        "Thomas" "It is yellow which implies that you must have great caution when partaking in its delicious compared to the redness of ketchup!"
        hide thomas neutral 
        show thomas upset
        "Thomas" "What, do you take issue with mustard?"
    menu:
        "I can’t stand mustard!!!":
            jump badpath5

        "I love mustard too!!!":
            jump goodpath5
    
    label badpath5:
        "Jake" "Ugh, I can’t stand mustard. It’s so gross and inferior to horseradish"
        show thomas angry
        "Thomas" "What did you just say..."
        "Jake" "It’s just like the worst condiment ever, I can’t imagine anyone liking it"
        show thomas angry at newSize
        "Thomas" "THAT’S THE LAST STRAW!!!"
        hide thomas angry
        "Narrator" "And so Thomas jumps across the table and viciously assaults Jake, ending his life instantly before dashing off towards the now vermillion sun"
        return

    label goodpath5:
        "Jake" "Mustard is pretty good, I like it as an ingredient more than a condiment though."
        hide thomas upset
        show thomas happy
        "Thomas" "That’s a fair and valid opinion, I LOVE mustard."
        "Jake" "It’s so hot that you have passions in life!"
        hide thomas happy
        "Narrator" "You’re killing it on this date! The moments continue to fly by and you almost don’t even notice the chips just magically phasing into existence on the table"
        "Narrator" "Thomas picks up the chip and just... gets a lil freaky with it! He seems to be licking the salt very slowly off of the chip???"
        "Jake" "(What in the...)"
    
    menu:
        "Aww! That is so adorable!":
            jump goodpath6
        
        "This is so disgusting!":
            jump badpath6
    
    label badpath6:
        "Jake" "Ummm you know that’s bad for you right? It’s also bad table manners to boot-"
        show thomas angry at center
        show thomas angry at newSize
        "Narrator" "Vaporizes you instantly into a pile of salt he can consume!"
        return

    label goodpath6:
        "Jake" "Omigod you’re so sodium-chloride-pilled."
        show thomas happy
        "Thomas" "(Smirks sexily as he unscrews the top of the shaker, unhinges his python-like jaw and empties the entire container into it.)"
        hide thomas happy
        "Narrator" "Thomas and Jake finish eating their food and now the decisive hour is finally upon them!"
        "Narrator" "The bill is delivered to their table! What will Jake do?!"
    
    menu:
        "Make Thomas Pay!":
            jump badpath7
        
        "Split the Bill!":
            jump goodpath7
        
        "Pay the Entire Bill!":
            jump badpath8
    
    label badpath7:
        show thomas upset
        "Thomas" "Me? Pay for everything? I don’t like that!"
        hide thomas upset
        "Narrator" "Yea, he really didn’t like that... Your date is ruined!"
        return

    label badpath8:
        "Jake" "I’ll pay for everything! Don’t worry-"
        "Narrator" "The Mafia snipes Jake before he can finish his sentence! The date is over!"
    
    label goodpath7:
        "Jake" "Let’s split the bill!"
        show thomas happy
        "Thomas" "Yea, I agree with that! If we had paid this any other way you probably would have died to be honest!"
        hide thomas happy
        show thomas blushing
        "Thomas" "By the way, this date was really enjoyable... Lets do this again sometime!"
        "Jake" "Woohoo!!!"
        hide thomas blushing
        Narrator "And thus the date is successful... The end!"
        return


        


    








    

        
    
        



        

        



