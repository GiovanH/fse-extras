import glob
import subprocess
import os
import re


color_data = {
    "karkat": 'gray',
    "aradia": 'burgundy',
    "tavros": 'bronze',
    "sollux": 'gold',
    "nepeta": 'olive',
    "kanaya": 'jade',
    "terezi": 'teal',
    "vriska": 'cerulean',
    "equius": 'indigo',
    "gamzee": 'purple',
    "eridan": 'violet',
    "feferi": 'fuchsia'
}

char_kwargs = {
}


char_exdata = {
}

char_extests = {
}

talksprites = glob.glob("assets/sprite/*.*")

characters = set(
    os.path.split(talksprite)[1].split("_")[0].lower()
    for talksprite in talksprites
)


for character in characters:
    with open(f"{character}.rpy", "w") as charfp:
        try:
            text_color = color_data[character.lower()]
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
