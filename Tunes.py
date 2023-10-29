# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 19:05:17 2023

@author: AKris
"""
from Tunes_calc_code import *
from pathlib import Path
import os

DIR = Path(__file__).parent

tact = 1
max_tact = 1
melody = "amtet"
saves_folder = "TestyTown"
datapack_name = "groovy tunes"
# location = Path(os.getenv("APPDATA")).joinpath(
#     f".minecraft/saves/{saves_folder}/datapacks/{datapack_name}/data/tunes/functions/melody/{melody}.mcfunction"
# )
location = DIR.joinpath(
    f"{datapack_name}/data/tunes/functions/melody/{melody}.mcfunction"
)  # Testing

pling = ""
harp = ""
bell = ""
chime = ""
bit = ""
xylophone = ""
banjo = ""
guitar = ""
bass = ""
didgeridoo = ""
hat = ""
snare = ""
basedrum = ""

if melody == "ghostbusters":

    pling += "gc.gc.-dfA#-cfA-gc.gc.-dfA#-cfA-gc.gc.-dfA#-cfA-gc.gc.-dfA#.dfA#.cfA- "
    pling += ".C,C,GCE.C.fA#D.A#.--C,C,C,C,dfA#.C.-.C,C,GCE.C.fA#D.A#.--C,C,C,C,dfA#.D.fAC.C,C, "
    pling += "GD#.C.D#-dfA#-cfA.C,A#,GC.C.C-dfA#-cfA-gc.gc.-dfA#-cfA-gc.gc.-dfA#.dfA#.cfA.C,C, "
    pling += "GD#.C.D#-dfA#-cfA.C,A#,GC.C.C-dfA#-cfA-gc.gc.-fA#D-fAC-gc.gc.-fA#D.fA#D.fAC.G. "
    pling += "D#;C;D#;C;D#;C;D#;C;D#.C.A#,B,C.D#;C;D#;C;D#;C;D#;C;D#.C.A#,B,C. "
    pling += "D#G;CD#;D#G;CD#;D#G;CD#;D#G;CD#;D#G.CD#.A#,B,C.D#G;CD#;D#G;CD#;D#G;CD#;D#G;CD#;D#G.CD#.A#,B,C. "
    pling += "cGC.cGC."

    bass += "c.c.d#,e,G.A#.A#.f.f.c.c.d#,e,G.A#.A#.f.f.c.c.d#,e,G.A#.A#.f.f.c.c.d#,e,G.A#.A#.f.f. "
    bass += "c.c.d#,e,G.A#.A#.f.f.c.c.d#,e,G.A#.A#.f.f.c.c.d#,e,G.A#.A#.f.f.c.c.d#,e,G.A#.A#.f.f. "
    bass += "c.c.d#,e,G.A#.A#.f.f.c.c.d#,e,G.A#.A#.f.f.c.c.d#,e,G.A#.A#.f.f.c.c.d#,e,G.A#.A#.f.f. "
    bass += "c.c.d#,e,G.A#.A#.f.f.c.c.d#,e,G.A#.A#.f.f.c.c.d#,e,G.A#.A#.f.f.c.c.d#,e,G.A#.A#.f.g. "
    bass += "c-C-c-A#-a#-A#-a#A#.a#A#.a#A#.a#A#.a-A-a-f-f-f-f.f.f.f. "
    bass += "c-C-c-A#-a#-A#-a#A#.a#A#.a#A#.a#A#.a-A-a-f-f-f-f.f.f.f. "
    bass += "cC.cC."

elif melody == "amtet":

    pling += "&&"
    pling += "B;A;f#-d....A,A,A.A.B.D.D.B."
    pling += "E;D;B.A..f#.A.B;A;f#.e..e.d."
    pling += "e;f#;d----.G;G;G."
    pling += ".f#.-------"
    pling += "&&&&"
    pling += "B;A;f#-d....A,A,A.A.B.D.D.B."
    pling += "E;D;B.A..f#.A.B;A;f#.e..e.d."
    pling += "e;f#;d----.G;G;G."
    pling += ".f#"

    banjo += "&&&&&&&&&&"
    banjo += "B;A;f#-d....A,A,A.A.B.D.D.B."
    banjo += "E;D;B.A..f#.A.B;A;f#.e..e.d."
    banjo += "e;f#;d----.G;G;G."
    banjo += ".f#"

    chime += "&&&&&&&&&&&&------G;G;G."
    chime += ".f#"

    xylophone += ".A,A,A.A,A.A,A.B-.A,A,A.A,A.A,A.G#-"
    xylophone += ".A,A,A.A,A.A,A.B-.A,A,A.A,A.A,A.G#-"
    xylophone += ".A,A,A.A,A.A,A.B-.A,A,A.A,A.A,A.G#-"
    xylophone += ".A,A,A.A,A.A,A.B-.A,A,A.A,A.A,A.G#-"
    xylophone += ".B,B,B.B,B.C#;B.A..E,E,E.E,E.F#;E.C#."
    xylophone += ".A,A,A.A,A.A,A.B-.A,A,A.A,A.A,A.B-"

    harp += "&&&&&&"
    harp += "a-.a--c#.d-.d-.d-b-.b.--d-.c#.--"
    harp += "a-.a--c#.d-.d-.d-b-.b.--d-.c#.--"

    bass += "aaa----aaa----aaa----aaa----"
    bass += "aaa----aaa---g#g#g#-#f#f#f-------ccc-bbb---bBB-g#G#G#----aaa----aaa----"
    bass += "aaa-.aaa-eee.ggg.g#g#g#.aaa-.aaa-eee.ggg.g#g#g#.ddd-.ddd-aaa.ccc.ddd.eee;ccc;ddd-ggg.ccc.aaa."
    bass += "aaa-.aaa-eee.ggg.g#g#g#.aaa-.aaa-eee.ggg.g#g#g#.ddd-.ddd-aaa.ccc.ddd.eee;ccc;ddd-ggg.ccc.aaa."
    bass += "aaa----aaa---g#g#g#-#f#f#f-------ccc-bbb---bBB-g#G#G#----aaa"

    hat += "-f#--f#--f#--f#--f#--f#--f#--f#--f#--f#--f#--f#--f#--f#--f#--f#--f#--f#--f#--f#--f#--f#--f#---"
    snare += "&&&&&-------f#,f#;-f#--f#--f#--f#--f#--f#--f#--f#,f#;-f#--f#--f#--f#--f#--f#--f#-.f#,f#,f#,f#;-f#--f#--f#--f#--f#--f#--f#--f#,f#;-f#--f#--f#--f#-"
    basedrum += "&&&&&&f#--f#--f#--f#--f#--f#--f#--f#--f#--f#--f#--f#--f#--f#--f#--f#--f#--f#--f#--f#--f#--f#--f#--f#--f#--f#--f#--f#--"


code = "particle note ~ ~ ~ 1 1 1 1 1 normal @a\n\n"


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

for notes_instrument in notes_instruments:
    notes, instrument = notes_instrument
    if notes:
        convert = convert_notes_to_code(notes, instrument, tact)
        code += convert[0]
        max_tact = max(max_tact, convert[1])
        # tact = convert[1]


code += "\nexecute if score @s tunes.tact matches "
code += str(max_tact)
code += ".. run function tunes:reset"

with open(location, "w+") as text_file:
    text_file.write(code)
print("done")
