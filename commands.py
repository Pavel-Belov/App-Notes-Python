from datetime import datetime
import pandas as pd

from utils import *


csv_file = "notes.csv"

# 
def create_note(title, text):
    id_note = get_id()
    df = pd.read_csv(csv_file)
    new_row = pd.Series([id_note, title, text, datetime.now()],
                        index=["Id", "Title", "Text", "Date"])
    df.loc[len(df.index)] = new_row
    df.to_csv(csv_file, index=False)
    increment_id(int(id_note))


def delete_note(id_note):
    df = pd.read_csv(csv_file)
    df = df[df["Id"] != int(id_note)]
    df.to_csv(csv_file, index=False)


def edit_note(id_note, title, text):
    df = pd.read_csv(csv_file)
    if title != "":
        df.loc[df["Id"] == int(id_note), "Title"] = title
        df.loc[df["Id"] == int(id_note), "Date"] = datetime.now()
        df.to_csv(csv_file, index=False)
    if text != "":
        df.loc[df["Id"] == int(id_note), "Text"] = text
        df.loc[df["Id"] == int(id_note), "Date"] = datetime.now()
        df.to_csv(csv_file, index=False)


def get_note(id_note):
    df = pd.read_csv(csv_file)
    if (df["Id"] == int(id_note)).any():
        note = df[(df["Id"] == int(id_note))]
        return note.to_string(index=False)
    else:
        return None


def get_list_of_notes():
    df = pd.read_csv(csv_file)
    df.sort_values(by="Date", inplace=True)
    return df.to_string(index=False)
