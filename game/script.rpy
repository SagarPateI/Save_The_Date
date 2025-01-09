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
    play music slow1
    voice "audio/voicelines/jake/Okay deep breath.ogg"
    "Jake" "Okay, deep breath. This is going to be fine. It’s just a Computer Science major I matched with on Prowlr™. He’s coming all the way from Long Island to meet me... that’s gotta mean something, right?"
    voice "audio/voicelines/jake/What Could Possibly Go Wrong.ogg"
    "Jake" "What could possibly go wrong!?"

    voice "audio/voicelines/narrator/Train-Approaching.ogg"
    "(sound of a train approaching)"

    menu:
        "No Running Away":
            jump goodpath1

        "Run Away":
            jump badpath1
    
    label badpath1:
        stop music 
        play music badend
        voice "audio/voicelines/jake/I can_t do this, run away.ogg"
        "Jake" "Well, I could say the wrong thing... or wear the wrong outfit, or the waiter’ll forget our orders and we’ll starve or a piano could fall on us while we eat and we’ll die - not from the impact BUT FROM THE SHOCK OF A DATE GONE SO HORRIBLY WRONG OH GOD I CAN’T DO THIIISSSS!!!!"
        voice "audio/voicelines/narrator/Narr-BE-1.ogg"
        "Narrator" "Jake’s anxiety builds up, listing out various worries."
        voice "audio/voicelines/jake/I can_t do this, I_m sorry (run away 2).ogg"
        "Jake" "I... I just can’t do this... I’m sorry!"
        return

    label goodpath1:
        voice "audio/voicelines/jake/It’s Just a Date.ogg"
        "Jake" "Okay, deep breath. It’ll go fine!! I’m gonna be fine. It’s just a date."
        voice "audio/voicelines/jake/Should I call and Uber or take the train.ogg"
        "Jake" "Now, should I call an Uber or take the train?"

    menu:
        "Take the Train":
            jump goodpath2

        "Call an Uber":
            jump badpath2 

    label badpath2:
        stop music 
        play music badend
        voice "audio/voicelines/jake/I cannot be late for this, gotta call an Uber.ogg"
        "Jake" "I cannot be late for this - gotta call an Uber!"
        voice "audio/voicelines/jake/Low battery (Uber end).ogg"
        "Jake" "My battery’s a bit low, so I’ll have to turn off my Life180 location tracker... What could go wrong?"
        voice "audio/voicelines/uber-driver/Uber-Driver-BE-1.ogg"
        "UberDriver" "Hop in, buddy! Where to?"
        voice "audio/voicelines/narrator/Narr-BE-2.ogg"
        "Narrator" "Many things could go wrong. Jake would discover this right as the sleeping agent sprinkled onto their seat wore off, allowing them to wake up just in time to watch as their Uber driver harvested their remaining organs. Whoopsies."
        return

    label goodpath2:
        voice "audio/voicelines/jake/Boy Do I Love Trains.ogg"
        "Jake" "Boy do I love trains. The next train leaves in five minutes! I better get going quick!!"
        voice "audio/voicelines/narrator/Narrator-Good-Ending-1.ogg"
        "Narrator" "Jake sprints off towards the train station"
        voice "audio/voicelines/jake/I should probably text him….ogg"
        "Jake" "I should probably text him and let him know I’m at the station."
        scene bg street at background_size
        with fade
        voice "audio/voicelines/jake/Where is he, I can’t see him anywhere.ogg"
        "Jake" "Where is he? I can’t see him anywhere!"
        voice "audio/voicelines/narrator/Footsteps-Approaching.ogg"
        "(Footsteps approaching)"
        voice "audio/voicelines/narrator/Narr-GE-2.ogg"
        "Narrator" "(Your date taps you on your shoulder!)"
        voice "audio/voicelines/jake/WOAH, WHERE DID YOU.ogg"
        "Jake" "WAHH!? Where did yo- how?"
        show thomas happy
        voice "audio/voicelines/thomas/Hi.- (said in a way that only a godlike sexdonis like him can say~).ogg"
        "Thomas" "Hi. (said in a way that only a godlike sexdonis like him can say~)"
        voice "audio/voicelines/jake/Say something a CS major could find funny.ogg"
        "Jake" "(Quick, say something a CS major could find funny!)"
        voice "audio/voicelines/jake/How do link user say hello.ogg"
        "Jake" "How do Linux users greet each other? Hello, Wor–"
        voice "audio/voicelines/thomas/I’d just like to interject for a moment.ogg"
        "Thomas" "I’d just like to interject for a moment. What you’re referring to as Linux, is in fact, GNU/Linux, or as I’ve recently taken to calling it, GNU plus Linux."
        voice "audio/voicelines/thomas/Linux is not an operating system unto itself.ogg"
        "Thomas" "Linux is not an operating system unto itself, but rather another free component of a fully functioning GNU system made useful by the GNU corelibs, shell utilities and vital system components comprising a full OS as defined by POSIX."
        voice "audio/voicelines/jake/He didn’t get the joke at all!.ogg"
        "Jake" "(Oh no, he didn’t get the joke at all. What did I get myself into!?)"
        voice "audio/voicelines/jake/Smooth Jake.ogg"
        "Jake" "(Smooth, Jake... Real smooth.)"
        voice "audio/voicelines/narrator/Narr-GE-3.ogg"
        "Narrator" "Jake and Thomas walk over to a popular (and authentic!) italian restaurant and were seated at a table. They engage in pleasant conversation and the moments just fly by, however..."
        voice "audio/voicelines/jake/It’s been hours and the waiter isn’t here.ogg"
        "Jake" "(It’s been hours and the waiter still has not visited our table! What should I do?!)"

    menu:
        "Call the Waiter":
            jump goodpath3

        "Don’t Call the Waiter":
            jump badpath3
    
    label badpath3:
        stop music 
        play music badend
        voice "audio/voicelines/jake/Too shy.ogg"
        "Jake" "Erm... I guess I’m just too shy to call the waiter over! uwu"
        hide thomas happy
        show thomas dead
        voice "audio/voicelines/thomas/(Throws up and dies of cringe!).ogg"
        "Thomas" "(Throws up and dies of cringe!)"
        voice "audio/voicelines/narrator/Narr-BE-3.ogg"
        "Narrator" "And thus Thomas passes away. The date is over!"
        return
    
    label goodpath3:
        voice "audio/voicelines/jake/Oh, waiter.ogg"
        "Jake" "Oh waiter!!!"
        hide thomas happy 
        show waiter at center
        show waiter at halfSize
        voice "audio/voicelines/waiter/Waiter-GE-1.ogg"
        "Waiter" "Welcome to generic restaurant, we serve food. What could you possibly want from me?"
    
    menu:
        "Let’s order spaghetti with extra penicillin!":
            jump badpath4
        "We’ll order burgers at this fine Italian establishment!":
            jump goodpath4
    
    label badpath4:
        stop music 
        play music badend
        voice "audio/voicelines/jake/Spaghetti-please.ogg"
        "Jake" "Spaghetti with extra penicillin please!"
        "Waiter" "I’ll get that for you right away!"
        hide waiter
        voice "audio/voicelines/narrator/Narr-BE-4.ogg"
        "Narrator" "True to his word, the waiter brings out the penicillin spaghetti expeditiously and then proceeds to serve the other tables."
        show thomas happy
        voice "audio/voicelines/thomas/Oh boy! I love penicillin.ogg"
        "Thomas" "Oh boy! I love penicillin!"
        hide thomas happy
        voice "audio/voicelines/narrator/Narr-BE-5.ogg"
        "Narrator" "Little did Thomas know, he was in for a rude awakening!"
        voice "audio/voicelines/jake/How's your spaghetti, babes.ogg"
        "Jake" "How’s your spaghetti, babes?"
        show thomas allergy
        voice "audio/voicelines/thomas/Choking noises.ogg"
        "Thomas" "*Choking noises*"
        voice "audio/voicelines/jake/THOMAS NO.ogg"
        "Jake" "THOMAS!!! NOOOOOOOO!!!!!"
        show thomas dead
        voice "audio/voicelines/narrator/Narr-BE-6.ogg"
        "Narrator" "Thomas has died due to his previously unknown Penicillin allergy!"
        return

    label goodpath4:
        voice "audio/voicelines/jake/One normal burger for me!.ogg"
        "Jake" "I’ll have one normal burger for me and one sexy burger for my date please. *wink*"
        hide waiter
        show thomas blushing
        voice "audio/voicelines/thomas/Oh my! What a normal and attractive person.ogg"
        "Thomas" "Oh my! What a normal and attractive person!"
        hide thomas blushing
        show waiter at center
        show waiter at halfSize
        voice "audio/voicelines/waiter/Waiter-GE-2.ogg"
        "Waiter" "*chuckles* Right away, sir!"
        hide waiter
        voice "audio/voicelines/narrator/Narr-GE-4.ogg"
        "Narrator" "The waiter bows and exits stage left just as the burgers appear miraculously on the table. Talk about quality italian service!"
        voice "audio/voicelines/narrator/Narr-GE-5.ogg"
        "Narrator" "The date between Jake and Thomas seems to be going well! They are talking, laughing and having a great time!"
        voice "audio/voicelines/narrator/Narr-GE-6.ogg"
        "Narrator" "You’ve gained relationship points with Thomas!"
        voice "audio/voicelines/narrator/Narr-GE-7.ogg"
        "Narrator" "Just kidding, we don’t have any mechanics like that in this video game!"
        show thomas neutral
        voice "audio/voicelines/thomas/How’s the burger, babes.ogg"
        "Thomas" "How’s the burger, babes?"
        hide thomas neutral
        voice "audio/voicelines/jake/Greatest-burgers-ever.ogg"
        "Jake" "Those were the greatest burgers I’ve ever had! I can’t believe they came from an italian restaurant!"
        voice "audio/voicelines/jake/Why did you put mustard on your burger.ogg"
        "Jake" "Though, I have a question... Why did you put mustard on your burger?"
        show thomas neutral
        voice "audio/voicelines/thomas/I just think mustard is the greatest condiment in the world.ogg"
        "Thomas" "I just think mustard is the greatest condiment in the world."
        "Thomas" "It is yellow which implies that you must have great caution when partaking in its deliciousness compared to the redness of ketchup!"
        hide thomas neutral 
        show thomas upset
        voice "audio/voicelines/thomas/What, do you take issue with mustard.ogg"
        "Thomas" "What, do you take issue with mustard?"
    menu:
        "I can’t stand mustard!!!":
            jump badpath5

        "I love mustard too!!!":
            jump goodpath5
    
    label badpath5:
        stop music 
        play music badend
        voice "audio/voicelines/jake/Ugh, I can’t stand mustard.ogg"
        "Jake" "Ugh, I can’t stand mustard. It’s so gross and inferior to horseradish"
        show thomas angry
        voice "audio/voicelines/thomas/What did you just say.ogg"
        "Thomas" "What did you just say..."
        voice "audio/voicelines/jake/It’s like the worst condiment ever.ogg"
        "Jake" "It’s just like the worst condiment ever, I can’t imagine anyone liking it"
        show thomas angry at newSize
        voice "audio/voicelines/thomas/THAT’S THE LAST STRAW.ogg"
        "Thomas" "THAT’S THE LAST STRAW!!!"
        hide thomas angry
        voice "audio/voicelines/narrator/Narr-BE-7.ogg"
        "Narrator" "And so Thomas jumps across the table and viciously assaults Jake, ending his life instantly before dashing off towards the now vermillion sun"
        return

    label goodpath5:
        voice "audio/voicelines/jake/Mustard is pretty good.ogg"
        "Jake" "Mustard is pretty good, I like it as an ingredient more than a condiment though."
        hide thomas upset
        show thomas happy
        voice "audio/voicelines/thomas/That’s a fair and valid opinion.ogg"
        "Thomas" "That’s a fair and valid opinion, I LOVE mustard."
        voice "audio/voicelines/jake/It’s so hot that you have passions.ogg"
        "Jake" "It’s so hot that you have passions in life!"
        hide thomas happy
        voice "audio/voicelines/narrator/Narr-GE-8.ogg"
        "Narrator" "You’re killing it on this date! The moments continue to fly by and you almost don’t even notice the chips just magically phasing into existence on the table"
        voice "audio/voicelines/narrator/Narr-GE-9.ogg"
        "Narrator" "Thomas picks up the chip and just... gets a lil freaky with it! He seems to be licking the salt very slowly off of the chip???"
        voice "audio/voicelines/jake/What in the….ogg"
        "Jake" "(What in the...)"
    
    menu:
        "Aww! That is so adorable!":
            jump goodpath6
        
        "This is so disgusting!":
            jump badpath6
    
    label badpath6:
        stop music 
        play music badend
        voice "audio/voicelines/jake/You know that’s bad for you right_.ogg"
        "Jake" "Ummm you know that’s bad for you right? It’s also bad table manners to boot-"
        show thomas angry at center
        show thomas angry at newSize
        voice "audio/voicelines/narrator/Narr-BE-8.ogg"
        "Narrator" "*Vaporizes you instantly into a pile of salt he can consume!*"
        return

    label goodpath6:
        voice "audio/voicelines/jake/Sodium Chloride Pilled.ogg"
        "Jake" "Omigod you’re so sodium-chloride-pilled."
        show thomas happy
        voice "audio/voicelines/thomas/(Smirks sexily as he unscrews the top of the shaker).ogg"
        "Thomas" "(Smirks sexily as he unscrews the top of the shaker, unhinges his python-like jaw and empties the entire container into it.)"
        hide thomas happy
        voice "audio/voicelines/narrator/Narr-GE-10.ogg"
        "Narrator" "Thomas and Jake finish eating their food and now the decisive hour is finally upon them!"
        voice "audio/voicelines/narrator/Narr-GE-11.ogg"
        "Narrator" "The bill is delivered to their table! What will Jake do?!"
    
    menu:
        "Make Thomas Pay!":
            jump badpath7
        
        "Split the Bill!":
            jump goodpath7
        
        "Pay the Entire Bill!":
            jump badpath8
    
    label badpath7:
        stop music
        play music badend
        show thomas upset
        voice "audio/voicelines/thomas/Me- Pay for everything- I don’t like that.ogg"
        "Thomas" "Me? Pay for everything? I don’t like that!"
        hide thomas upset
        voice "audio/voicelines/narrator/Narr-BE-9.ogg"
        "Narrator" "Yea, he really didn’t like that... Your date is ruined!"
        return

    label badpath8:
        stop music 
        play music badend
        voice "audio/voicelines/jake/I’ll pay for everything.ogg"
        "Jake" "I’ll pay for everything! Don’t worry-"
        voice "audio/voicelines/narrator/Narr-BE-10.ogg"
        "Narrator" "The Mafia snipes Jake before he can finish his sentence! The date is over!"
        return
    
    label goodpath7:
        play music peaceful
        voice "audio/voicelines/jake/Let’s split the bill.ogg"
        "Jake" "Let’s split the bill!"
        show thomas happy
        voice "audio/voicelines/thomas/Yea, I agree with that.ogg"
        "Thomas" "Yea, I agree with that! If we had paid this any other way you probably would have died to be honest!"
        hide thomas happy
        show thomas blushing
        voice "audio/voicelines/thomas/By the way, this date was really enjoyable.ogg"
        "Thomas" "By the way, this date was really enjoyable... Lets do this again sometime!"
        voice "audio/voicelines/jake/Woohoo.ogg"
        "Jake" "Woohoo!!!"
        hide thomas blushing
        voice "audio/voicelines/narrator/Narr-GE-12.ogg"
        "Narrator" "And thus the date is successful... The end!"
        return