# -*- coding: utf-8 -*-
from Tunes_calc_code import *
from pathlib import Path
import os

DIR = Path(__file__).parent

debug = False
tact_number = 32
melody = "jingle_bells"
saves_folder = "TestyTown"
datapack_name = "groovy tunes"

if melody == "ghostbusters":
    from melodies.ghostbusters import *
elif melody == "amtet":
    from melodies.amtet import *
elif melody == "all_i_want":
    from melodies.all_i_want import *
elif melody == "pokemon":
    from melodies.pokemon import *
elif melody == "last_christmas":
    from melodies.last_christmas import *
elif melody == "jingle_bells":
    from melodies.jingle_bells import *

location_datapack = Path(os.getenv("APPDATA")).joinpath(
    f".minecraft/saves/{saves_folder}/datapacks/{datapack_name}/data/tunes/functions/melody/{melody}.mcfunction"
)  # Datapack

location_local = DIR.joinpath(
    f"{datapack_name}/data/tunes/functions/melody/{melody}.mcfunction"
)  # Testing


notes_instruments = [
    (pling, "pling"),
    (harp, "harp"),
    (bell, "bell"),
    (chime, "chime"),
    (bit, "bit"),
    (flute, "flute"),
    (xylophone, "xylophone"),
    (iron_xylophone, "iron_xylophone"),
    (banjo, "banjo"),
    (guitar, "guitar"),
    (bass, "bass"),
    (didgeridoo, "didgeridoo"),
    (hat, "hat"),
    (snare, "snare"),
    (basedrum, "basedrum"),
]

code = (
    "execute if predicate tunes:rand25 run particle note ~ ~ ~ 1 1 1 1 1 normal @a\n\n"
)

tact = 1
max_tact = 1
for notes_instrument in notes_instruments:
    notes, instrument = notes_instrument
    if notes:
        new_code, new_tact = convert_notes_to_code(notes, instrument, tact)
        code += new_code
        max_tact = max(max_tact, new_tact)


if debug:
    for interval in range(int(max_tact / tact_number)):
        code += f"""\nexecute if score @s tunes.tact matches {interval*tact_number} run tellraw @a "Row: {interval+1} - Tact: {interval*tact_number} " """

code += (
    f"\nexecute if score @s tunes.tact matches {max_tact}.. run function tunes:reset"
)

with open(location_datapack, "w+") as text_file:
    text_file.write(code)


with open(location_local, "w+") as text_file:
    text_file.write(code)

print(f"Created song: {melody.capitalize()}")
