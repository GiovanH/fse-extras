init offset = 2

label __package_entrypoint___aradiafix:
    jump __p__volumeeightroutetwo


init:
    $ persistent.__p__aradialoops = 0


# init python:
#     def __p__rewindTo(label):
#         for i in range(0, 100):
#             print(i)
#             context = renpy.game.context()
#             print(context.current)
#             # if context.current == label:
#             #     print("BREAK")
#             #     break
#             # else:
#             #     renpy.pause(0.1)
#             renpy.rollback(1)


label __p__volumeeightroutetwo:
    
    $ renpy.block_rollback()

    $ main_menu = False

    scene black with Dissolve(1.0)

    $ quick_menu = True
    
    show bg outsidenight with dissolve
    
    play music "music/ARADIA_INTRO-OUTRO.flac" fadein 1 loop
    
    "What are you doing here? What are you doing on this awful planet? You walk. You walk and you don’t stop walking. You walk until the moons are high in the sky and the lights from the city all but fade away."
    "You walk until you can’t think about anything but walking anymore. Then you zap. ZAP Zap ZaP z8p Z4P zap zAP. Who cares."
    "You just want out of here."
    "What’s happening to you? What are these thoughts? What are these half-remembered truths? Why do all your new friends seem so fresh but so familiar? You are lost inside yourself for what simultaneously feels like both a moment and an eternity."
    
    #for this line.. If there is a way to make the text \"feel so heavy\" appear one word or letter at a time that would rule but if not then one word per screen is fine
    
    window show

    "You stop walking and lay down. The grass feels cool on the back of your head and your eyes{nw}"

    
    scene bg black with closeeyes
    "You stop walking and lay down. The grass feels cool on the back of your head and your eyes{fast} {cps=3}feel {w=0.3}so {w=0.3}heavy..."
    
    window hide

    scene bg aradiadigsite
    show aradia past uhh:
        xpos 20
        ypos 565
        zoom 2
    with openeyes
    
