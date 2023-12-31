# -*- coding: utf-8 -*-

pause_amount = {
    "pause:,": 1,
    "pause:.": 2,
    "pause:;": 3,
    "pause:-": 4,
    "pause:+": 8,
    "pause:*": 16,
    "pause:&": 32,
}

freqs = []
for i in range(0, 25):
    freqs.append(str(round((2 ** (i / 12.0)) / 2, 6)))

note_logic = {
    "1": "scale:1",
    "2": "scale:2",
    "3": "scale:3",
    "4": "scale:4",
    "5": "scale:5",
    "6": "scale:6",
    "7": "scale:7",
    "8": "scale:8",
    "9": "scale:9",
    ",": "pause:,",
    ".": "pause:.",
    ";": "pause:;",
    "-": "pause:-",
    "+": "pause:+",
    "*": "pause:*",
    "&": "pause:&",
    " ": "section",
    "#f": freqs[0],
    "g": freqs[1],
    "g#": freqs[2],
    "a#": freqs[4],
    "a": freqs[3],
    "b": freqs[5],
    "c": freqs[6],
    "c#": freqs[7],
    "d": freqs[8],
    "d#": freqs[9],
    "e": freqs[10],
    "f": freqs[11],
    "f#": freqs[12],
    "G": freqs[13],
    "G#": freqs[14],
    "A": freqs[15],
    "A#": freqs[16],
    "B": freqs[17],
    "C": freqs[18],
    "C#": freqs[19],
    "D": freqs[20],
    "D#": freqs[21],
    "E": freqs[22],
    "F": freqs[23],
    "F#": freqs[24],
}


def convert_notes_to_code(string, instrument, tact):

    code = ""
    scale = 3

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

    for freq in notes:
        if freq in pause_amount:
            tact += pause_amount[freq] * scale
        elif freq == "section":
            code += "\n"
        elif freq[0:5] == "scale":
            scale = int(freq[6])
        else:
            code += f"""execute if score @s tunes.tact matches {tact} run playsound minecraft:block.note_block.{instrument} record @a[distance=..128] ~ ~ ~ 8 {freq}\n"""

    code += "\n"

    return [code, tact]
