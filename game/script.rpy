# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
# $ Thomas = Character('Zeil', color="#E03B8B")
default Thomas = Character('Thomas', color="#E03B8B")
default Protagonist = Character('Protagonist', color="#E03B8B")         
# The game starts here.

label start:
    "Protagonist" "Omigod! I have a date with a hottie and I'm so nervous!!! I gotta make sure I say the right things!"
    "Protagonist" "aaa so scared do i run or goooo"

    menu:
        "No running away":
            jump goodpath1

        "Run away":
            jump badpath1
    
    label badpath1:
        "lol you die"
        return

    label goodpath1:
        "The protagonist makes their way to (Date Area) and finally meets their date"

    label background:
        scene bg restaurant
        with fade
        show man left at left as man1
        show man right at right as man2
        "Thomas"  "Bla Bla."
        "Protagonist"  "Bla bla."
        
    menu:
        "Call waiter over":
            jump goodpath2
            
        "Continue waiting":
            jump badpath2
         
    label badpath2:
        "lol your date leaves you"
        return

    label goodpath2:
        "Thomas"  "Bla Bla."
        "Protagonist"  "Bla bla."
    
    menu:
        "Laura Baptie Special, Hannah Wiser Toolkit, Foot Fungus":
            jump badpath3
            
        "Hannah Wiser Toolkit, Foot Fungus, Laura Baptie Special":
            jump badpath3
        
        "Foot Fungus, Hannah Wiser Toolkit, Laura Baptie Special":
            jump goodpath3

    label badpath3:
        "lol your date dies"
        return
    
    label goodpath3:
        "Thomas"  "Bla Bla."
        "Protagonist"  "Bla bla."

    menu:
        "Comment negatively on mustard":
            jump badpath4
            
        "Comment positively on mustard":
            jump goodpath4

    label badpath4:
        "lol your date kills you"
        return

    label goodpath4:
        "Thomas"  "Bla Bla."
        "Protagonist"  "Bla bla."
        
    menu: 
        "Shame him for being weird with the salt!":
            jump badpath5
        
        "Don't shame him!!! He is doing his best!":
            jump goodpath5

    label badpath5:
        "lol your date leaves you"
        return

    label goodpath5:
        "Thomas"  "Bla Bla."
        "Protagonist"  "Bla bla."
        
    menu:
        "Split Bill":
            jump goodpath6
        
        "Pay the bill yourself":
            jump badpath7
        
        "Make him pay":
            jump badpath6

    label badpath6:
        "lol your date leaves you"
        return

    label badpath7:
        "lol mafia kills you"
        return

    label goodpath6:
        "You win!"
        return



        
            


label bgm:
    play music "audio/bgm_basketball.mp3" fadein 1.0 volume 0.5
    Zeil "Oh, the basketball team is playing?"
    Zeil "It's too loud. I'll meet you in the classroom."
    
    stop music fadeout 1.0
    scene bg classroom
    with fade

label sfx:
    play sound "audio/sfx_bell.mp3"
    Zeil "Oh no. It's already time."

menu:
    "Yes":
        jump choices1_a
    "...":
        jump choices1_b

label choices1_a:
    Zeil "Good!"
    $ learned = True
    jump choices1_common

label choices1_b:
    Zeil "..."
    jump choices1_common

label choices1_common:
    Zeil "For more effects, you can check out Ren'Py's guides."
    Zeil "The link can be found in the description."

label flags:
    if learned:
        Zeil "If you learned a thing or two, please like the video!"
    else:
        Zeil "You can check out my other videos to learn more about game development!"

    return