label __p__aradiaintro:
    
    play music "music/ARADIA-LOOP-mixed.flac" loop fadeout 1 fadein 1
    
    show aradia past uhh:
        xpos 20
        ypos 565
        zoom 2
        
    ara "0_0"

    "Troll Jesus CHRIST-"
    "Inches away from your face someone is bent over you and staring unblinkingly into your eyes."
  
    show aradia:
        ease_back 0.3 xpos 640 ypos 730 zoom 1

    "In a single panicked motion, you do a youthful sideways roll and spring to your feet."
    "This doesn’t seem to startle her at all. She doesn’t move from her precariously balanced squat. She is just looking at you. Observing you. Is she.. waiting for you to do something?"

    show aradia past grin
    
    "After exactly 21 seconds of staring directly at you she offers an entirely too toothy smile. Part of you suspects she just remembered that's what you do in these situations."
    "She examines you with an obvious curiosity."

    ara past smile "n0t the w0rst decisi0n"
    ara "t0 nap am0ng the remains 0f the deceased"

    "Haha.. what?"
    
    show aradia past confused at bounce

    "With a sarcastic motion that suggests looking literally anywhere around you, she draws your attention to what appears to be some sort of... digsite? You seem to have fallen asleep on a pile of bones."
    show aradia neutral
    
    "Her shirt is emblazoned with a dark red Aries symbol. Oh cool, another zodiac kid. You must have said \"Aries\" out loud because she immediately corrects you."

    $ __p__rand = random.choice([True, False])
    if __p__rand:
        ara serious "it is pr0n0unced ah-RAH-dee-uh"
    else:
        ara serious "it is pr0n0unced ah-RAY-dee-uh"

    "That makes sense. Although you've just met, you cannot fathom her name being pronounced any other way."
    "Your new potential friend Aradia is looking a little... what is a polite and charming way of saying \"rough around the edges?\""
    "Her clothes are a bit shabby, but maybe that’s just normal wear and tear when you’ve been hanging out in the dirt all day."
    "What... IS she doing out here in the dirt anyway?"

    ara past grin "i c0me 0ut here t0 dig up b0nes"

    "Oh! Like uh.. archeology?"

    ara past neutral "0h yes, that t00"
    ara past smile "b0nes are an imp0rtant part 0f the life cycle. y0u 0ften hear ab0ut the beauty 0f life but i find that death is just as imp0rtant and fascinating"
    ara "the finality of death has a beauty t0 it"
    ara past worried "0r it used t0"

    "You want to ask what she means, but it must be written all over your face. She very quickly moves on."

    ara past neutral "remains can tell us a lot ab0ut their 0wners life..."
    ara "h0w they lived"
    ara past smile "h0w they met their end... is that n0t a little w0nderful?"
    ara past neutral "f0ssils represent a finality"
    ara "a m0ment l0cked in time"
    ara past serious "it is the physical that remains while the spirit m0ves 0n"
    ara "everything that made them wh0 they were is g0ne"
    ara "when all is said and d0ne its 0nly the b0nes that survived t0 tell their tale"
    ara past grin "and in that way death is a s0rt 0f perfecti0n d0nt y0u think?"
    ara "their vi0lent end a s0rt 0f peace"
    ara past smile "n0thing left but the b0nes"

    "You’ve never thought about it that way. In fact you suspect you may have never thought about anything as much as this girl has thought about bones."

    ara past grin "0h b0nes are just 0ne 0f my many interests"

    "Oh, yeah, uh, you too. Big Bone Fan Over Here."

    ara past smile "i see y0u are als0 a pers0n 0f exquisite taste"
    ara past grin "0u0"

    "Well damn oh-ooh-oh to you too. Your stomach growls a little bit. Just how long were you out here?"

    ara past neutral "i disc0vered y0ur b0dy several h0urs ago"
    ara past serious "i th0ught y0u might be dead s0 i was watching y0u t0 c0nfirm my suspici0ns"

    "She was watching what she thought was a dead body? For... several hours?"

    ara past neutral "yes"
    ara "0n the l00k0ut f0r early signs 0f dec0mp0siti0n"
    ara past smile "r0t"
    ara past grin "rig0r m0rtis etc"
    ara past worried "unf0rtunately y0u are n0t c0mpletely dead"

    "Thank goodness for that."

    ara past serious "i guess"

    "Wait, what does she mean {i}completely?{/i}"
    
    show aradia past smile

    "There is a moment where her unbreaking, if not somewhat unsettling grin leans more towards normal. Well, ok, someone might describe it as normal if maybe you’d never seen anybody smile before."
    "Like if you were passing someone in the hallway and they described what a smile was to you and you were like, no no, I got this."
    "Alas, you digress."

    ara past neutral "y0u are like me"
    ara "the dead speak t0 y0u"
    ara past serious "y0u w0uld d0 well t0 pay attenti0n"
    ara "a mantle 0f d00med s0uls leashed t0 y0u"
    ara past neutral "i w0nder just h0w many times y0u have died"

    "Died? Like... Bereft of Life?"
    "She sits down beside you. She picks up some sort of rib or femur or pelvis or whatever and begins to idly draw in the dirt. It is a crude drawing of some sort of misshapen stick person. Unrelatable."

    ara past neutral "traditi0nally yes that is what dying means"
    ara past serious "but y0u are different"
    ara "i can see the gh0sts 0f all y0ur alternate iterati0ns fl0ating ar0und y0u"
    ara past smile "trying t0 help y0u"
    ara past serious "d00med timelines that have been purp0sefully erased fr0m y0ur c0nci0usness"
    ara "but y0u’re the culmination 0f the ch0ices y0u’ve made, fatal 0r 0therwise"
    ara past worried "y0u’ve been f0rced t0 leave s0 much behind y0u"

    "Your memories! Despite the fact that she seems very focused on her dirt art, you suddenly feel so seen."

    ara past serious "s0me0ne d0esn’t want y0u t0 remember"
    ara "but"
    
    show aradia past neutral:
        easein 0.3 xpos 482 ypos 700 zoom 1.25

    "She looks at you and leans in close."
    
    ara past smile "d0 y0u want t0 kn0w a secret"
    
    if persistent.__p__aradialoops > 0:
        show aradiahint at fadinghint
    
    menu:
        "[pick] Wait, did she just say {color=#a10000}\"gh0sts?\"":
            jump __p__aradiaghosts
            
        "[pick] You have never wanted anything more in your entire life." if persistent.__p__aradialoops > 0:
            jump __p__aradiasecrets
            
