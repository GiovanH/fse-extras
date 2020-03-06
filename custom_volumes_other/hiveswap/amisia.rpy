init offset = 1
image fs_amisia axe = "{{assets}}/sprite/amisia_axe.png"
image fs_amisia blur2 = "{{assets}}/sprite/amisia_blur2.png"
image fs_amisia confess = "{{assets}}/sprite/amisia_confess.png"
image fs_amisia doubt = "{{assets}}/sprite/amisia_doubt.png"
image fs_amisia frame = "{{assets}}/sprite/amisia_frame.png"
image fs_amisia growl = "{{assets}}/sprite/amisia_growl.png"
image fs_amisia hairpull = "{{assets}}/sprite/amisia_hairpull.png"
image fs_amisia hop = "{{assets}}/sprite/amisia_hop.png"
image fs_amisia nya = "{{assets}}/sprite/amisia_nya.png"
image fs_amisia ponder = "{{assets}}/sprite/amisia_ponder.png"
image fs_amisia smile = "{{assets}}/sprite/amisia_smile.png"
image fs_amisia smile2 = "{{assets}}/sprite/amisia_smile2.png"
image fs_amisia smug = "{{assets}}/sprite/amisia_smug.png"

init python:
    quirks["amisia"] = [("u", "uu")]
define fs_amisia = Character(name="AMISIA", kind=hiveswap, image="amisia", show_blood="blue")

