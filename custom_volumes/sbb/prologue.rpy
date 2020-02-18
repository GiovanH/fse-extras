transform __p__feintright:
    ypos 730 xpos 640
    easeout 0.12 xpos 320
    pause(0.5)
    linear 0.12 xpos 640

transform __p__quickbouncetwice:
    ypos 730
    easeout 0.12 ypos 716
    linear 0.12 ypos 730
    easeout 0.12 ypos 716
    linear 0.12 ypos 730

image !brownblood = "{{assets}}/images/brownblood.png"

define !brownstab = Fade(0.09, 0.09, 0.15, color="#7F4000")

## SECILY ROUTE START ##
########################



label __package_entrypoint___prologue:

    $ renpy.block_rollback()
    
    $ main_menu = False

    $ feint = False
    $ appel = False

    show image gui.main_menu_background
    scene black with Dissolve(1.5)
    window hide

    show background !warehouse with Dissolve(1.5)
    show !secily sword hold with Dissolve(1.5)
    play music "{{assets}}/music/secilytheme.mp3" loop

    $ quick_menu = True

    !secily sword hold speak "1.e4 Go ahead, take it. ...e5"

    show !secily sword hold at twitch

    "You proffer the dueling rapier, your second-best, to the ruffian. You took down his two mates easily enough, and now he’s the last one standing. Unarmed and afraid."
    "This is part of the ritual for you. He’s not dying alone."

    show !secily sword hold speak
    !secily "2.f4 It’s not a trick. You know that. I’m sure all your ilk has heard of me. ...exf4"
    !secily "3.Nf3 There we go, you even know how to hold it. ...Be7"
    !secily menacing speak "4.Bc4 Sometimes I get asked why I do this. ...Bh4+"
    show !secily menacing

    "He stands, eyes narrowed, and you touch the tips of your blades. Proper stance and all. You wish more smugglers had the touch of class this soul did."

    "You almost feel bad for what’s about to happen."
    "Then you remember the document detailing the deaths caused by this counterfeit medicine lab, start to finish, like it was photocopied straight into your head."

    !secily menacing speak "5.g3 There’re three reasons. Here’s the first: it’s only fair. Face to face, blade to blade, an honest chance. You deserve that. Everyone deserves that. If you die, you die with nobility. With courage. ...fxg3"
    !secily sword hold speak "6.O-O If you don’t, you walk out of here the first man in twelve sweeps to win a duel with me. And that’s something to fight for. ...gxh2+" 

    play music "{{assets}}/music/secilyfight.mp3" loop
    
    !secily engarde "7.Kh1 {i}Allez!{/i} ...Be7"
    
    menu:
        "You start the bout with..."
        
        "A feint to the right.":
            $ feint = True

            show !secily lunge at !feintright

            "You start the bout with a feint to the right, but he doesn’t take the bait, holding steady... but too passive. A shame."
            "A bit more aggression and he’d be a real challenge. You straighten yourself to continue the duel."
            
        "An appel.":
            $ appel = True

            show !secily engarde at !quickbouncetwice

            "You start the bout, aiming to shock him with the noise of your stomp on approach. He flinches at it, but not enough to be a real opening."
            "Good composure, kid."
            
        "A simple thrust.":
            jump __p__thrust    

        
label __p__thrust:

    show !secily lunge at twitch

    if not appel and not feint:
        "You start the bout with a simple thrust. This one knows what he’s doing, you can see it in his stance."
        "He might’ve been just like you, learning the épée in some bright office, dreaming of holding a real regulator’s blade like Proserpina, gleaming in your hand."

        jump __p__continue_prologue_1
    
    if appel and feint:
        "You end the bout with a simple thrust. This one knows what he’s doing, you can see it in his stance."
        "He might’ve been just like you, learning the épée in some bright office, dreaming of holding a real regulator’s blade like Proserpina, gleaming in your hand."

        jump __p__continue_prologue_1

    if appel or feint:
        "You follow up with a simple thrust. This one knows what he’s doing, you can see it in his stance."
        "He might’ve been just like you, learning the épée in some bright office, dreaming of holding a real regulator’s blade like Proserpina, gleaming in your hand."

        jump __p__continue_prologue_1




label __p__continue_prologue_1:
    "If so, he strayed. You didn’t."
    
    "Your superior technique prevails and you catch his blade in a {i}prise-de-fer{/i}, all the leverage yours."

    stop music
    show !secily lunge
    with hpunch

    play sound "{{assets}}/music/sfx/stab.mp3"
    pause(.25)

    show !brownblood with !brownstab
    
    "You press your advantage and slide effortlessly closer with the tip until you’ve pierced his chest right beside his bloodpusher, sliding your sharp point deeper to draw a torrent of rosy brown blood."
    "Your other sword falls out of his hand with an indelicate clatter as he chokes out in pain. You catch him as he leans over, dying, and begin speaking in his ear, calm as always."

    play music "{{assets}}/music/secilytheme.mp3" loop
    
    !secily menacing speak "{size=-4}8.Bxf7+ The second reason I’m doing this is the one I need you to hear. It’s the important one. If there’s anything, {i}anything{/i} out there for your soul after this, if you meet any kind of maker or can see any shred of any of the dead, I need you to carry a message for me. ...Kxf7{/size}" 
    !secily "9.Ne5+ Tell them this is for Ahlina Robiad. I will send them as many as they need to avenge her. ...Ke6"

    show !secily menacing
    
    "He’s nodding, even as blood starts to trickle from the corner of his mouth. Good lad."
    
    !secily menacing speak "10.Qg4+ And if you see {i}her{/i}, tell her I’m sorry. ...Kxe5" 
    !secily "11.Qf5+ I can’t join her just yet. ...Kd6"

    show !secily menacing
    
    "You wait for him to slump over, dead, and slide him off your blade, taking a picture with your visor to document another successful compliance initiative to your superiors."
    "You pull a kerchief out of your coat pocket and wipe your blade clean. You speak to no one as you sheathe it and walk out of the room."
    
    !secily sword hold speak "12.Qd5++ The third reason is that I enjoy it. And I always have. ...1-0"

    show !secily sword hold
    scene blackcover with Dissolve(1.5)
    stop music fadeout 1.5
    pause(1.5)

    # SBB prologue doesn't use an end card.
    return
