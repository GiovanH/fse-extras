init offset = 1

# Define characters


define !jo = Character(name="ectoBiologist", kind=pesterchum, what_color='#0715cd', image="john")

# Different ways to namespace names:
# Defines can use dots
# "!" is the preferred prefix for character defines and other areas where dot namespaces are accepted.
# But it can't be used inside quotes or parameters.
# "__p__" is also acceptable, and can be used in all contexts
define !vr = Character(name="arachnidsGrip", kind=trollian, show_blood="cerulean", image="vriska")

define !bo = Character(name="BOLDIR", kind=hiveswap, image="boldir", show_blood="olive")

# Using dots in the namespace is optional, and only works for defines.
define !tz = Character("[tztitle]", kind=trollian, show_blood='teal', image="!terezi")

# Give characters poses
# image vriska neutral3 = Image("images/Vriska_Neutral_3.png", ypos=730, xanchor=640, yanchor=730)
# Because this is an image, you can't use the "!" shorthand: Use "__p__" instead.
image vriska __p__ngreen = Image("{{assets}}/Vriska_Green.png", ypos=730, xanchor=640, yanchor=730)
image !terezi neutral = Image("{{assets}}/terezi.png", ypos=730, xanchor=640, yanchor=730)

# Define backgrounds
# image bg johnroom = im.Scale("images/john_s room.png", 1300,730)

# Define other graphics, end cards
image !fakemenu = "{{assets}}/fakemenu.png"
image !vriskaend = "images/vriska_endcard_badend1.png"
image !fakemenu = "{{assets}}/fakemenu.png"

define !mituna = quirkSayer(Character("Mituna", screen="chan_say"), "greentext")

# ob_meulin is already defined; define a new copy using the openround style
# Because this is used as a kind, you can't use the "!" shorthand: Use "__p__" instead.
define __p__befriendus = Character(
    kind=openround,
    namebox_xanchor=0.5, namebox_yanchor=1.0, namebox_ypos=14, # Position the namebox askew
    say_dialogue_yoffset=-27, # shift box up
    show_use_nameframe=True, # Frame the name in a box
    show_hashtags=" " # By default, show a blank hashtag)
)
define !meu2 = Character(
    name="MEULIN", show_blood="olive", kind=__p__befriendus, image="ob_meulin", 
)

image !karako grype happy = GrypeMasked("__p__karako happy")
image grype_frame !karako = GrypeFrame(
        handle="arachnidsGrip",
        blood="cerulean", 
        avatar="{{assets}}/vriskagrype.png"
    )
image grype_frame !karako2 = GrypeFrame(
        handle="arachnidsGrip",
        blood="#646464", 
        avatar="{{assets}}/vriskagrype.png"
    )

