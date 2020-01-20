init offset = 1

# Define characters


# Different ways to namespace names:
# Defines can use dots
define __p__.jo = Character(name="ectoBiologist", kind=pesterchum, what_color='#0715cd', image="john")
# define __p__.jo = Character(kind=pesterchum,  what_color='#0715cd', image="john")

# "!." is the preferred prefix for character defines and other areas where dot namespaces are accepted.
# But it can't be used inside quotes or parameters.
define !.vr = Character(name="arachnidsGrip", kind=trollian, show_blood="cerulean", image="vriska")

# "__p__" is also acceptable, and can be used in all contexts
define __p__.bo = Character(name="BOLDIR", kind=hiveswap, image="boldir", show_blood="olive")

# Using dots in the namespace is optional.
define __p__tz = Character("[tztitle]", kind=trollian, show_blood='teal', image="__p__terezi")

# Give characters poses
# image vriska neutral3 = Image("images/Vriska_Neutral_3.png", ypos=730, xanchor=640, yanchor=730)
image vriska __p__ngreen = Image("{{assets}}/Vriska_Green.png", ypos=730, xanchor=640, yanchor=730)
image __p__terezi neutral = Image("{{assets}}/terezi.png", ypos=730, xanchor=640, yanchor=730)

# Define backgrounds
# image bg johnroom = im.Scale("images/john_s room.png", 1300,730)

# Define other graphics, end cards
image __p__fakemenu = "{{assets}}/fakemenu.png"
image __p__vriskaend = "images/vriska_endcard_badend1.png"
image __p__fakemenu = "{{assets}}/fakemenu.png"

define !mituna = quirkSayer(Character("Mituna", screen="chan_say"), "greentext")

# ob_meulin is already defined; define a new copy using the openround style
define __p__befriendus = Character(
    kind=openround,
    namebox_xanchor=0.5, namebox_yanchor=1.0, namebox_ypos=14, # Position the namebox askew
    say_dialogue_yoffset=-27, # shift box up
    show_use_nameframe=True, # Frame the name in a box
    show_hashtags=" " # By default, show a blank hashtag)
)
define __p__.meu2 = Character(
    name="MEULIN", show_blood="olive", kind=__p__befriendus, image="ob_meulin", 
)

image !vriska grype neutral = GrypeMasked("vriska neutral1")
image grype_frame __p__vriska = GrypeFrame(
        handle="arachnidsGrip",
        blood="cerulean", 
        avatar="{{assets}}/vriskagrype.png"
    )
