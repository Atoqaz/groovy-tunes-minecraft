# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 19:05:17 2023

@author: AKris
"""
from Tunes_calc_code import *
from pathlib import Path
import os

DIR = Path(__file__).parent

to_datapack = 0
melody = "amtet"
saves_folder = "TestyTown"
datapack_name = "groovy tunes"

if melody == "ghostbusters":
    from melodies.ghostbusters import *
elif melody == "amtet":
    from melodies.amtet import *

if to_datapack:
    location = Path(os.getenv("APPDATA")).joinpath(
        f".minecraft/saves/{saves_folder}/datapacks/{datapack_name}/data/tunes/functions/melody/{melody}.mcfunction"
    )  # Datapack
else:
    location = DIR.joinpath(
        f"{datapack_name}/data/tunes/functions/melody/{melody}.mcfunction"
    )  # Testing


notes_instruments = [
    (pling, "pling"),
    (harp, "harp"),
    (bell, "bell"),
    (chime, "chime"),
    (bit, "bit"),
    (xylophone, "xylophone"),
    (banjo, "banjo"),
    (guitar, "guitar"),
    (bass, "bass"),
    (didgeridoo, "didgeridoo"),
    (hat, "hat"),
    (snare, "snare"),
    (basedrum, "basedrum"),
]

code = "particle note ~ ~ ~ 1 1 1 1 1 normal @a\n\n"

tact = 1
max_tact = 1
for notes_instrument in notes_instruments:
    notes, instrument = notes_instrument
    if notes:
        new_code, new_tact = convert_notes_to_code(notes, instrument, tact)
        code += new_code
        max_tact = max(max_tact, new_tact)
        # tact = convert[1]


code += "\nexecute if score @s tunes.tact matches "
code += str(max_tact)
code += ".. run function tunes:reset"

with open(location, "w+") as text_file:
    text_file.write(code)

print(f"Created song: {melody.capitalize()}")
