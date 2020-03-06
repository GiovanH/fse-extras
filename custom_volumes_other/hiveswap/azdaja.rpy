init offset = 1
image fs_azdaja analize = "{{assets}}/sprite/Azdaja_analize.png"
image fs_azdaja bragging = "{{assets}}/sprite/Azdaja_bragging.png"
image fs_azdaja controlled = "{{assets}}/sprite/Azdaja_controlled.png"
image fs_azdaja embarrased = "{{assets}}/sprite/Azdaja_embarrased.png"
image fs_azdaja neutral = "{{assets}}/sprite/Azdaja_neutral.png"
image fs_azdaja pissed = "{{assets}}/sprite/Azdaja_pissed.png"
image fs_azdaja power1 = "{{assets}}/sprite/Azdaja_power1.png"
image fs_azdaja power2 = "{{assets}}/sprite/Azdaja_power2.png"
image fs_azdaja power3 = "{{assets}}/sprite/Azdaja_power3.png"
image fs_azdaja power4 = "{{assets}}/sprite/Azdaja_power4.png"
image fs_azdaja sayonara = "{{assets}}/sprite/Azdaja_sayonara.png"
image fs_azdaja surprise = "{{assets}}/sprite/Azdaja_surprise.png"

init python:
    quirks["azdaja"] = [("(.+)", "||| \g<1> |||")]
define fs_azdaja = Character(name="AZDAJA", kind=hiveswap, image="azdaja", show_blood="gold")

