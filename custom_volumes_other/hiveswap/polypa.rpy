init offset = 1
image fs_polypa dejected = "{{assets}}/sprite/polypa_dejected.png"
image fs_polypa hoodie_intro = "{{assets}}/sprite/polypa_hoodie_intro.png"
image fs_polypa hoodie_pissed = "{{assets}}/sprite/polypa_hoodie_pissed.png"
image fs_polypa neutral = "{{assets}}/sprite/polypa_neutral.png"
image fs_polypa pleased = "{{assets}}/sprite/polypa_pleased.png"
image fs_polypa scuffle = "{{assets}}/sprite/polypa_scuffle.png"
image fs_polypa serious = "{{assets}}/sprite/polypa_serious.png"
image fs_polypa shocked = "{{assets}}/sprite/polypa_shocked.png"
image fs_polypa shooshpap = "{{assets}}/sprite/polypa_shooshpap.png"

init python:
    quirks["polypa"] = [("(.+)", "<1> *|")]
define fs_polypa = Character(name="POLYPA", kind=hiveswap, image="polypa", show_blood="olive")