label __p__aradiaghosts:
    
    hide aradiahint with dissolve

    "You’re really not following. Sounds kind of fake if you’re being honest. \"Ghosts?\" Yeah. Ok. You’ve seen some weird shit on this planet but you draw the line at ghosts."

    "The spooky bit was kind of charming and cool at first but this is borderline ridiculous."
    
    show aradia neutral:
        easeout 0.3 xpos 640 ypos 730 zoom 1
    
    if persistent.__p__aradialoops > 1:
        
        jump __p__aradiaghostsquickfail
        
    if persistent.__p__aradialoops > 0:
        
        ara past confused "0h"
        
        "She almost looks hurt. Her tone turns hollow."

        ara past confused "h0w disapp0inting"
        
    else:

        ara past surprised "0h"
        
        "She almost looks hurt. Her tone turns hollow."

        ara uhh2 "h0w disapp0inting"

    show aradia turned with dissolve

    "Aradia rises and turns her back towards you. The night air feels cold, which it hadn’t before now. Perhaps on behalf of the especially cold shoulder treatment you are getting right now. Little bumps form on your skin."

    ara "i have misjudged y0u"
    ara "i th0ught i c0uld trust y0u but"
    ara "maybe y0u are just like the rest"
    ara "im 0k with that"
    ara "it d0es n0t b0ther me"
    
    show aradia at dreamfloating

    "She is floating several feet off the ground. Typically this is your sign not to say \"mmmmm sounds like it kinda DOES bother you.\""

    menu:
        
        "She is floating several feet off the ground. Typically this is your sign not to say \"mmmmm sounds like it kinda DOES bother you.\"{fast}"
        
        "[pick] Give in to your need to feel like you know better than everyone.":
                
            "Mmmmm sounds like it kinda DOES bother her. Sounds like she probably isn’t {color=#a10000}\"0k\"{/color} with it."

            "She is silent for what seems like several minutes. Have your words reached her?"
            
            show aradia past ghost with dissolve

            "When she turns to you, her eyes are white and her expression is blank."

            "Her head tilts to the side, as if she is looking at a curious bauble, her face unchanging."

            ara "n0thing really b0thers me anym0re"
            
        "[pick] Keep your mouth shut for once.":
            
            "You keep quiet. Now is not the time for your incredible insights. The restraint you have shown here will surely be rewarded."

            "She turns to you slowly, dangling somewhat limply in the air."

            ara "this act was f0r y0ur benefit"
            ara "but t0 pr0ceed any further is p0intless"
            
            show aradia past ghost with dissolve

            "Her eyes are white. Her face is unreadable. Oh my god ghosts are real too? Alternia is fucked up."

            ara "b00"

    "Oh jesus. No thanks. This secret sucks. Time to fucking go. Sorry you said ghosts were fake or whatever bullshit."

    ara "yes maybe that w0uld be best f0r b0th 0f us"
    ara "i had s0me h0pe f0r y0u"
    ara "but it l00ks like that was misplaced"

    "There is a hollow disappointment in her voice. You’ve never been negged by a ghost before."

    "She raises a hand to you, her form silhouetted by the twin moons. There is a blissful moment where you feel suspended and still."
    
    scene black with Dissolve (0.5)

    $ persistent.__p__aradialoops += 1

    call ending pass ("gameover aradia1", False, True)

    return

    # $ quick_menu = False
    
    # play music "music/game_over.mp3" fadeout 1.0 noloop
    
    # scene gameover aradia1 with Dissolve(1.0)
    
    # show bg aradiadigsite behind gameover
    # show aradia past ghost at dreamfloating behind gameover

    # $ renpy.pause(10)
    
    # hide gameover with Dissolve(1.0)
    
    # $ renpy.music.set_volume(0.7, delay=0, channel='sound')
    
    # play sound "music/BE-KIND_RE-WIND.flac"
    
    # show aradia past uhh:
    #     xpos 20
    #     ypos 565
    #     zoom 2
    
    # $ renpy.movie_cutscene("ararewind1.mpg")
    
    # $ persistent.__p__aradialoops += 1
    
    # $ quick_menu = True

    # jump __p__aradiaintro

