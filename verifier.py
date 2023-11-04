from tunes_calc_code import pause_amount
from pathlib import Path


DIR = Path(__file__).parent

melody = "pokemon"


pause_amount = {x[5:]: y for x, y in pause_amount.items()}


def get_line_sum(line, pause_amount):
    location = line.find("+=") + 4
    line = line[location:-2]
    sum = 0
    for char in line:
        if char in pause_amount:
            sum += pause_amount[char]
    return sum


with open(DIR.joinpath(f"melodies\{melody}.py")) as filehandle:
    for index, line in enumerate(filehandle):
        if "+=" in line:
            sum = get_line_sum(line, pause_amount)
            if (sum != 32) & (sum % 32 != 0):
                print(f"{index+1}: Line {line[:-1]} contains {sum} tacts")
