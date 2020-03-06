init offset = 1
image fs_tagora clasp = "{{assets}}/sprite/Tagora_clasp.png"
image fs_tagora document = "{{assets}}/sprite/Tagora_document.png"
image fs_tagora ew = "{{assets}}/sprite/Tagora_ew.png"
image fs_tagora helpful = "{{assets}}/sprite/Tagora_helpful.png"
image fs_tagora hollering = "{{assets}}/sprite/Tagora_hollering.png"
image fs_tagora judging = "{{assets}}/sprite/Tagora_judging.png"
image fs_tagora nervous = "{{assets}}/sprite/Tagora_nervous.png"
image fs_tagora neutral = "{{assets}}/sprite/Tagora_neutral.png"
image fs_tagora neutral2 = "{{assets}}/sprite/Tagora_neutral2.png"

init python:
    quirks["tagora"] = [("(.+)", "<1>\n\n*__________")]
define fs_tagora = Character(name="TAGORA", kind=hiveswap, image="tagora", show_blood="teal")