label __p__aradiaghostsquickfail:
    
    show aradia past uhh
    
    ara "0h y0uve g0t t0 be kidding me"
    $ persistent.__p__aradialoops = 1
    scene bg black with dissolve
    
    $ achievement.grant("ACH_REALLY")
    $ achievement.sync()
    
    return

label __p__aradiasecrets:
    
    show aradia past smile:
        xpos 482 ypos 700 zoom 1.25
        
    show bg aradiadigsite
    
    if renpy.music.get_playing(channel='music') != "music/ARADIA-LOOP-mixed.flac":
        play music "music/ARADIA-LOOP-mixed.flac" loop fadeout 1 fadein 1
    
    hide aradiahint with dissolve
    
    "You have to admit you are a little fascinated by this line of inquiry. You don your signature cool person facade and tell her that there is nothing in this god forsaken universe that will keep you from hearing that secret. You throw in that you are going to die if you do not find out immediately."

    show aradia past grin:
        easeout 0.5 xpos 640 ypos 730 zoom 1
        
    "Smooth as butter, baby."
    
    ara "you dont know know how relieved i am to hear that"

    "The way she speaks has shifted slightly. It sounds fuller. Livelier. That's... good?"
    
    show aradia past glow with dissolve
    
    show aradia glow as godradia:
        xpos 640 ypos 730 zoom 0.3 xanchor 640 yanchor 730 transform_anchor True
        easeout 1.4 zoom 1
        
    pause 1.85
    
    hide aradia past glow
    hide godradia
    show aradia smile
    with dissolve
    
    ara "oh yes i have been alive for some{nw}"
    
    show aradia smile2
    ara "oh yes i have been alive for some {fast}{cps=4}{i}time{/i}{nw}"
    
    show aradia smile
    ara "oh yes i have been alive for some {i}time{/i}{fast} now"
    
    ara "all according to plan"

    "When she says the word \"time\" her eyebrows lift a little, as if cueing you in on a joke she seems to think you are completely familiar with. You give it a polite chuckle. What a character."

    "She beams, and there is a moment you forget that she was talking about ghosts and secrets."
    
    ara talk "they cant find us here"
    ara grin "we have made them very mad :D"

    "They can’t find us here? Them? We’ve? Mad? Made? You don’t ask for clarification on \"very.\" You’re feeling pretty confident about that one."

    ara talk "this is not the first{nw}"
    
    ara waggle "this is not the first{fast} {cps=4}{i}time{/i}{nw}"
    
    ara talk "this is not the first {i}time{/i}{fast} we have met"
    
    ara confused "though it is hard to say how long has passed since then"
    
    ara waggle "{cps=4}{i}time{/i}{nw}"
    
    ara confused "{i}time{/i}{fast} passes differently out here"

    "Hey apropos of nothing and far be it from you to comment on someone’s appearance but why does she look so much older? Why is she wearing the magic teen pajamas like John and them?"
    
    "How does she manage to do her makeup so well and just not brush her hair at all? You know with curls the issue might actually be over brushing. You don’t want to brag but you happen to have an encyclopedic knowledge of hair care products. Has she considered switching to a sulfate-free shampoo?"
    
    "God you wish you had hair."

    ara oh "wow you ask a lot of questions but i guess thats natural"
    ara talk "right now we are outside of the canonical relevanc-"

    show aradia mm at bounce
    
    "You are gonna have to stop her right there. You have had enough of canon and relevancy and what it means and what is or isn’t. Do you people never tire of sniffing your own farts about canonical impact."

    ara bothered "wow rude"

    "Yeah you’re rude now."

    "FUCK the narrative."

    show aradia grin at nod
    
    ara grin "absolutely phenomenal and i could not agree more"
    ara talk "like i was trying to explain, out here even the powers that be cant hear us"
    ara amused "i must say im a big fan of your work"
    ara "i have seen quite a few doomed timelines before"
    ara "but nothing like this"
    ara oh "you are something they had no contingency plans for and paradox space is practically falling apart at the seams"
    ara confused "this timeline has been peppered with inconsistencies and clues"
    ara "things here and there that cannot exist yet"
    ara "events that occur too early"
    ara oh "i figured you were doing it on purpose so i thought id get your attention"
    ara confused "but you are a little broken arent you"

    "She looks disappointed as she says this. You don’t know why she would want your attention but she has it."

    ara oh "it is not only your attention i want"
    ara "the power is shifting and the ones pulling the strings are distracted with their own meaningless problems"
    ara confused "you really cant remember anything can you"

    "You tell her you remember some things that you can’t explain. Names of things. Hints of the past. Whispers of ghosts. Wait how does she know this?"

    ara "yes they have been whispering to you quite loudly"
    ara amused "they are the fractured remnants of your departed selves"
    ara "and they have been trying to help you get here at this exact moment"

    "You ask where and when here is exactly. As you look around the scenery seems to shift. Sometimes you’re inside. Sometimes you’re outside. Sometimes you are in all places at once?"

    "You swear you see some shadow of your friends here and there but in places they don’t really belong. Why would Rose be in Kanaya’s hive? Do they know each other? You want to know what is going on and why it is so important that you are here."

    "Wherever \"here\" is."

    ara smile "i asked an old friends ghost to tell an ancient space squid to burp up a place for us to meet"

    "As one does. Sure."

    ara oh "think of it as a liminal space made of the same thing memories are made of"
    ara talk "i have spent a lot of"
    
    show aradia wagglebig
    
    ara "{i}time{i}"
    
    ara talk "in the furthest ring and in these bubbles and trying to figure out how they work"
    ara "so i have some ideas"
    ara oh "but i dont think the ones who conceived them even really know exactly"
    ara talk "what matters is the specific path you took to get here"
    ara grin "it took you many tries but you made it :D"

    "You get the feeling the more this is spelled out the less sense it will make. Kinda kills the magic."

    ara oh "yes"
    ara "that is probably true of most things"
    ara amused "instead of explaining it to you it was easier just to rewind things and have you try again"

    "You’re almost too embarrassed to ask how many times it took you to get it right."
    
    show aradia disgusted at nod

    "She puts her hand on your shoulder and just shakes her head. Oh."

    ara amused "the important thing is you made it"
    ara "i tried so many things to get you here"
    
    ara oh "0ne time i pretended to be a gh0st 0_0"

    "She affects a spooky tone, sort of waving her fingers around."

    ara talk "since accidentally entering the medium your particular class and aspect combination have given you knowledge and foresight you shouldnt have"
    ara oh "but here, where the connection to every version of yourself is strongest"
    ara smile "we can do a little housekeeping :)"

    "She reaches her hand out to yours. Oh fuck is this it? You are finally making a friend and all it took was an infinite number of tries."

    "You take her hand and she smiles at you."

    "And then everything goes off the shits."
    
    play music "music/friendsim_title_full.mp3" loop fadeout 1.0 fadein 1.0
    
    show mspaghost1 behind aradia at ghostfloating1
    show mspaghost2 behind aradia at ghostfloating2

    "Something flies into you. Oh fuck was that a ghost! You can see them! Oh fuck it has your face!"
    
    show mspaghost3 behind mspaghost1 at ghostfloating3
    show mspaghost4 behind mspaghost2 at ghostfloating4

    "There are so many of them."
    
    show aradia waggle
    
    if persistent.flash:
        show memories at fadingmemories
    else:
        show memories slower at fadingmemories

    "One by one they slam into you. The entirety of their lives and each of their deaths play out before you in real time."

    "Aradia clutches your hand and begins to laugh in a way that makes you start to think maybe this wasn’t a great idea."

    "But..."

    "You remember. You remember all of them."
    
    show aradia smile
    
    hide memories
    hide mspaghost1
    hide mspaghost2
    hide mspaghost3
    hide mspaghost4
    with dissolve

    "As the last doomed version of yourself is absorbed into your body you collapse out of both physical and mental exhaustion. You are back in the dirt. Back in the bone pile. You just sort of turn over and lay there for a second."

    "Oh my god. Mallek. Tyzias. Boldir! Oh, little Diemen. Zebr- mmm ok maybe not that guy."

    "But there is still a gap. Why are you here? You look down at the hoodie Mallek gave you. Didn’t Karkat's friend say nobody had used this symbol for a long time?"

    ara oh "i am afraid i dont know exactly"
    ara confused "my abilities have allowed me to tidy up your timelines that have happened in a sort of tentative canon"

    "You roll your eyes. She ignores you and continues."

    ara "so whatever happened to you outside of the narrative is beyond my capacity as a guide of the deceased"
    ara talk "but i know a way we can find out"
    ara "it is why i brought you here to give you back your memories"

    "God you miss just fucking around about hotdogs. You wonder what your friends are up to now. You think maybe you should check on them."

    "She looks you in the eyes, and you stop rolling them for two seconds."
    
    show bg aradiadigsite

    ara oh "arent you tired of being nice"
    ara grin "dont you just want to go apeshit"
    
    menu:
        
        "[pick] You want to see this whole place break apart.":
            
            jump __p__aradiabreakapart
            
        "[pick] Oh, look at the time, you were supposed to pick your punk rock alien daughter up at the mall like a hundred years ago or whatever.":
            
            jump __p__aradiavoid