# Start of route
# Start of route should always be named like this, where sandbox is replaced
# with your volume_id.
label __package_entrypoint___sandbox:

    # Menu boilerplate: Exit main menu, fade to black
    $ renpy.block_rollback()
    $ main_menu = False
    show image "gui/game_menu.png"
    window hide
    scene black with Dissolve(1.0)
    show blackcover
    $ quick_menu = True

    # Set the scene, fade in from black
    scene fs_bg background_spaceship with Dissolve(0.6)


    # Helper for rewind
    "rollback"

    "achieve"

    $ achievement.grant("__p__test")

    "achieved"
    show !karako happy at default
    "Happy" 
    show !karako happy blank
    "Happy blank"
    show !karako happy grateful
    "Happy grateful"
    show !karako happy block
    "Happy block"
    show !karako happy same
    "Happy same"

    show !karako happy at bounce
    "Bounce"
    show !karako happy at bounce(50)
    "Bounce 30"
    show !karako happy at bounce(repeat=2)
    "Bounce twice"
    show !karako happy at bounce(pause=0, repeat=2)
    "Bounce twice quick"

    hide !karako

    show ob_mituna idle
    !mituna "Fuck"
    !mituna ">tfw no greentext\nwait ah no shit"
    !mituna "Attachment" (show_attachment="{{assets}}/vriskagrype.png")
    !mituna "Attachment" (show_attachment="gui/game_menu.png")
    !mituna "Attachment" (show_attachment="{{assets}}/Vriska_Green.png")
    !mituna "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque at feugiat eros, nec rhoncus velit. Nullam nunc est, semper id justo sit amet, laoreet congue tortor. Etiam scelerisque lacinia elit, eu mollis magna efficitur nec. Aliquam cursus tristique elit, vel facilisis nibh congue vitae. Interdum et malesuada fames ac ante ipsum primis in faucibus."
    !mituna "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque at feugiat eros, nec rhoncus velit. Nullam nunc est, semper id justo sit amet, laoreet congue tortor. Etiam scelerisque lacinia elit, eu mollis magna efficitur nec. Aliquam cursus tristique elit, vel facilisis nibh congue vitae. Interdum et malesuada fames ac ante ipsum primis in faucibus." (show_attachment="{{assets}}/vriskagrype.png")
    hide ob_mituna
    # Grype
    show grype_frame !karako
    show !karako grype happy 
    !vr "Bitch."
    show grype_frame !karako2
    !vr "im gray now"
    hide !karako 
    hide grype_frame

    show ob_meulin idle
    ob_meulin idle "Color by color" (show_blood="#0A0")
    ob_meulin idle "Color by blood" (show_blood="candyred")
    ob_meulin idle "!!"
    ob_meulin laugh "!!!" (show_hashtags="#hashtag1")
    ob_meulin laugh "!!!" (show_hashtags="#hashtag1\n#multiline")
    ob_meulin hypno "A very spooky bit of text which reads about three lines at this size" (show_chuckle=True)
    ob_meulin hypno "spoop" (show_chuckle=True, show_hashtags="#HONK")

    !meu2 idle "!!"
    !meu2 laugh "!!!" (show_hashtags="#hashtag1")
    !meu2 hypno "HONK" (show_chuckle=True)
    !meu2 hypno "spoop" (show_chuckle=True, show_hashtags="#HONK")
    hide ob_meulin

    # Test dialogue systems
    # Compare our dialog systems against the vanilla ones
    # to ensure everything matches up
    !bo "Boldir custom"
    !vr "Custom vriska"
    !jo "Custom john"
    ob_meulin "Custom openbound"

    # Make absolutely sure the preprocessor isn't modifying dialogue
    "My quirk is weird and I exclaim wrong !it's weird"
    op "My quirk is weird and I exclaim wrong !it's weird"
    !vr "My quirk is weird and I exclaim wrong !it's weird"



    # Trollian multiline test
    show !karako happy blank
    !vr "Hi! I'm vriska\nLines are loose"
    !vr "Hi! I'm vriska, but busy.\nMultiple lines are tight." (show_big=True)
    
    # Trollian colorizing
    !vr "Override" (show_blood="#0A0")
    !vr "Gray" (show_blood="gray")
    !vr "Candy red" (show_blood="candyred")
    !vr "burgundy" (show_blood="burgundy")
    !vr "Bronze" (show_blood="bronze")
    !vr "Gold" (show_blood="gold")
    !vr "Lime" (show_blood="lime")
    !vr "Olive" (show_blood="olive")
    !vr "Jade" (show_blood="jade")
    !vr "Teal" (show_blood="teal")
    !vr "Cerulean" (show_blood="cerulean")
    !vr "Indigo" (show_blood="indigo")
    !vr "Purple" (show_blood="purple")
    !vr "Violet" (show_blood="violet")
    !vr "Fuchsia" (show_blood="fuchsia")
    hide !karako

    # Hiveswap colorizing
    show fs_boldir neutral
    !bo "Default"
    !bo "Override" (show_blood="#0A0")
    !bo "Test" (show_blood="test")
    !bo "Gray" (show_blood="gray")
    !bo "Candy red" (show_blood="candyred")
    !bo "burgundy" (show_blood="burgundy")
    !bo "Bronze" (show_blood="bronze")
    !bo "Gold" (show_blood="gold")
    !bo "Lime" (show_blood="lime")
    !bo "Olive" (show_blood="olive")
    !bo "Jade" (show_blood="jade")
    !bo "Teal" (show_blood="teal")
    !bo "Cerulean" (show_blood="cerulean")
    !bo "Indigo" (show_blood="indigo")
    !bo "Purple" (show_blood="purple")
    !bo "Violet" (show_blood="violet")
    !bo "Fuchsia" (show_blood="fuchsia")
    hide boldir

    # Pesterchum and multilines
    show john neutral
    !jo "Hi! I'm john\nLines are loose"
    !jo "Hi! I'm john, but busy.\nMultiple lines are tight." (show_big=True)
    hide john

    # Test our supplemental narrators, characters
    flarp "Flarp instructions."
    narrator_prattle "Generic prattle"
    narrator_dirk "Some ultimate dirk narration."
    narrator_calliope "Narrator calliope"

    # Openbound: Use parameters for effects.
    show ob_meulin idle
    ob_meulin idle "Color by color" (show_blood="#0A0")
    ob_meulin idle "Color by blood" (show_blood="candyred")
    ob_meulin idle "!!"
    ob_meulin laugh "!!!" (show_hashtags="#hashtag1")
    ob_meulin hypno "A very spooky bit of text which reads about three lines at this size" (show_chuckle=True)
    ob_meulin hypno "spoop" (show_chuckle=True, show_hashtags="#HONK")

    !meu2 idle "!!"
    !meu2 laugh "!!!" (show_hashtags="#hashtag1")
    !meu2 hypno "HONK" (show_chuckle=True)
    !meu2 hypno "spoop" (show_chuckle=True, show_hashtags="#HONK")
    hide ob_meulin

    # Music notifications. 
    # See full implementation in sys/fx.rpy
    # By default, shows a notification and hides itself.
    show screen MusicToast()
    "Drink it in"

    # ...although you do need to hide it yourself eventually
    # if you want things to work right, even if you use the autohiding versions. 
    hide screen MusicToast

    # Set albumart, title, artist, and album fields to your data.
    # Set tf to toast_down instead of toast_down_peek to make the notification stick on the screen.
    # You can use tags here like other text.

    # Advanced:
    # You can supply an arbitrary transofmration to the tf parameter
    # You can style the entire window using stule=x
    # You can edit the template form strings using ttitle, tartist, and talbum
    # You can edit the size of the album art using albumartsize
    show screen MusicToast(
        tf=toast_down,
        albumart="{{assets}}/scourgequest.jpg",
        title="Let Me Tell You About (Instrumental)",
        artist="Flutterwhat",
        album="{a=https://flutterwhat.bandcamp.com/track/let-me-tell-you-about-insturmental}ScourgeQuest{/a}")
    
    "Drink it in {i}forever{/i}"
    # After *something*, hide the notification, if you used something like toast_down to make it stick.
    # Something that uses toast_down or toast_up will use the toast animation to hide the window.
    hide screen MusicToast

    "and I guess let it leave before bringing in the next thing"

    

    # Test extended choice screen

    menu:
        "[pick] pick1":
            pass
        "[pick] pick2":
            pass
        "[pick] pick3":
            pass

    menu (screen="choice_scrollable"):
        "[pick] pick1\nline2":
            pass
        "[pick] pick2\nline2":
            pass
        "[pick] pick3\nline2":
            pass
        "[pick] pick4\nline2":
            pass
        "[pick] pick5\nline2":
            pass
        "[pick] pick6\nline2":
            pass
        "[pick] pick7\nline2":
            pass
        "[pick] pick8\nline2":
            pass
        "[pick] pick9\nline2":
            pass

    show screen MusicToast(tf=toast_flyby)
    "Is this even a toast anymore?"
    hide screen MusicToast

    # Different approaches to quirk formatting
    show gamzee neutral1

    # Approach 1: Call quirksay
    # Arguments are sayer (character), quirk name, text
    $ quirkSay(gam, "gamzee", "Quirk formatting 1")

    # Approach 2: Define a new sayer
    # Define a new character, given an existing character and a quirk
    # New sayer is reusable!
    $ __p__gamq = quirkSayer(gam, "gamzee")
    !gamq "Quirk formatting 2"
    !gamq "Quirk formatting 2 forever"

    # Approach 3
    # You can quirk format text without saying it directly
    $ __p__tmp_text = quirkSub("gamzee", "Quirk formatting 3") + " and I guess other stuff"
    gam "[__p__tmp_text]"
    hide gamzee

    show !karako happy blank
    !vr "I'm 8riska"
    hide !karako

    show !terezi neutral
    # play music "music/fs_BOLDIR.wav" loop
    hide blackcover with dissolve

    # Test dynamic name growth
    $ tztitle = "A"
    !tz "1"
    $ tztitle = "AAAAAAAAAAAA"
    !tz "2"
    $ tztitle = "AAAAAAAAAAAAAAAAAAAAAAAAAAA"
    !tz "3"
    $ tztitle = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
    !tz "4"

    # Twitter demo
    !tz neutral "Hey. Hey. Over here."

    "Oh shit. You’re just standing out here with all his mail, he’s going to think you’re trying to rob the place."
    menu:
        "Oh shit. You’re just standing out here with all his mail, he’s going to think you’re trying to rob the place.{fast}"

        "[pick] Play it cool":
            pass
        "[pick] Hide the evidence":
            pass

    show !fakemenu
    !tz "UHHHHHHHH"

    show !terezi at right1280 with ease
    !tz "*SNIFFFFFFFF*"

    show !terezi at left1280 with move
    !tz "TF 1S TH1S TH1NG :?"

    hide !terezi
    hide !fakemenu

    show !karako happy

    # Write dialogue!
    !karako happy "Hey. Hey. Over here."
    vr __p__ngreen "8itch."

    hide !karako  # goodbye

    # You can use assets that have already been definied in other pesterquest routes directly!
    show bg gamzeehive
    show gamzee pie1
    gam pie1 "cAn I oFfEr YoU a PiE iN tHeSe TrYiNg TiMeS"
    # Be careful about naming your resources so they don't conflict with other ones. 
    # I help where I can by offering the substitutions like {{package_id}}.

    # Show end card
    call ending pass ("!vriskaend", True, True)
    return
