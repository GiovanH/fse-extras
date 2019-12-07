label __package_entrypoint___volumex:

    $ renpy.block_rollback()

    $ main_menu = False

    show expression "gui/game_menu.png"

    window hide

    scene black with Dissolve(1.5)

    op "The following is a {=friend}FAN-BASED{/friend} mod project."

    op "Homestuck, Hiveswap, Friendsim, and the Friendsim IP are all owned by WhatPumpkin LLC. Please support the official release."

    op "Like, no, seriously."

    op "This won't even run without it. Be a {=friend}FRIEND & FAN{/friend} on behalf of fans  & friends."

    op "Thank you."

    op "..."

    play music "{{assets}}/music/Ergo_Phizmiz_-_10_-_Smoke_Animals.wav"

    op "Things have been pretty shitty lately, you're not going to lie."

    op "Around this time of year you'd probably be procrastinating an overdue art-meme. Or testing the upper limits of your body's abjuring."

    op "Or saying thank you for something other than physical violence that doesn't remove one or more of your limbs."

    op "Maybe even playing part one of a videogame programmed by a dog or some crazy shit like that."

    op "Hell, anything's better than being left to your not-cursed, not-magical, not-enchanted-or-special-in-any-way-existential-thoughts."

    op "It's truly been the Hallowed-Hack season for friend and {=friend}fiend{/=friend} alike."

    op "To everyone except for you."

    op "..."

    op "Maybe that's why things have been so shitty."

    op "You have too many friends."

    op "You're sure none of them would mind if you were to impose, but if you screw it up, or say the wrong thing..."

    op "Well, that's the bad ending."

    op "You're never the type to {=friend}PESTER CHUMS{/=friend}."

    op "So why not flirt with the unknown for a change?"

    show __p__shady

    op "Why not get {=friend}SPOOKY?{/=friend}"

    stop music

    show __p__shady2

    call screen __p__trollselect with Dissolve(1.0)

    with Pause(0.25)

    return

