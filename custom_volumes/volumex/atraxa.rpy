label __p__atraxa:

    $ renpy.block_rollback()

    scene black with Dissolve(1.0)

    scene bg __p__atraxahive with dissolve

    $ quick_menu = True

    "...God, you're going to disappoint the fuck out of your folks back home. Or worse, impress them."

    "You've become civically engaged! And the wedding, or more accurately, the divorce from all your friends with differing opinions is tomorrow!"

    "Somehow the siren song of political action committees, and, of course, free I VOTED stickers -- provided Alternia has those -- has caught your attention something fierce."

    "After all, what better a way to make friends than to lose a bunch of them for BETTER more OPINIONATED friends? Ones who suggest how you dress, think, behave, and who you do or don't associate with."

    "...wow, this idea sounded so much better on the brochure and in your head reading what you skimmed from the brochure..."

    "Actually, come to think of it, you still have it."

    show __p__highlycursed with moveinright

    "...you know what, to be fair, the lady handing it out was pretty and very passionate. You couldn't NOT take one. Or pretend you wouldn't give your life to spread its message. Whatever that message is. Your mind was...somewhere else!"

    show __p__atraxa neutral with moveinleft
    play music "{{assets}}/music/imout.wav" loop
    show __p__atraxa neutral

    __p__teg "What are you? Some kind of mutant tro//? Or another sentient creature?"

    show __p__atraxa muhgun at bounce

    __p__teg "die seas scum!"

    show __p__atraxa muhgun2 at bounce

    "Definitely the latter, you say. Unless he would prefer the former, in which case you’re that, actually. But mutants, you’ve learned, are not particularly well-liked on this planet."

    __p__teg question "An a/ien... Hmph. I won’t have to cu// you, then. Not immediate/y, at /east. You don’t appear to be a cu//-on-sight species."

    show __p__atraxa proud at nod

    __p__teg "/ucky for you, that I won’t have to /oose my b/ade. And\n/ucky for me, to have found a potentia/ comrade."

    __p__teg question "I know what you seek."

    "Shelter and friendship, not necessarily in that order. You’re about to speak up, but he’s already moving on."

    __p__teg proud "You seek the meeting p/ace of the Eastern A/ternian Fine Animated Art Appreciation Society."

    __p__teg talk "Or, as some /ess-cu/tured sou/s wou/d ca// it – the\nanime c/ub."

    show __p__atraxa neutral

    "Oh, a club! Back home, teachers used to go on and on about how clubs were a wonderful place to meet new friends. You didn’t really believe it then, but maybe things are different here on Alternia."

    "You confidently assert that yes, you are here for the animes!"

    __p__teg pleased "Good."

    __p__teg proud "I feared I was going to have to cance/ tonight’s meeting due to no-shows, but now it can proceed as schedu/ed. Fo//ow me."

    show __p__atraxa movethenstop

    "He gestures toward his hive and begins to stride confidently toward it. But then he rethinks it, pausing to look back at you."

    __p__teg "Wait."

    __p__teg demanding "Subs or dubs?"

    menu:
        "[pick] Subs.":


            show __p__atraxa proud at nod

            __p__teg "Heh... It’s entertaining how wrong you are."

            __p__teg talk "But even the greatest of A/ternia’s phi/osofighters required sparring opponents on the batt/efie/d of the inte//ect."

            __p__teg proud "To cha//enge your assumptions with my superior /ogic and taste wi// be a fu/fi//ing task."

            __p__teg talk "Come in."

            "Not really the reaction you were hoping for, but you’d say anything to get into someone’s hive, so you’ll take it."
        "[pick] Dubs.":


            show __p__atraxa pleased at bounce

            __p__teg "Perfect. A fe//ow connoisseur."

            __p__teg "/et’s continue."
        "[pick] Um... both are good?":


            show __p__atraxa sour

            "His expression immediately sours, a look you’re all-too-familiar with. If you had a mouse, you’d be frantically scrolling the wheel upwards to roll back time and make a new choice."

            "But you live in the real world, where you have to face the consequences of your godawful anime opinions."

            __p__teg "Tch. Have you no conviction?"

            show __p__atraxa angry at bounce

            __p__teg "The anime c/ub is a sanctuary for those of strong wi// and fine/y-honed arguments, not a she/ter for coward/y pissants."

            __p__teg "What debate can come from a sycophantic toady such as yourse/f?"

            __p__teg demanding "How are you going to stimu/ate my inte//ect?"

            "You begin to sputter in protest. You’re plenty stimulating! You’ve got a pretty long list of friends who you’ve stimulated in all KINDS of ways. Platonic ones, mostly. But he’s not having any of it."

            __p__teg brood "There are other anime \"fans\" in this city. Perhaps their gatherings wi// be more your /eve/."

            __p__teg "Farewe//."

            hide __p__atraxa with moveoutright

            call ending ("__p__gameover atraxa1", False, True) from _call_ending_55

            return

    show bg __p__atraxahive with wiperight
    show __p__atraxa neutral at middle

    __p__teg neutral "/EX/cellent work, greenhorn. A job well done."

    show __p__atraxa proud at bounce

    __p__teg "Keep me posted if there are any further developments... .7v7"

    "You can't stop staring at that massive fucking monolith of regal hair. Is it just a thing for fiends to have an obscene amount of hair?"

    show __p__atraxa demanding

    __p__teg "Alas...it's my burden as a blueblood to bear, subtrollian freak...to care so little what others expect of me, and care so much what I /EX/pect of me."

    "...You're finding it difficult to honor this gal's wishes. You didn't even say that last bit aloud."

    show __p__atraxa question at bounce

    __p__teg "...Hm. So, hun, you know how I said keep your thoughts to yourself?"
    menu:
        "[pick] Yeah.":



            __p__teg brood shaking "Don't. Please. Just don't."

        "[pick] Nah.":


            show __p__atraxa pleased at bounce

            __p__teg "Perfect. A fe//ow connoisseur."

            __p__teg "/et’s continue."

    __p__teg "At least not where my beauty is concerned."

    show __p__atraxa talk at shaking 

    __p__teg "It's /criminally/ underappreciated. Blues /DESERVE/ to feel beautiful. Every other color gets positivity spoonfed to their ugly shades and overrated tints. Hgnnm..."

    show __p__atraxa demanding at bounce 

    __p__teg "Impressionable young /ceruleans/ and /indigos/ need to be told... there's a use in being blue! It really is okay, okay?!"

    "Okay."

    show __p__atraxa talk at shaking

    __p__teg "You can't shame the best there is for being great. I mean, take a look at rusties. Beautiful people. Tremendous. I love rusties. Nobody loves rustbloods better than me."

    show __p__atraxa brood at bounce

    __p__teg "I know everything about their kind."

    show teg demanding at bounce

    __p__teg "But alas... I'd never shake hands with one. You know why? Because I'm /forced/ to. We live in a /SOCIETY/ that's just so /CRUEL/ and /DUMB/ and /FORCES/ us to make friends with the lowest common denominators... "

    show __p__atraxa sour at bounce

    __p__teg "Now I /know/ what you're thinking!"

    "You don't doubt it."

    "Ceruleans seem to be a little lax on intellectual private property rights. Your thoughts are never guarded enough. And, for once, biased enough."

    "Especially around Miss. Anti-Integration here."

    show __p__gwylin neutral with moveinleft

    __p__czebe "SUCK MY FUCKING TOES, STATIST SCUM!"

    show __p__gwylin shocked at bounce

    "What the..."

    show __p__atraxa movethenstop

    __p__teg "NOT YOU /AGAIN/!"

    show __p__atraxa sourtoneutral

    "Oh. Fuck. That's not good."

    __p__teg "/Hemorealism/ is NOT the same thing as /hemoism/. Statistically speaking..."

    __p__teg "Rustbloods make up for 44 percent of the alternian populace's psychic related crimes and offenses, despite only taking up /18 percent/ of the total psychic population. That's like poisoning just under half a batch of grubsausage links..."

    show __p__atraxa demanding at shaking

    __p__teg "Statistics say that meat could be topped with death, mugging, or psionic assault. How /appetizing/."

    __p__teg "It's an uncomfortable truth... but truth doesn't feel bad about hurting your feelings, or tarnishing your world view."

    __p__teg "And uhhh... neither do I, honestly? I know I'm right. And deep down, you do too."

    __p__teg "Hemodiversity is just a barkbeast-whistle for blueblood genocide, if you /REALLY/ think about it."

    "You sure could use a source for those statistics, or a comprehensive explanation of just what a 'psychic crime' entails. Or if what Atraxa does counts. You wonder if she'd be this grumpy if she met some of your rust-friends..."

    "Maybe if she just spent a day in the shoes of -- "

    show __p__atraxa movethenstop

    __p__teg "I just don't /CARE/ for rustbloods... I never want you to think of me like that again."

    show __p__atraxa sourtoneutral

    "Oh. Fuck. That's not good."

    __p__teg talk "Per my viewing schedu/e, we’// watch a carefu//y curated se/ection of episodes from one c/assic, and from one recent re/ease."

    __p__teg question "But... hm..."

    __p__teg "Since you’re a newcomer, it might be best not to jump into the midd/e of /ast bout’s series, Phi/osopher Ha/f-Iron."

    __p__teg "Perhaps we sha//, instead, begin with the first season of Schoo/fed Heroism, and transition into some episodes of Kismet:Stuck Morning?"

    show __p__atraxa angry at bounce

    __p__teg angry "The origina/ airing, of course. Not the censored one with the ridicu/ous CGI dragon. Ugh."

    "Looks like atraxa intends to take full control of the morning’s activities, which you find entirely copacetic."

    "The less you need to assert your own opinions and make your own choices, the less likely you are to fuck up."

    "It’s probably not a healthy way to live, but it’s gotten you somewhere between one to nineteen friends so far, so you’re sticking to it."

    "With deft and precise movements, atraxa retrieves a disc from its container and pops it in the troll equivalent of a DVD player."

    "It makes a slimy, chugging noise as it sucks the disc in, and like usual, you aren’t sure if it’s an inanimate object or a living being. Either way, you’re a little disgusted."

    "The DVD player hums and atraxa’s TV lights up with a colorful title screen."

    "You’re ready to get settled in for a journey through the wonderful world of the animes, but he frowns and pauses the episode less than a minute in."

    __p__teg question "... Hang on."

    __p__teg "This isn’t the correct copy."

    __p__teg "The /oca/ization on these /ines was changed after the origina/ trans/ator was cu//ed by a purp/eb/ood for crimes against buffoonery."

    show __p__atraxa demanding at bounce

    __p__teg angry "I specifica//y ordered the first edition and paid extra for it. This is unacceptab/e!"

    "atraxa stops the DVD player, ejects the disc, and places it back in its case."

    __p__teg talk "Come. There’s sti// time in the night. We need to go reso/ve this immediate/y."

    __p__teg "The shop that imported it for me is nearby."

    show __p__atraxa neutral

    show bg hs_background3 with wipeleft

    "He heads for the door and beckons for you to follow, which you do. You guess it was too much to hope for a quiet morning inside, wasn’t it?"

    "At least you get to go shopping for animes, which sounds fun enough. Will it be at one of those fancy automated stores, you wonder?"

    __p__teg question "No. Un/ike most stores on A/ternia, this specia/ity shop is run by a /iving tro//."

    __p__teg "A fe//ow co//ector who wou/d not entrust such work to automation."

    show __p__atraxa angry at bounce

    __p__teg "So one wou/d EXPECT, with an actua/ think pan invo/ved, there wou/d be no care/ess mistakes /ike this."

    __p__teg question "At /east I’m on good terms with the owner, so I doubt there wi// be troub/e."

    "You, on the other hand, expect plenty of it. Pretty much everything on this goddamn planet has been trouble so far. Does he know how awful it is here? You don’t want to humansplain to him or anything, but things are pretty awful here."

    __p__teg sour "Things are pretty awfu/ here."

    "Oh. You guess he knows. He’s staring at one of the many billboards that line the streets, which has been defaced with bright red graffiti. It’s saying some pretty nasty stuff about Trizza."

    __p__teg "Hmph... Rebe/ sentiments grow by the moment."

    __p__teg brood "A/ternia /ies on the verge of peri/. A b/ade’s edge..."

    __p__teg "And not any b/ade, but the b/ade of a razor-sharp fo/ded stee/ katana."

    __p__teg "Forged under the East A/ternian moon/ight..."

    __p__teg "Heated by the be//ows-breath of a magnificent draconian\n/usus..."

    __p__teg "Coo/ed by the shimmering cascade of an acid waterfa//..."

    __p__teg "And fit to be hand/ed on/y by a true expert."

    show __p__atraxa dance at bounce

    __p__teg "Do you dance?"

    "You’re a little caught off-guard by that question. Dancing? As in... moving one’s body to music?"

    __p__teg question "In a way, yes."

    __p__teg pleased "Moving to the sweet music of stee/ on stee/, the rhythm of combat, the sti/etto step that weaves death and g/ory into one beautifu/ motion."

    show __p__atraxa talk at bounce

    "Oh. Swordfighting, of course. You really should have figured that one out. This guy’s dial has only two settings; talking about swords or talking about anime. Sometimes he gets particularly frisky and talks about both at once."

    "You tell him that you don’t know how to handle swords, but they seem really cool, and you’d love to learn."

    __p__teg question "Coo/?"

    show __p__atraxa sour at nod

    __p__teg "Feh."

    __p__teg dance "Swordp/ay is more than \"coo/\". It is a way of /ife. A code of honor."

    __p__teg "To pick up the b/ade is to bind yourse/f to the tenets of bushido, and to be prepared at a// times to enforce justice the on/y way a swordsman knows – through stee/."

    __p__teg talk "Someday, the pursuit of justice may bring me face to face with these rebe/ scum."

    __p__teg "I must be ready to show them the true, magnificent terror of the b/ade."

    __p__teg proud "Who knows? Maybe I wou/d even be awarded a\nc/owngressiona/ meda/ of honor."

    __p__teg "A tro// can dare to dream..."

    "So that’s why he practices swordplay, huh? To enforce justice, kind of like a vigilante?"

    __p__teg sour "Vigi/ante? P/ease."

    __p__teg question "I wou/d on/y ever cu// a tro// who /ega//y deserved death."

    __p__teg demanding "What kind of /aw/ess moron do you take me for?"

    "You don’t take him for a moron at all. In fact, he’s very smart and clever and just."

    show __p__atraxa proud at nod

    "You hope you’re not laying it on too thick, but he seems to enjoy the praise."

    __p__teg question "Ah. We’re here. This won’t take too /ong."

    "He’s taken you to a night market that reminds you of the place where you met Polypa. A strip mall lies to the left of the many tents and stalls, and a sign above one door reads, \"SUPER TOPATO IMPORTS.\""

    show bg atraxashop with wiperight
    show __p__atraxa neutral at left1280 with move

    "As you enter, atraxa makes a beeline for the counter, which is manned by a greasy looking goldblood with pinkish looking eyes."

    "You, on the other hand, are more interested in the rest of the store. It looks a lot like atraxa’s living room, but bigger."

    "Anime figurines on sale for what looks to be a preposterous amount of money, DVDs and comics lining the shelves, arcade games in the corner..."

    "There’s even a section for replica swords, which all look far too sharp and legitimately deadly for your liking."

    "Skulking between the shelves is an oliveblood guy. You can’t quite tell if he works here, or if he’s just browsing. You're not sure if any trolls even have normal jobs."

    show __p__atraxa demanding at bounce

    "You’re about to ask the olive guy about a particularly interesting DVD when you’re distracted by a commotion at the counter."

    show __p__atraxa at left1280 with move

    "You’re pretty sure you heard atraxa snarling something about his \"rights as a consumer\"? Looks like trouble is brewing. You turn your head toward the counter and listen in."

    __p__teg angry "Do you rea//y think you can get away with ripping me off\n /ike this? Do you know who I am? My b/ood caste?"

    __p__teg demanding "A tea/b/ood /ike me has connections. A vast network of /ikeminded sou/s at my beck and ca//, ready to be unsheathed against my hap/ess foes."

    __p__teg "The /ega/ force I can bring to bear against you is greater than your pueri/e mind cou/d ever imagine."

    __p__teg angry "A f/eet of /egis/acerators wi// descend on you /ike shadow c/ones, each armed with the greatest weapon of them a//: know/edge."

    __p__teg "And with our intricate understanding of the A/ternian /ega/ code, you wi// be mired in suits so myriad, so mind-numbing, you wi// wish for the swift and ear/y death my b/ade can provide."

    __p__teg brood "Or..."

    __p__teg demanding "You can offer me an exchange of equa/ or greater va/ue to my origina/ purchase!"

    __p__teg dance "Which path wi// you choose to wa/k, scum?"

    show __p__atraxa question at bounce with hpunch

    "You wander closer to the counter, hoping you might be able to help resolve the situation, but instead you blunder right into the oliveblood and send a box tumbling from his hands to the ground."

    "A bunch of assorted products spill out as the shopkeeper gasps dramatically. You don’t see what the big deal is. Looks like some more DVDs and manga."

    show __p__atraxa sour

    "One cover features a troll with heart-shaped horns and a bright pink sign, and another features some red-blooded douchebag wearing pants way too tall for him."

    "atraxa picks up one of the mangas and waves it in front of the shopkeeper’s face."

    show __p__atraxa demanding at bounce

    __p__teg "Care to exp/ain what I’m /ooking at here?"

    __p__teg "Imperia/ Dictate, Number the Second, Section Three point Two. The depiction of nonstandard hemo/ogica/ attributes is strict/y forbidden."

    __p__teg "Imperia/ Dictate, Number the Seventh, Section Five. Materia/ which encourages action against the state is considered contraband of the highest degree."

    "The oliveblood, who can clearly see the situation careening downhill like a scuttlebuggy without wheelstops, begins to creep toward the door."

    "You’d love to do the same, but you can’t give up on a potential new friendship. It’s basically pathological."

    __p__teg sour "Tch... To think that my favorite Eastern A/ternian hobby shop cou/d stoop so /ow as to pedd/e this crimina/ fi/th..."

    __p__teg "What a sickening betraya/."

    "The shopkeeper stammers, offering a litany of muddled explanations that only seem to incense atraxa further. He was holding it for a friend! No, wait, uh... it’s satire?"

    show __p__atraxa muhgun at bounce

    "atraxa slams a palm down on the counter and his eyes shoot open, revealing dark purple irises with a strange swirl pattern."

    __p__teg "Imperia/ Dictate, Number the Sixty-First, Section Two! Satire is especia//y contraband!"

    __p__teg "You think you can mess with me? I’ve watched count/ess hours of /ega/ drama. P/ayed and rep/ayed /egendary\n/egis/acerator and memorized every twist. I know the /aw back and forth."

    __p__teg dance "And now, it’s time for the punishment due. You’re fucking dead, kiddo."

    show __p__atraxa at middle with move

    "As atraxa leans over the counter, his free hand grips the hilt of his katana and tenses, ready to draw. He’s about to straight-up execute this guy."

    menu:
        "[pick] Don't intervene.":


            "You really don’t want to get in between the shopkeeper and atraxa’s sword. For all you know, this really does warrant an immediate execution. Who are you to judge?"

            "You do, however, squint a little so you don’t have to see the full, gory detail of the culling."

            show __p__speedlines
            show __p__atraxa muhgun2 at __p__slashing

            "Turns out, it’s not nearly as gory as you expected. atraxa leaps over the counter and swings wildly at the guy, but many of his attacks fail to connect."

            "It’s mostly a bunch of bombastic anime-style moves that don’t translate well to actual combat."

            show goldblood with hpunch

            "Still, some strikes hit home, drawing a spray of murky gold blood that jolts the shopkeeper out of his petrified fear."

            hide __p__speedlines
            show __p__atraxa sour at bounce with vpunch

            if persistent.flash:

                hide goldblood with pinkflash
            else:


                hide goldblood with slowpinkflash

            "He screeches and unleashes a strobing psionic blast from his eyes, causing atraxa to stagger back, disoriented."

            "The flash of light doesn’t seem to have caused any real damage, but it offers the perfect opportunity to flee; by the time your eyes have adjusted the only thing they see is the backdoor swinging wildly in his wake."

            "Unsurprisingly, the oliveblood is nowhere to be seen as well."

            __p__teg "Tch..."

            show __p__atraxa brood at shaking

            "atraxa glances down at his katana, stained with the blood of the shopkeeper, and slowly sheathes it. His hand is shaking, claws tapping the hilt restlessly."

            show __p__atraxa neutral at middle

            "He turns slowly to you, forcing himself back into his usual stoic posture."

            __p__teg talk "I... Uh..."

            __p__teg brood "He got /ucky, that’s a//. But he can’t hide forever."

            __p__teg question "/et’s go. We need to report this to a drone."

            show __p__atraxa neutral

            show bg hs_background3 with wipedown

            "He strides out of the shop, leaving you to follow hurriedly behind. What a mess. You hesitantly ask him whether it was really necessary to try and kill that boy for what he did."

            show __p__atraxa question at bounce

            __p__teg "O-Of course it was!"

            __p__teg talk "The /aw is abso/ute. A foreigner /ike you might not understand."

            __p__teg brood "It is not my duty to question the righteousness of my actions. I am but a too/ through which the /aw is enforced."

            __p__teg "I am the b/ade that Her Imperious Condescension wie/ds to maintain order in this wor/d of chaos."

            __p__teg talk "Just /ike this drone."

            show __p__atraxa neutral

            "He gestures to one of the big, hulking drones that you’ve grown all-too-familiar with during your stay here on Alternia. Right now, it looks like it’s cleaning up some bronze-colored blood that was spattered on the side of a building."

            show __p__atraxa talk at nod

            "atraxa approaches and hails it, beginning to explain that there’s a collector’s shop he needs to report for rebel activity. But the drone isn’t listening to any of that."

            show __p__atraxa question

            "It slowly turns from him to stare directly at you, and it raises its weapon to your face. A grating, electronic noise issues from its metallic grill. In the immortal words of a wise cartoon dog: ruh roh."

            show __p__atraxa demanding at bounce

            __p__teg demanding "Ho/d it!"

            __p__teg "This creature is under my protection. It has committed no crime."

            __p__teg dance "If you continue this attempted cu//ing, I wi// strike back with my katana."

            show __p__atraxa demanding at bounce

            __p__teg demanding "And... a strong/y worded /etter to your superiors!"

            show __p__atraxa neutral

            "The drone seems supremely annoyed that it can’t just get right down to culling a motherfucker, but atraxa’s caste must be just high enough to give it pause. You, the motherfucker in question, are incredibly relieved."

            "That relief quickly fades when the drone produces a palmhusk with a blurry picture of you on the screen, and a LOT of text beneath, most of it flashing red. That’s a never a good sign."

            "It looks like... A rap sheet."

            show __p__atraxa sour

            "atraxa reads through it quickly, which is a pretty impressive feat considering his eyes are still closed, and his expression darkens the further down he gets."

            __p__teg "Wanted under suspicion of meat product theft..."

            show __p__atraxa angry

            __p__teg "Wanted under suspicion of meat product theft... heist of fine art..."

            show __p__atraxa demanding at bounce

            __p__teg "Wanted under suspicion of meat product theft... heist of fine art... accomp/ice to the assassination of a vio/etb/ood??"

            show __p__atraxa muhgun at nod

            "Oof. You didn’t realize you’d racked up such a heavy list of crimes. He’s already rounding on you with fury radiating off every inch of his being. It’s terrifying. You’ve seen this guy arguing with a retail clerk. You know what he’s capable of."

            __p__teg "A// this time, I thought your sou/ was open to the way of the samurai."

            __p__teg "I thought I had met a potentia/ new connoisseur of the animated arts."

            __p__teg dance "But no..."

            __p__teg "Your b/ood pusher pumps on/y /ies through your vi//ainous veins."

            show __p__atraxa demanding at bounce

            __p__teg "You were just /ooking for an a/ibi... A p/ace to bide your time... To hide away from the drones unti/ it was time to indu/ge once more in your crimina/ ways!"

            "You try to defend yourself. You didn’t do any of those things! And you had a perfectly good reason for most of them!"

            show __p__atraxa muhgun

            "atraxa isn’t buying it. He’s clutching his katana’s hilt so tight, veins are bulging on his hand."

            __p__teg "Si/ence, coward."

            __p__teg "The time has come for my b/ade to strike true!"

            show __p__speedlines
            show __p__atraxa muhgun2 at bounce

            __p__teg "Hah!"

            with hpunch

            "He draws his blade in a smooth motion and swipes at you, and you just barely manage to sidestep the attack."

            hide __p__speedlines
            hide __p__atraxa
            with moveoutright

            "You dart backwards, stumbling over yourself in your haste to get away, while he swings his katana wildly around while making lots of weird grunting noises."

            "Once again, his mouth has been writing a check his sword hand can’t cash, but you doubt that matters when trolls are stronger and faster than you in general, and he’s accompanied by a giant murderdrone."

            "It’s time for you to split, and you’d better do it lickety."

            "Glancing around, you notice that you’re about to cross over a bridge, with an underpass beneath it. Perfect! Just like an action hero you can hop right over the edge of the road, duck into the underpass, and find a nice hiding spot."

            "You dash toward the traffic barrier, vault nimbly over it, and {i}oh jesus piss this is way higher than you thought it was.{/i}"

            with vpunch

            if persistent.flash:

                with Fade(0.04, 0.5, 0.5, color="#ffffff")

            "You hit the ground hard with a resounding crack, and for a moment your vision goes blank as a wave of pain sears your nerves."

            "As the pained disorientation begins to fade, you decide it’s about time to take stock of your situation."

            "A couple of broken bones (old hat), a troll trying to kill you (not unfamiliar), drones attacking you (same) and sun about to rise and scorch you into nothing (again)."

            "Individually, you’ve risen to the challenge of just barely handling each of these problems. But all at once? Yeah, you think you’re just gonna call this one here."

            call ending ("__p__gameover atraxa2", False, True) from _call_ending_56

            return
        "[pick]Defend the shopkeeper.":


            "Okay, you know this is a terrible idea, but you’ve seriously had it up to here with being party to the murder of random trolls."

            show __p__atraxa question

            "You quickly interpose yourself between atraxa and the goldblood. Does he really have to kill this guy? For what seems to be his first offense?"

            "You launch into an impassioned spiel about LOVE and FRIENDSHIP and JUSTICE, riding the value of forgiveness and second chances really hard."

            "And, for good measure, you throw in a little side note about how atraxa’s favorite shop will close down if he kills this dude."

    __p__teg sour "Si/ence."

    with hpunch

    "atraxa shoves you roughly aside and you go careening into a display full of body pillows."

    show __p__atraxa muhgun

    "You watch, stomach plummeting, as __p__atraxa turns back to the shopkeeper and slowly draws his sword."

    show __p__atraxa neutral at bounce

    "But then, at the last second, he reconsiders."

    __p__teg "..."

    show __p__atraxa at shaking

    __p__teg "............"

    show __p__atraxa sour at middle

    __p__teg "... Ugh. Consider yourse/f /ucky I’m in a good mood."

    __p__teg "If I catch you se//ing contraband again, your /ife wi// be mine."

    show bg hs_background3 with wipedown

    "atraxa strides out of the store, holding a fresh copy of the DVD he wanted to exchange. You give the shopkeeper a vaguely apologetic look and rush out of the store behind him."

    "Whew! That was a close one. You thank atraxa profusely for listening to your dumb little speech about... whatever it was you said. Honestly, you already forgot."

    __p__teg question "You’re c/ear/y new to this p/anet. I fe/t... pity, for your naivete."

    __p__teg sour "But I shou/d have just ki//ed him."

    __p__teg "Death is the /ega//y-prescribed punishment for such crimes as his."

    __p__teg question "Actua//y... it’s the /ega//y-prescribed punishment for most crimes."

    __p__teg "I shou/d have separated him from his head."

    __p__teg talk "But I /ooked into your p/eading eyes, and I saw..."

    __p__teg brood "I saw........."

    "atraxa goes quiet. You would describe the silence as being particularly brooding. There’s a lot of silences like that on this planet. Then, finally, he speaks:"

    show __p__atraxa at nod

    __p__teg "This... isn’t my first time."

    __p__teg question "It was just over a sweep ago, I be/ieve. I was patro//ing the hivebatch in search of evi/doers when I caught the unmistakab/e scent of smoke in the air."

    __p__teg "Upon pursuing the /ead I saw a hive, partia//y co//apsed, partia//y on fire. My instincts f/ared, and I rushed in to he/p the innocent sou/ who was trapped there."

    __p__teg talk "But as I was he/ping the gir/ bandage her wounds, it occurred to me that I had made a grievous error in judgment."

    __p__teg question "Tro//s be/ow a certain age without a /usus, or a proper hive, are considered unviab/e and s/ated to be cu//ed."

    __p__teg talk "By rights I shou/d have put her out of her misery, the moment I rea/ized my mistake."

    __p__teg "And yet..."

    __p__teg question "I /ooked into her deep grey eyes, du//ed from the pain of\n/oss, and I sheathed my b/ade."

    __p__teg "In fact... Even though she is hive/ess and /usus/ess, I remain in contact with her to this day."

    __p__teg talk "Knowing deep down that one day, I must cu// her. The /aw demands it."

    __p__teg "But I haven’t yet."

    __p__teg brood "I don’t know if I cou/d..."

    __p__teg "Why does my conviction waver at times /ike these?"

    "If he’s talking about who you think he’s talking about, you’re pretty sure he couldn’t kill her even if he tried."

    "But that’s not the point here. The point is, he’s spilling some REAL and TRUE and DEEP emotion with you!"

    "This friendship is basically in the bag. Just gotta drop some sweeping, vague wisdom that makes him feel better about potentially not being an unthinking cog in the Alternian murder machine."

    "You offer a light suggestion that maybe, what is legal and what is just... aren’t always the same thing? Just a little thought."

    "Maybe he’s doing the right thing, overlooking her situation because of how obviously fucked up it is to be a homeless orphan."

    "He goes silent for a long time, chewing his bottom lip."

    show __p__atraxa sour at bounce

    __p__teg "Feh. You’re naïve."

    __p__teg "Naïve, uncu/tured, unen/ightened."

    "Wow, thanks!"

    __p__teg talk "You think the wor/d is simp/e. /ike a cartoon for chi/dren."

    __p__teg angry "But this is A/ternia, a /and ru/ed by co/d /ogic, where men such as myse/f must make the hard decisions."

    __p__teg talk "It’s not easy, being dedicated to the code of /aw."

    __p__teg "It asks much of us and gives us /itt/e in return. But it gives us order. It keeps the beasts at bay."

    __p__teg "If I were to question it, what then?"

    __p__teg angry "Wou/d I begin to wonder if it is unjust for a b/ueb/ood to command his servants? For imperia/ drones to cu// the infirm? For us to obey the ever-changing whims of the A/ternian roya/ty?"

    "It takes a lot of effort to suppress your \"well, yeah\", but for the sake of this burgeoning friendship, you allow him to continue his monologue."

    __p__teg talk "Riots in the streets. Tro// ki//ing tro//. Even more than usua/, I mean."

    __p__teg "No. I cannot waver."

    __p__teg dance "These hands must remain steady and true. Though I fee/ a pu// toward the scorching fangs of the /ight, I must continue my path and remain in the tender, righteous embrace of the dark."

    __p__teg "Truth be my b/ade, inte//ect my sensei, and justice my on/y companion on this /one/y road."

    "He goes on like that for quite a while. It all starts to muddle together in your head, and you lose count of how many times he’s repeated some screed about justice and truth and being smarter than all the other trolls in the room."

    "It honestly sounds to you like he’s just... lonely?"

    "You know a whole lot about loneliness, and the poor management thereof."

    "Some people throw themselves into their nerdy anime hobby, and others become obsessed with making friends no matter the cost to their mental or physical wellbeing."

    "Maybe he just needs a couple of good pals to remind him what it’s like to have a heart."

    "But if you try to tell him that, he’ll probably just respond with another long and winding monologue, likely stolen from an anime he watched recently. Maybe you should just let him vent."

    __p__teg question "You have my thanks for /ending your ear."

    "Oh! A compliment brings you out of your reverie. Nothing interrupts the ol’ introspection machine like the opportunity to chug on the succulent ambrosia that is any kind of praise or gratitude."

    "It’s no big deal, you tell him. You’re a great listener! That’s what friends are for. Has he considered having more friends? Like you, for example?"

    show __p__atraxa neutral

    "He opens his mouth like he’s about to reiterate the whole \"lone swordsman\" thing, so you hastily try to change the topic. What’s with his eyes?"

    "Most trolls you’ve seen have had grey irises, and those who didn’t followed the typical biological trend of displaying their blood color."

    show __p__atraxa sour

    "atraxa pauses, his grip tensing on his sword as his fangs dig into his lip. Oh jeez. This must be his most closely guarded secret. Have you earned enough trust to hear it...?"

    __p__teg question "They’re contact /enses, for cosp/ay."

    "Oh."

    "Fair enough."

    show __p__atraxa neutral

    "Actually, is cosplaying as a different blood caste even legal on this planet? If he's doing it, it probably is... right?"

    "You’re about to ask when something distracts you – the sight of another troll standing in front of atraxa’s hive, using it as shelter from the rising sun."

    "They’re pacing back and forth with precise movements, glancing at one of the windows almost like they’re plotting to break in."

    "And when they hear footsteps approaching, they perk up and whirl their head around—"

    "Hey, wait a second. You recognize them!"

    show __p__atraxa neutral at left1280 with move

    show polypa neutral at right1280 with moveinright



    "Polypa spots you before atraxa spots her. Her expression is hard and stoic, eyes glancing between the two of you as she assesses the situation."

    show polypa pleased

    "And then, like she’s throwing on a disguise, her face softens and she smiles."

    show polypa at speaking

    polypa "hey tegs*|"

    polypa "i was starting to wonder * where you were * and if anime night was cancelled *|"

    polypa neutral "your lusus * is staring at me through the window * i think he thinks it’s funny * watching me stuck outside *|"

    polypa "roasting to death * while you’re chasing purrbeasts around the hivebatch *|"

    show polypa at stopspeaking

    show __p__atraxa proud at speaking

    __p__teg "Heh. C/assic Tadashi."

    __p__teg talk "Why were you /ate?"

    show __p__atraxa at stopspeaking

    show polypa at speaking

    polypa "just busier than expected * with some work *|"

    show polypa serious at stopspeaking

    "She shoots you a sharp glance."

    show polypa pleased at speaking

    polypa "assembling some new mecha models *|"

    polypa "you know how it is *|"

    show polypa at stopspeaking

    show __p__atraxa question at speaking

    __p__teg "Yes, of course. It’s a// too easy to get wrapped up in one’s hobby."

    show __p__atraxa neutral at stopspeaking

    show polypa neutral at speaking

    polypa "anyway * i didn’t realize we’d have a third * for once *|"

    polypa pleased "not to mention * somebody i know *|"

    show polypa at stopspeaking

    show __p__atraxa question at speaking

    __p__teg "Nani?? You and my new kohai have a/ready met?"

    show __p__atraxa at stopspeaking

    show polypa neutral

    "She pauses, her eyes darting back and forth between you two once more."

    "She seems to be assessing the situation, wearing a look like an assassin trying to evade capture. You recognize that look, considering she was literally wearing it the last time you met."

    show polypa neutral at speaking

    polypa "we’re kinda * moirails *|"

    show polypa at stopspeaking

    "Whoa! That’s absolutely not what you thought you were, but you just kind of nod your head and roll with it. It seems to be what she wants you to do."

    show __p__atraxa talk at speaking

    __p__teg "Oh. Moirai/s."

    show __p__atraxa sourtoneutral at stopspeaking

    "atraxa’s face tightens almost imperceptibly, but you caught it. Nothing gets past your honed friendmaking eyes."

    "Well, actually, a lot of things get past them, but not this particular thing."

    "You’re finely tuned to the nuances of social situations, as long as those nuances don’t involve making a binary choice on which your social future hinges."

    show __p__atraxa talk at speaking

    __p__teg "We//."

    __p__teg dance "As you know, I am far too busy studying the b/ade to pursue quadrants of any sort."

    __p__teg "A foo/ish waste of time. Were it not for the /aws of this\n/and, I wou/d swear off them entire/y."

    show __p__atraxa neutral at stopspeaking

    show polypa pleased at speaking

    polypa "are you sure it isn’t * that you just can’t get a date *|"

    polypa neutral "you don’t have to play the mysterious loner * you know *|"

    polypa pleased "there’s other clubs you could join * instead of insisting on running your own *|"

    show polypa at stopspeaking

    show __p__atraxa sour at bounce

    "He huffs, looking away. You hear his lusus barking from behind the window, in a tone that sounds like laughter."

    show __p__atraxa question at speaking

    __p__teg "Foo/s mock that which they cannot understand."

    __p__teg talk "And to think, I was going to congratu/ate you on finding\n/ove."

    show __p__atraxa neutral at stopspeaking

    show polypa pleased at speaking

    polypa "once you finished your spiel * about romance being dumb *|"

    show polypa at stopspeaking

    show polypa at __p__whap

    show __p__atraxa pleased

    "Polypa gives him a light, friendly whap, which he responds to with a smile. You can tell the exchange is friendly not only because he’s smiling, but because he’s still standing."

    show __p__atraxa pleased at speaking

    __p__teg "Enough banter."

    __p__teg proud "The harsh g/are of the sun begins to crest, and we have Eastern A/ternian animation to indu/ge in."

    __p__teg pleased "I’// a//ow you both to spend the day at my hive, if needed. There’s space."

    show __p__atraxa neutral at stopspeaking

    "Oh shit. A slumber party? And with more than one participant, even? That’s got to be worth extra friend points. You are so in."

    "Shelter from the broiling death orb in the sky barely even registers to you as an added bonus."

    "Polypa smiles at you as the three of you enter atraxa’s hive."

    show bg __p__atraxahive with wiperight
    show polypa at middle with move
    show __p__tadashi end with moveinright

    show __p__darken

    "atraxa covers up all of his windows to block out the sun, and then starts up the new copy of his DVD, which thankfully seems to meet his standards this time."

    "You settle in on the couch, basking in the warm glow of friendship, and prepare to lose yourself to hours of the beautiful wonderful animes."

    call ending ("__p__victory atraxa", True, True) from _call_ending_57

    return
