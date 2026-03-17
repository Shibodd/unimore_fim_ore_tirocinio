from pypdf import PdfReader, PdfWriter
import pandas as pd
import PIL.Image

import the_writer 


TEMPLATE = "Scheda ORE FIM.pdf"
DATA = "data.csv"
OUTPUT = "out.pdf"

person = the_writer.Person(
    "Eusebio",
    "Tritagatti",
    "123456",
    "Informatica"
)

reader = PdfReader(TEMPLATE)
template_page = reader.pages[0]

writer = PdfWriter()

df = pd.read_csv(DATA, parse_dates=["date"], dayfirst=True)
for c in ["morning_from", "morning_to", "afternoon_from", "afternoon_to"]:
    df[c] = pd.to_datetime(df[c], format="%H:%M")

df["hours_morning"] = ((df["morning_to"] - df["morning_from"]) / pd.Timedelta(hours=1)).round().astype(int)
df["hours_afternoon"] = ((df["afternoon_to"] - df["afternoon_from"]) / pd.Timedelta(hours=1)).round().astype(int)
df["hours"] = df["hours_morning"] + df["hours_afternoon"]

the_writer.write(df, person, template_page, writer)
writer.write(OUTPUT)