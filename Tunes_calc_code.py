# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 13:15:51 2023

@author: AKris
"""


def convert_notes_to_code(string, instrument, tact):

    code = ""

    freqs = []
    for i in range(0, 25):
        freqs.append(str(round((2 ** (i / 12.0)) / 2, 6)))

    note_logic = {
        ",": "pause,",
        ".": "pause.",
        ";": "pause;",
        "-": "pause-",
        "&": "pause&",
        " ": "section",
        "#f": freqs[0],
        "g#": freqs[2],
        "g": freqs[1],
        "a#": freqs[4],
        "a": freqs[3],
        "b": freqs[5],
        "c#": freqs[7],
        "c": freqs[6],
        "d#": freqs[9],
        "d": freqs[8],
        "e": freqs[10],
        "f#": freqs[12],
        "f": freqs[11],
        "G#": freqs[14],
        "G": freqs[13],
        "A#": freqs[16],
        "A": freqs[15],
        "B": freqs[17],
        "C#": freqs[19],
        "C": freqs[18],
        "D#": freqs[21],
        "D": freqs[20],
        "E": freqs[22],
        "F#": freqs[24],
        "F": freqs[23],
    }

    notes = []
    while True:

        if string == "":
            break

        if string[:2] in note_logic:
            notes.append(note_logic[string[:2]])
            string = string[2:]
        elif string[:1] in note_logic:
            notes.append(note_logic[string[:1]])
            string = string[1:]
        else:
            raise ValueError(f"Note not defined for string {string[:2]}")

    for f in notes:
        if f == "pause,":
            tact += 1
        elif f == "pause.":
            tact += 2
        elif f == "pause;":
            tact += 3
        elif f == "pause-":
            tact += 4
        elif f == "pause&":
            tact += 32
        elif f == "section":
            code += "\n"
        else:
            code += "execute if score @s tunes.tact matches "
            code += str(tact)
            code += " run playsound minecraft:block.note_block."
            code += instrument
            code += " record @a[distance=..128] ~ ~ ~ 8 "
            code += f
            code += "\n"

    code += "\n"

    return [code, tact]
