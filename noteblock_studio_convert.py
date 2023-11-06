import os
from pathlib import Path
import pandas as pd

from Tunes_calc_code import note_logic, pause_amount

data_pack_to_convert = "jingle_bells"

DIR = Path(__file__).parent
DIR_NEW_FILE = DIR.joinpath(f"convert/{data_pack_to_convert}.txt")
DIR_DATAPACK = Path(os.getenv("HOMEPATH")).joinpath("Desktop")

DIR_NOTES = DIR_DATAPACK.joinpath(f"{data_pack_to_convert}/functions/notes")


def inverse_frequencies(note_logic):
    frequencies = {
        value: key
        for key, value in note_logic.items()
        if (value[:5] != "scale") & (value[:5] != "pause") & (value[:7] != "section")
    }
    return frequencies


def get_note_files(DIR_NOTES):
    note_files_unsorted = DIR_NOTES.glob("*.mcfunction")
    note_files = []
    for note_file in note_files_unsorted:
        note_files.append(int(note_file.stem))
    note_files = sorted(note_files)
    return note_files


def get_file_content(filename):
    instruments = []
    freqs = []
    with open(filename, "r") as _file:
        for line in _file:
            if line.startswith("playsound"):
                line_split = line.split(" ")

                instrument = line_split[1].split(".")[-1]
                freq = str(round(float(line_split[-2]), 6))

                instruments.append(instrument)
                freqs.append(freq)
    return instruments, freqs


def convert_pause_amount(pause_amount):
    return {value: key[-1] for key, value in pause_amount.items()}


# def replace_pauses(music_instruments, amount_pause):
#     for music in music_instruments:


#     pass


def dataframe_to_encoded_notes(df, amount_pause):
    df = df.fillna(amount_pause[1])
    df = df.reindex(
        list(range(df.index.min(), df.index.max() + 1)), fill_value=amount_pause[1]
    )

    music_instruments = []
    for instrument in df.columns:
        music = f'{instrument} += "' + "".join(df[instrument].values) + '"'
        music_instruments.append(music)

    return music_instruments


def save_music_instruments(filename, music_instruments):
    with open(filename, "w+") as file_handle:
        for instrument in music_instruments:
            file_handle.write(instrument)
            file_handle.write("\n")


def main():
    note_files = get_note_files(DIR_NOTES)

    df = pd.DataFrame({})
    for index, note_file in enumerate(note_files):
        filename = DIR_NOTES.joinpath(f"{note_file}.mcfunction")
        instruments, freqs = get_file_content(filename)
        df.loc[note_file, instruments] = freqs

    inv_frequencies = inverse_frequencies(note_logic)
    df = df.replace(inv_frequencies)  # Convert frequencies to letters
    amount_pause = convert_pause_amount(pause_amount)
    music_instruments = dataframe_to_encoded_notes(df, amount_pause)

    save_music_instruments(filename=DIR_NEW_FILE, music_instruments=music_instruments)
    pass


if __name__ == "__main__":
    main()

