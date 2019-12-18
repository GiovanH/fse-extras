import glob
import subprocess
import os
import re


color_data = {
    "DAVE": "#e00707",
    "JADE": "#4ac925",
    "JOHN": "#0715cd",
    "ROSE": "#b536da"
}

char_kwargs = {
}


char_exdata = {
    "DIEMEN": r"""
init python:
    quirks["diemen"] = [("(.+)", "(| \g<1> |)")]
""",
    "AZDAJA": r"""
init python:
    quirks["azdaja"] = [("(.+)", "||| \g<1> |||")]
""",
    "AMISIA": r"""
init python:
    quirks["amisia"] = [("u", "uu")]
""",
    "TAGORA": r"""
init python:
    quirks["tagora"] = [("(.+)", "<1>\n\n*__________")]
""",
    "POLYPA": r"""
init python:
    quirks["polypa"] = [("(.+)", "<1> *|")]
""",
    "ZEBRUH": r"""
init python:
    quirks["zebruh_hearts"] = [("(.+)", "{image=char heart} \g<1> {image=char heart}")]
    quirks["zebruh_diamonds"] = [("(.+)", "{image=char diamond} \g<1> {image=char diamond}")]
    quirks["zebruh_clubs"] = [("(.+)", "{image=char club} \g<1> {image=char club}")]
    quirks["zebruh_spades"] = [("(.+)", "{image=char spade} \g<1> {image=char spade}")]
""",
}

char_extests = {
    "ZEBRUH": """
    $ quirkSay(zebruh, "zebruh_hearts", "Hearts")
    $ quirkSay(zebruh, "zebruh_spades", "Spades")
    $ quirkSay(zebruh, "zebruh_diamonds", "Diamonds")
    $ quirkSay(zebruh, "zebruh_clubs", "Clubs")
"""
}

talksprites = glob.glob("assets/sprite/*.*")

characters = set(
    os.path.split(talksprite)[1].split("_")[0].lower()
    for talksprite in talksprites
)


for character in characters:
    with open(f"{character}.rpy", "w") as charfp:
        try:
            text_color = color_data[character.upper()]
        except:
            print("Don't know character", character)
            continue
        define = f'define {character.lower()} = Character(name="{character.upper()}", what_color="{text_color}", kind=pesterchum, image="{character}")\n\n'

        charfp.write(define)
        for charsprite in glob.glob(f"assets/sprite/{character}_*.*"):
            filedir, filename = os.path.split(charsprite)
            charname, *rest = filename.split("_")
            charname = charname.lower()
            rest = " ".join(rest)
            pose = os.path.splitext(rest)[0]
            # print(charname, rest)

            kwargs = char_kwargs.get(charname, ", ypos=730")

            imgpath = charsprite.replace("assets/", "{{assets}}/").replace("\\", "/")
            image = f'image {charname} {pose} = Image("{imgpath}"{kwargs})\n'
            charfp.write(image)

        charfp.write(char_exdata.get(character.upper(), ""))
        charfp.close()


with open(f"backgrounds.rpy", "w") as bgfp:   
    for file in glob.glob(f"assets/bg/*.*"):
        filedir, filename = os.path.split(file)
        filename, fileext = os.path.splitext(filename)
        imgpath = file.replace("assets/", "{{assets}}/").replace("\\", "/")
        bgfp.write(f'image bg {filename} = Image("{imgpath}")\n')

with open(f"objects.rpy", "w") as bgfp:   
    for file in glob.glob(f"assets/object/*.*"):
        filedir, filename = os.path.split(file)
        filename, fileext = os.path.splitext(filename)
        imgpath = file.replace("assets/", "{{assets}}/").replace("\\", "/")
        bgfp.write(f'image {filename} = Image("{imgpath}")\n')

with open(f"effects.rpy", "w") as bgfp:   
    for file in glob.glob(f"assets/object/*.*"):
        filedir, filename = os.path.split(file)
        filename, fileext = os.path.splitext(filename)
        imgpath = file.replace("assets/", "{{assets}}/").replace("\\", "/")
        bgfp.write(f'image fx {filename} = Image("{imgpath}")\n')

with open(f"text.rpy", "w") as bgfp:   
    for file in glob.glob(f"assets/text/*.*"):
        filedir, filename = os.path.split(file)
        filename, fileext = os.path.splitext(filename)
        imgpath = file.replace("assets/", "{{assets}}/").replace("\\", "/")
        bgfp.write(f'image char {filename} = Image("{imgpath}")\n')
