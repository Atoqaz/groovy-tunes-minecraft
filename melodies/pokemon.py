# https://minecraft.fandom.com/wiki/Note_Block
pling = ""  # Glowstone
harp = ""  # Any other block
bell = ""  # Gold block
chime = ""  # Packed ice
bit = ""  # Emerald block
xylophone = ""  # Bone
iron_xylophone = ""  # Iron block
banjo = ""  # Hay bale
guitar = ""  # Wool
bass = ""  # Wood
didgeridoo = ""  # Pumpkin
hat = ""  # Glass
snare = ""  # Sand
basedrum = ""  # Stone
flute = ""  # Clay / Honeycomb
cow_bell = ""  # Soul sand

# pause_amount = {
#     "pause,": 1,
#     "pause.": 2,
#     "pause;": 3,
#     "pause-": 4,
#     "pause+": 8,
#     "pause*": 16,
#     "pause&": 32,
#     "pause*": 64,
# }

# 32 tick per row

# Iron block
iron_xylophone += "&"
iron_xylophone += "&"
iron_xylophone += "&"
iron_xylophone += "&"
iron_xylophone += "-D-D-D-D+-D-"
# 5
iron_xylophone += "C+A-f*f-"
iron_xylophone += "D+D+C-A#-C+"
iron_xylophone += "&"
iron_xylophone += "-D#-D#+D#+F-D-"
iron_xylophone += "-C+A#*A#-"
# 10
iron_xylophone += "D+D-C+A#-D+"
iron_xylophone += "&"
iron_xylophone += "+D-D-D-D+D-"
iron_xylophone += "C+A-f*-"
iron_xylophone += "D-D+-C+A#-C-"
# 15
iron_xylophone += "&"
iron_xylophone += "-D#-D#-D#-D#+-F-"
iron_xylophone += "D+C-A#*A#-"
iron_xylophone += "D+D-C+A#-D+"

bell += "&"
bell += "&"
bell += "&"
bell += "&"
bell += "&"
# 5
bell += "&"
bell += "&"
bell += "&"
bell += "&"
bell += "&"
# 10
bell += "&"
bell += "&"
bell += "&"
bell += "&"
bell += "&"
# 15
bell += "&"
bell += "&"
bell += "&"
bell += "&"
bell += "*-d-f-G-"
# 20

# Wool block
guitar += "G+G+G+G+"
guitar += "G+G+G+G+"
guitar += "G+G+G+G+"
guitar += "*-d-f-G-"
guitar += "&"
# 5
guitar += "*-f-d-g-"
guitar += "&"
guitar += "+-f+c+d#-"
guitar += "d#&"
guitar += "a#&"
# 10
guitar += "a#+-c+-d+"
guitar += "*-d-f-G-"
guitar += "&"
guitar += "*-f-d-g-"
guitar += "&"
# 15
guitar += "+-f+c+d#-"
guitar += "d#&"
guitar += "a#&"
guitar += "a#+-c+-d+"
guitar += "*-d-f-G-"


# Wood
bass += "&"
bass += "&"
bass += "&"
bass += "*-d-f-G-"
bass += "&"
# 5
bass += "*-f-d-g-"
bass += "&"
bass += "+-f+c+d#-"
bass += "d#&"
bass += "a#&"
# 10
bass += "a#+-c+-d+"
bass += "*-d-f-G-"
bass += "&"
bass += "*-f-d-g-"
bass += "&"
# 15
bass += "+-f+c+d#-"
bass += "d#&"
bass += "a#&"
bass += "a#+-c+-d+"
bass += "*-d-f-G-"

