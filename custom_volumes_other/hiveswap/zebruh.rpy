init offset = 1
image fs_zebruh disgust = "{{assets}}/sprite/zebruh_disgust.png"
image fs_zebruh displeased = "{{assets}}/sprite/zebruh_displeased.png"
image fs_zebruh excited = "{{assets}}/sprite/zebruh_excited.png"
image fs_zebruh huh = "{{assets}}/sprite/zebruh_huh.png"
image fs_zebruh showoff = "{{assets}}/sprite/zebruh_showoff.png"
image fs_zebruh stand = "{{assets}}/sprite/zebruh_stand.png"
image fs_zebruh talk = "{{assets}}/sprite/zebruh_talk.png"
image fs_zebruh upset = "{{assets}}/sprite/zebruh_upset.png"
image fs_zebruh wink = "{{assets}}/sprite/zebruh_wink.png"

init python:
    quirks["zebruh_hearts"] = [("(.+)", "{image=char heart} \g<1> {image=char heart}")]
    quirks["zebruh_diamonds"] = [("(.+)", "{image=char diamond} \g<1> {image=char diamond}")]
    quirks["zebruh_clubs"] = [("(.+)", "{image=char club} \g<1> {image=char club}")]
    quirks["zebruh_spades"] = [("(.+)", "{image=char spade} \g<1> {image=char spade}")]
define fs_zebruh = Character(name="ZEBRUH", kind=hiveswap, image="zebruh", show_blood="blue")