label __p__aradiabreakapart:
    
    play music "music/ARADIA-LOOP-mixed.flac" loop fadeout 1 fadein 1

    "You think about it for a little bit. You’ve been gone for so long, and you can go back whenever you want, right? You gotta focus on the friends in the here and now."

    with hpunch
    
    "You know what. Yeah. Let’s trash this place. You stand up and kick over a small pile of bones."
    
    show aradia ohno at bounce

    ara "nooo my bones"

    "Oh oops sorry."
    
    show aradia sad at lowered

    "She kneels down next to the carnage and just stares for a little bit. Shit she looks completely devastated. It is actually kind of hard to watch."

    "You turn away. Aw biscuits. This is no way to canonize a friendship with a time god. What were you thinking? You are just too damn good at kicking over small piles of shit! Curse these powerful legs. Marvus wouldn’t do something like this. That guy was cool as hell."

    show aradia grin at default with move
    
    show aradia grin at bounce
    
    "Aradia begins to laugh in a way someone less eager for friendship might describe as a cackle."

    ara smile "look"
    
    show aradia waggle

    "She has arranged the bones into an outlandish if not slightly vulgar configuration."

    ara talk "for once i really am ok with this"
    ara "i was just lying to you for comedic effect"
    ara amused "its ok you can laugh"
    ara "try it with me say ha"

    "Ha."

    ara smile "now say it again"

    "Ha."

    ara grin "there you go :)"
    
    ara confused "i meant apeshit more in the larger sense"
    ara "i dont think any of them care about bones"
    ara amused "their loss"
    ara smile "if you really want to see things fall apart i can lead you to where you need to be"

    "You don’t know who \"they\" are and you don’t give a single solitary shit. Fuck this place. Fuck whoever took your memories. Let's go absolutely buckwild up in this piece. You kick up some dirt and don’t even care."

    show aradia oh at nod
    
    show sickle1:
        xpos -300 ypos 20
        easein 0.75 xpos 20
        
    show sickle2:
        alpha 0 xpos 20 ypos 20
        pause 1.0
        linear 0.5 alpha 1
    
    "Aradia produces a series of abstractions from thin air. Some sort of giant Ouija Board. The lens spells out S-I-C-K-L-E but in Alternian which you still don’t understand why you can read but you know what not the weirdest shit happening right now."

    hide sickle1
    hide sickle2
    
    show sickle3:
        xpos 20 ypos 20
        easeout 0.12 ypos 10
        linear 0.12 ypos 20
        pause 1.0
        easein 0.75 xpos -300
        
    "Karkat’s rambunctiously colored sickle appears mid-air. She hands it to you and excitedly takes your other hand."

    ara smile "lets go :)"

    show aradia amused
    show bg karkathive
    if persistent.flash:
        with retjump
    else:
        with retjumpslow
    
    "Over the next few hours you teleport around both Alternia and Earth dropping a bunch of seemingly random objects in nonsense places, being careful not to be seen."
    
    show bg johnfyard
    if persistent.flash:
        with retjump
    else:
        with retjumpslow
        
    "You change a gift itinerary in John’s Dad’s PDA. You sign the kids up for cellphone plans."
    
    show bg rosemomroom
    if persistent.flash:
        with retjump
    else:
        with retjumpslow

    "Are you just... doing chores? This really feels more like running errands than breaking anything."
    
    show bg kanayahive
    if persistent.flash:
        with retjump
    else:
        with retjumpslow

    ara grin "trust me"
    ara "they are going to notice and"
    ara smile "oh i bet they are gonna be so steamed"

    "You personally guarantee nobody in their right mind will care about any of this, but the moment the words leave your mouth something in the distance cracks. You don’t see it. You don’t hear it. You {i}feel{/i} it."
    
    show bg vriskahive
    if persistent.flash:
        with retjump
    else:
        with retjumpslow
        
    "You zap to the next location. You steal Vriska’s lipstick and there it is again. A crack."

    "You almost can’t believe it. This stupid plan is working. You guess the devil really is in the details. Next to you Aradia looks absolutely {i}thrilled.{/i}"

    ara oh "subtle changes in the timeline can have big repercussions but nothing like this!"
    ara "they usually just create a doomed offshoot but this is a whole doomed reality"
    ara grin "dont you know what this means"

    "You tell her that you totally do know what it means but just in case she doesn’t know, she should explain it for herself."

    show bg daveroof
    show aradia amused
    if persistent.flash:
        with retjump
    else:
        with retjumpslow
        
    ara "if you just keep up whatever it is youve been doing this whole place is going to come down"
    
    show aradia smile at bounce
    
    ara "hup"

    "Aradia lifts an air conditioning unit and throws it into the stratosphere with her mind. Wow. That's fucked up."
    
    show aradia talk at lowered
    play music "music/ARADIA_INTRO-OUTRO.flac" fadeout 1 fadein 1 loop
    
    "She sits on the edge of the roof, overlooking the city."

    ara "thank you"
    
    ara smile "this was fun"
            
    show bg roofcracked
    with hpunch

    "A faint crack forms in the sky. The curtains of space and time pull back to reveal a nothingness that does not really make you feel as whole as you had hoped."

    ara oh "but there is still a bit for you to do"
    ara "you still have a few more friends to make"

    "What? That’s it? You put a crack in reality and then just go back to spending time with some teens?"
    
    show aradia confused at default with move

    ara confused "hm"
    
    show aradia talk at bounce
    
    ara "yeah!"
    ara oh "arent you also sort of a teen"
    
    "You explain that it was never very clear actually."

    ara confused "well the answers you want are at the end of your path"
    ara "the only way to find them is to get them to come to you"
    ara talk "and they will"
    ara smile "it will all make sense then"

    "You wish that were true. You sit next to her, your legs dangling over the edge of the moulding."
    
    show aradia oh at bounce
    
    show bg daveroof with wipedown
    
    "Before your eyes, the crack in the sky appears to be sewn shut, almost as quickly as it appeared. She was right. Something is happening."

    show aradia talk
    
    "The two of you sit in each other's company for what feels like both a moment and an eternity."
    
    $ achievement.grant("ACH_ARADIA")
    $ achievement.sync()
    
    # $ persistent.__p__aradialoops = 0
    
    call ending pass ("victory aradia", True, True) from __p___call_ending_33
    
    return
    
