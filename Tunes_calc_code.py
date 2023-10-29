# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 13:15:51 2023

@author: AKris
"""

def convert_notes_to_code(string, instrument,tact):
    
    Code = ''
    
    freqs = []
    for i in range(0,25):
        freqs.append(str(round((2 ** (i/12.0))/2,6)))
    
    notes = []
    while (True):
        
        if (string == ''): break
        
        if string.startswith(','):
            notes.append('pause,')
            string = string[1:]
        elif string.startswith('.'):
            notes.append('pause.')
            string = string[1:]
        elif string.startswith(';'):
            notes.append('pause;')
            string = string[1:]
        elif string.startswith('-'):
            notes.append('pause-')
            string = string[1:]
        elif string.startswith('&'):
            notes.append('pause&')
            string = string[1:]
        elif string.startswith(' '):
            notes.append('section')
            string = string[1:]
        elif string.startswith('#f'):
            notes.append(freqs[0])
            string = string[2:]
        elif string.startswith('g#'):
            notes.append(freqs[2])
            string = string[2:]
        elif string.startswith('g'):
            notes.append(freqs[1])
            string = string[1:]
        elif string.startswith('a#'):
            notes.append(freqs[4])
            string = string[2:]
        elif string.startswith('a'):
            notes.append(freqs[3])
            string = string[1:]
        elif string.startswith('b'):
            notes.append(freqs[5])
            string = string[1:]
        elif string.startswith('c#'):
            notes.append(freqs[7])
            string = string[2:]
        elif string.startswith('c'):
            notes.append(freqs[6])
            string = string[1:]
        elif string.startswith('d#'):
            notes.append(freqs[9])
            string = string[2:]
        elif string.startswith('d'):
            notes.append(freqs[8])
            string = string[1:]
        elif string.startswith('e'):
            notes.append(freqs[10])
            string = string[1:]
        elif string.startswith('f#'):
            notes.append(freqs[12])
            string = string[2:]
        elif string.startswith('f'):
            notes.append(freqs[11])
            string = string[1:]
        elif string.startswith('G#'):
            notes.append(freqs[14])
            string = string[2:]
        elif string.startswith('G'):
            notes.append(freqs[13])
            string = string[1:]
        elif string.startswith('A#'):
            notes.append(freqs[16])
            string = string[2:]
        elif string.startswith('A'):
            notes.append(freqs[15])
            string = string[1:]
        elif string.startswith('B'):
            notes.append(freqs[17])
            string = string[1:]
        elif string.startswith('C#'):
            notes.append(freqs[19])
            string = string[2:]
        elif string.startswith('C'):
            notes.append(freqs[18])
            string = string[1:]
        elif string.startswith('D#'):
            notes.append(freqs[21])
            string = string[2:]
        elif string.startswith('D'):
            notes.append(freqs[20])
            string = string[1:]
        elif string.startswith('E'):
            notes.append(freqs[22])
            string = string[1:]
        elif string.startswith('F#'):
            notes.append(freqs[24])
            string = string[2:]
        elif string.startswith('F'):
            notes.append(freqs[23])
            string = string[1:]
        else:
            print("Something went wrong...")
            break
        


    for f in notes:
        
        if (f == 'pause,'):
            tact += 1
        elif (f == 'pause.'):
            tact += 2
        elif (f == 'pause;'):
            tact += 3
        elif (f == 'pause-'):
            tact += 4
        elif (f == 'pause&'):
            tact += 32
        elif (f == 'section'):
            Code += '\n'
        else:
            Code += 'execute if score @s tunes.tact matches '
            Code += str(tact)
            Code += ' run playsound minecraft:block.note_block.'
            Code += instrument
            Code += ' record @a[distance=..128] ~ ~ ~ 8 '
            Code += f
            Code += '\n'
    
    Code += '\n'
    
    return [Code,tact]