image grype_frame __p__vriska2 = GrypeFrame(
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
    scene bg spaceship with Dissolve(0.6)

    # Helper for rewind
    "rollback"

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
    show grype_frame __p__vriska
    show !vriska grype neutral 
    !.vr "Bitch."
    show grype_frame __p__vriska2
    !.vr "im gray now"
    hide !vriska 
    hide grype_frame

    show ob_meulin idle
    ob_meulin idle "Color by color" (show_blood="#0A0")
    ob_meulin idle "Color by blood" (show_blood="candyred")
    ob_meulin idle "!!"
    ob_meulin laugh "!!!" (show_hashtags="#hashtag1")
    ob_meulin laugh "!!!" (show_hashtags="#hashtag1\n#multiline")
    ob_meulin hypno "A very spooky bit of text which reads about three lines at this size" (show_chuckle=True)
    ob_meulin hypno "spoop" (show_chuckle=True, show_hashtags="#HONK")

    __p__.meu2 idle "!!"
    __p__.meu2 laugh "!!!" (show_hashtags="#hashtag1")
    __p__.meu2 hypno "HONK" (show_chuckle=True)
    __p__.meu2 hypno "spoop" (show_chuckle=True, show_hashtags="#HONK")
    hide ob_meulin

    # Test dialogue systems
    # Compare our dialog systems against the vanilla ones
    # to ensure everything matches up
    bo "Boldir vanilla"
    __p__.bo "Boldir custom"
    vr "Vanilla vriska"
    !.vr "Custom vriska"
    jo "Vanilla john"
    __p__.jo "Custom john"
    ob_meulin "Custom openbound"

    "My quirk is weird and I exclaim wrong !it's weird"
    op "My quirk is weird and I exclaim wrong !it's weird"
    !.vr "My quirk is weird and I exclaim wrong !it's weird"



    # Trollian multiline test
    show vriska neutral1
    vr "Vanilla vriska"
    !.vr "Hi! I'm vriska\nLines are loose"
    !.vr "Hi! I'm vriska, but busy.\nMultiple lines are tight." (show_big=True)
    
    # Trollian colorizing
    !.vr "Override" (show_blood="#0A0")
    !.vr "Gray" (show_blood="gray")
    !.vr "Candy red" (show_blood="candyred")
    !.vr "burgundy" (show_blood="burgundy")
    !.vr "Bronze" (show_blood="bronze")
    !.vr "Gold" (show_blood="gold")
    !.vr "Lime" (show_blood="lime")
    !.vr "Olive" (show_blood="olive")
    !.vr "Jade" (show_blood="jade")
    !.vr "Teal" (show_blood="teal")
    !.vr "Cerulean" (show_blood="cerulean")
    !.vr "Indigo" (show_blood="indigo")
    !.vr "Purple" (show_blood="purple")
    !.vr "Violet" (show_blood="violet")
    !.vr "Fuchsia" (show_blood="fuchsia")
    hide vriska

    # Hiveswap colorizing
    show boldir neutral
    bo "Vanilla boldir"
    __p__.bo "Default"
    __p__.bo "Override" (show_blood="#0A0")
    __p__.bo "Test" (show_blood="test")
    __p__.bo "Gray" (show_blood="gray")
    __p__.bo "Candy red" (show_blood="candyred")
    bo "burgundy" (window_background="gui/textbox_rust.png")
    __p__.bo "burgundy" (show_blood="burgundy")
    bo "Bronze" (window_background="gui/textbox_bronze.png")
    __p__.bo "Bronze" (show_blood="bronze")
    bo "Gold" (window_background="gui/textbox_gold.png")
    __p__.bo "Gold" (show_blood="gold")
    __p__.bo "Lime" (show_blood="lime")
    bo "Olive" (window_background="gui/textbox_olive.png")
    __p__.bo "Olive" (show_blood="olive")
    bo "Jade" (window_background="gui/textbox_jade.png")
    __p__.bo "Jade" (show_blood="jade")
    bo "Teal" (window_background="gui/textbox_teal.png")
    __p__.bo "Teal" (show_blood="teal")
    bo "Cobalt" (window_background="gui/textbox_cobalt.png")
    __p__.bo "Cerulean" (show_blood="cerulean")
    bo "Blue" (window_background="gui/textbox_blue.png")
    __p__.bo "Indigo" (show_blood="indigo")
    bo "Purple" (window_background="gui/textbox_purple.png")
    __p__.bo "Purple" (show_blood="purple")
    __p__.bo "Violet" (show_blood="violet")
    __p__.bo "Fuchsia" (show_blood="fuchsia")
    hide boldir

    # Pesterchum and multilines
    show john neutral
    jo "Vanilla john"
    __p__.jo "Hi! I'm john\nLines are loose"
    __p__.jo "Hi! I'm john, but busy.\nMultiple lines are tight." (show_big=True)
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

    __p__.meu2 idle "!!"
    __p__.meu2 laugh "!!!" (show_hashtags="#hashtag1")
    __p__.meu2 hypno "HONK" (show_chuckle=True)
    __p__.meu2 hypno "spoop" (show_chuckle=True, show_hashtags="#HONK")
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
    show gamzee neutral

    # Approach 1: Call quirksay
    # Arguments are sayer (character), quirk name, text
    $ quirkSay(gam, "gamzee", "Quirk formatting 1")

    # Approach 2: Define a new sayer
    # Define a new character, given an existing character and a quirk
    # New sayer is reusable!
    $ __p__gamq = quirkSayer(gam, "gamzee")
    __p__gamq "Quirk formatting 2"
    __p__gamq "Quirk formatting 2 forever"

    # Approach 3
    # You can quirk format text without saying it directly
    $ gam(quirkSub("gamzee", "Quirk formatting 3") + " and I guess other stuff")
    hide gamzee

    show vriska neutral1
    !.vr "I'm 8riska"
    hide vriska

    show __p__terezi neutral
    # play music "music/fs_BOLDIR.wav" loop
    hide blackcover with dissolve

    # Test dynamic name growth
    $ tztitle = "A"
    __p__tz "1"
    $ tztitle = "AAAAAAAAAAAA"
    __p__tz "2"
    $ tztitle = "AAAAAAAAAAAAAAAAAAAAAAAAAAA"
    __p__tz "3"
    $ tztitle = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
    __p__tz "4"

    # Twitter demo
    __p__tz neutral "Hey. Hey. Over here."

    "Oh shit. You’re just standing out here with all his mail, he’s going to think you’re trying to rob the place."
    menu:
        "Oh shit. You’re just standing out here with all his mail, he’s going to think you’re trying to rob the place.{fast}"

        "[pick] Play it cool":
            pass
        "[pick] Hide the evidence":
            pass

    show __p__fakemenu
    __p__tz "UHHHHHHHH"

    show __p__terezi at right1280 with ease
    __p__tz "*SNIFFFFFFFF*"

    show __p__terezi at left1280 with move
    __p__tz "TF 1S TH1S TH1NG :?"

    hide __p__terezi
    hide __p__fakemenu

    show vriska neutral4

    # Write dialogue!
    vr neutral3 "Hey. Hey. Over here."
    vr __p__ngreen "8itch."

    hide vriska  # goodbye

    # You can use assets that have already been definied in other pesterquest routes directly!
    show bg gamzeehive
    show gamzee pie1
    gam pie1 "cAn I oFfEr YoU a PiE iN tHeSe TrYiNg TiMeS"
    # Be careful about naming your resources so they don't conflict with other ones. 
    # I help where I can by offering the substitutions like {{package_id}}.

    # Show end card
    call ending pass ("__p__vriskaend", True, True)
    return