# Diamond
harp += "GA#D-GA#D-GA#D-GA#D-GA#D-GA#D-GA#D-GA#D-"
harp += "fAD-fAD-fAD-fAD-fAD-fAD-fAD-fAD-"
harp += "GA#D-GA#D-GA#D-GA#D-GA#D-GA#D-GA#D-fAD-"
harp += "fAD-fAD-fAD-fAD-fAD-fAD-fAD-GA#D-"
harp += "GA#D-GA#D-GA#D-GA#D-GA#D-GA#D-GA#D-GA#D-"
# 5
harp += "fAD-fAD-fAD-fAD-fAD-fAD-fAD-GA#D-"
harp += "GA#D-GA#D-GA#D-GA#D-GA#D-GA#D-GA#D-GA#D-"
harp += "GCD-GCD-GCD-GCD-GCD-GCD-GCD-GCD-"
harp += "GA#D-GA#D-GA#D-GA#D-GA#D-GA#D-GA#D-GA#D-"
harp += "fA#D-fA#D-fA#D-fA#D-fA#D-fA#D-fA#D-fA#D-"
# 10
harp += "fA#D-fA#D-fA#D-GCD-GCD-GCD-fAD-fAD-"
harp += "fAD-fAD-fAD-fAD-fAD-fAD-fAD-fAD-"
harp += "GA#D-GA#D-GA#D-GA#D-GA#D-GA#D-GA#D-GA#D-"
harp += "faD-faD-faD-faD-faD-faD-faD-faD-"
harp += "GA#D-GA#D-GA#D-GA#D-GA#D-GA#D-GA#D-GA#D-"
# 15
harp += "GCD-GCD-GCD-GCD-GCD-GCD-GCD-GCD-"
harp += "GA#D#-GA#D#-GA#D#-GA#D#-GA#D#-GA#D#-GA#D#-GA#D#-"
harp += "fA#D-fA#D-fA#D-fA#D-fA#D-fA#D-fA#D-fA#D-"
harp += "fA#D-fA#D-fA#D-GCD-GCD-GCD-fAD+"
harp += "-fGD-fGD-fGD-Adf#+Adf#+"

# Sand
snare += "&"
snare += "&"
snare += "+b.b.b.b.b++"
snare += "*-b.b.b-f#-"
snare += "F#-F#-F#-F#-F#-F#-F#-F#-"
# 5
snare += "F#-F#-F#-F#-F#-F#-F#-F#-"
snare += "F#-F#-F#-F#-F#-F#-F#-F#-"
snare += "F#-F#-F#-F#d#-F#-F#b-F#-F#-"
snare += "F#c#-F#-F#-F#-F#-F#-F#-F#-"
snare += "F#-F#-F#-F#d#-F#-F#b-F#-F#-"
# 10
snare += "F#c#-F#-F#-F#f#-F#-F#b-F#d#-F#-"
snare += "F#-F#-F#-F#-F#--F#b-F#G-"
snare += "F#-F#-F#b-F#-F#-F#-F#-F#-"
snare += "F#-F#-F#b-F#-F#-F#a-F#-F#a-"
snare += "F#-F#-F#b-F#-F#-F#-F#-F#-"
# 15
snare += "F#-F#-F#b-F#d#-F#-F#b-F#-F#-"
snare += "F#f#-F#b-F#-F#-F#-F#-F#-F#-"
snare += "F#-F#-F#b-F#-F#-F#b-F#b-F#b.b."
snare += "F#c#-F#-F#-F#f#-F#-F#-F#d#-F#-"
snare += "&"

# Stone
basedrum += "&"
basedrum += "&"
basedrum += "*-d#-c#-b-"
basedrum += "-c#-c#-b-b*"
basedrum += "&"
# 5
basedrum += "&"
basedrum += "&"
basedrum += "+-b+b+b-"
basedrum += "&"
basedrum += "b&"
# 10
basedrum += "b+-b+-b+"
basedrum += "*-b-b+"
basedrum += "*-b-d#-b-"
basedrum += "*-b-d#-b-"
basedrum += "*-b-d#-b-"
# 15
basedrum += "+-b+b+b-"
basedrum += "*-b-d#-b-"
basedrum += "b&"
basedrum += "b+-b+-b+"
basedrum += "-b-b-b-b-d#-c#-b-"
