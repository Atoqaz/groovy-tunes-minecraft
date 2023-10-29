# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 19:05:17 2023

@author: AKris
"""
from Tunes_calc_code import *
from pathlib import Path
import os

DIR = Path(__file__).parent

melody = 'amtet'
saves_folder = "TestyTown"
datapack_name = "groovy tunes"
location = Path(os.getenv("APPDATA")).joinpath(f".minecraft/saves/{saves_folder}/datapacks/{datapack_name}/data/tunes/functions/melody/{melody}.mcfunction")

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

if (melody == 'ghostbusters'):
    
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
    
elif (melody == 'amtet'):
    
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
    


Code = 'particle note ~ ~ ~ 1 1 1 1 1 normal @s\n\n'
tact = 1
max_tact = 1

if (pling != ""):
    convert = convert_notes_to_code(pling,'pling',tact)
    Code += convert[0]
    max_tact = max(max_tact, convert[1])
    #tact = convert[1]

if (harp != ""):
    convert = convert_notes_to_code(harp,'harp',tact)
    Code += convert[0]
    max_tact = max(max_tact, convert[1])
    #tact = convert[1]

if (bell != ""):
    convert = convert_notes_to_code(bell,'bell',tact)
    Code += convert[0]
    max_tact = max(max_tact, convert[1])
    #tact = convert[1]

if (chime != ""):
    convert = convert_notes_to_code(chime,'chime',tact)
    Code += convert[0]
    max_tact = max(max_tact, convert[1])
    #tact = convert[1]

if (bit != ""):
    convert = convert_notes_to_code(bit,'bit',tact)
    Code += convert[0]
    max_tact = max(max_tact, convert[1])
    #tact = convert[1]

if (xylophone != ""):
    convert = convert_notes_to_code(xylophone,'xylophone',tact)
    Code += convert[0]
    max_tact = max(max_tact, convert[1])
    #tact = convert[1]

if (banjo != ""):
    convert = convert_notes_to_code(banjo,'banjo',tact)
    Code += convert[0]
    max_tact = max(max_tact, convert[1])
    #tact = convert[1]

if (guitar != ""):
    convert = convert_notes_to_code(guitar,'guitar',tact)
    Code += convert[0]
    max_tact = max(max_tact, convert[1])
    #tact = convert[1]

if (bass != ""):
    convert = convert_notes_to_code(bass,'bass',tact)
    Code += convert[0]
    max_tact = max(max_tact, convert[1])
    #tact = convert[1]

if (didgeridoo != ""):
    convert = convert_notes_to_code(didgeridoo,'didgeridoo',tact)
    Code += convert[0]
    max_tact = max(max_tact, convert[1])
    #tact = convert[1]

if (hat != ""):
    convert = convert_notes_to_code(hat,'hat',tact)
    Code += convert[0]
    max_tact = max(max_tact, convert[1])
    #tact = convert[1]

if (snare != ""):
    convert = convert_notes_to_code(snare,'snare',tact)
    Code += convert[0]
    max_tact = max(max_tact, convert[1])
    #tact = convert[1]

if (basedrum != ""):
    convert = convert_notes_to_code(basedrum,'basedrum',tact)
    Code += convert[0]
    max_tact = max(max_tact, convert[1])
    #tact = convert[1]


Code += '\nexecute if score @s tunes.tact matches '
Code += str(max_tact)
Code += '.. run function tunes:reset'


text_file = open(location,"w")
text_file.write(Code)
text_file.close()