label __p__aradiavoid:
    
    show aradia oh at bounce
    
    "Oh my god your friends??? You have to go back. You look at Aradia. This is awkward, you actually have a prior engagement. Actually... This could work! You extend your hand in the universal \"come with me\" gesture."

    scene blackcover with closeeyes
    
    pause 1
    
    show bg ardatahive at bgflicker
    
    pause 2.75
    
    show bg mall at bgflicker
    
    pause 2.25
    
    "You try to focus on anyone. The comforting chaos of Ardata’s house. The burnt out mall where you promised Daraya you’d take her with you. Yes, it’s all coming back to you. You are so glad you have an encyclopedic knowledge of that whole adventure before continuing. You zap the both of you onwards."

    scene bg black
    show tpose isolated
    show aradia oh at left1280
    if persistent.flash:
        with retjump
    else:
        with retjumpslow
        
    "You’re in the fucking hallway! There is that t-posing TURD. Aradia goes wide eyed. NO."
    
    "Not this time. Eat my whole ass you nobodies."
    
    hide tpose isolated with dissolve

    "You conjure the strongest memory you can. Oh my god. You sniffed Marvus’s armpit. The shame you are feeling sends you reeling. This is it you guess."

    show aradia ohno at bounce
    show marvus blade:
        xpos 1050 ypos 720 alpha 0
        easein 1.1 alpha 0.6
        pause 0.5
        ease_back 0.7 zoom 4 xpos -625 ypos -400 alpha 1
        
    show whitecover:
        alpha 0
        pause 1.9
        easein 0.3 alpha 1
    
    ara "YOU WHAT"
    
    scene bg aradiavoid with dissolve
    
    "But nothing is here."

    "You float listlessly in a black void."

    "Why isn’t anything here? Where is everyone? You refocus. Maybe that was just a bad point to remember."

    "You pull the strings of your hoodie tight, letting its warmth cover you like a dear friends embrace. Surely you have spent enough time with Mallek’s jacket to have formed some sort of secret bond with the memory of him. This will be enough. It needs to be enough."

    "You disappear and reappear in the same spot. You phase in and out over and over and nothing happens. Aradia watches you, but seems to be giving you space to process this."

    "It isn’t enough. It was never enough. They’re gone."
    
    $ renpy.music.set_volume(0.875, delay=1.5, channel='music')
    play sound "music/ITS_NOTHING.flac" loop

    "You go limp and just drift for a while. You hear the sad song of some sort of cosmic entity. Its low tones reverberate your entire body, filling you with a sorrow you didn’t know you were capable of feeling."

    "An impossibly long tendril appears from the void and slowly makes its way towards you. It gently wraps itself around you. You don’t even bother to question it at this point."

    show aradia oh with moveinbottom
    
    ara "wow"
    
    ara grin "on a scale of one to ten how shaken is your faith"

    "Why aren’t they here, Aradia? Where is everything."

    ara confused "i dont know"
    ara oh "but im here"
    ara "do you just want to vibe out with this space monster for a little while"
    ara talk "i kind of do"

    "Yeah. Ok. You guess."

    ara confused "i do not know where your friends are or why there isnt anything here"
    ara "and i am afraid you may not find these answers until you confront the puppetmaster"
    ara oh "but"

    "But...?"

    ara talk "isnt that fine?"
    ara "friends and grudges. life and death. existence and nothingness."
    ara "isnt it all the same in the end?"
    ara smile "the only th—"
    
    show aradia oh at bounce

    "If this is about bones you are going to lose your mind."

    show aradia smile
    
    "She smiles."

    ara amused "well i can confidently say it wasnt not about bones"

    "You can’t help but laugh a little bit."

    ara oh "do you want to try again"
    ara "i know there is a different way this goes"
    ara confused "but i still wanted to see what you would do"
    ara "you wont remember anything"
    ara amused "not even our friend here"

    "You think about it for a little bit. The tentacle sort of paps you on the face. Is it trying to comfort you?"

    "Eventually you know that's what has to happen. She will rewind you and tidy up the mess you’ve made by coming out here. There is a path you needed to follow and you keep trying to cheat it."

    "You ask her to let you sit here for a little bit longer. You don’t want to forget just yet."

    ara talk "ok"
    
    call ending pass ("gameover aradia2", False, True)

    return

    # $ renpy.pause(0.5)

    # $ quick_menu = False
    
    # stop music fadeout 1.0
    
    # scene gameover aradia2 with Dissolve(1.0)
    
    # show bg aradiavoid behind gameover
    # show aradia talk behind gameover

    # $ renpy.pause(15)
    
    # hide gameover with Dissolve(1.0)
    
    # $ renpy.music.set_volume(0.7, delay=0, channel='sound')
    
    # play sound "music/BE-KIND_RE-WIND.flac"
    
    # show aradia past smile:
    #     xpos 482 ypos 700 zoom 1.25
        
    # show bg aradiadigsite
    
    # $ renpy.movie_cutscene("ararewind2.mpg")
    
    # jump __p__aradiasecrets

