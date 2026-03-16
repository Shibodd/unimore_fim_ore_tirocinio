import numpy as np
import pandas as pd

from pypdf import PdfWriter, PageObject
from pypdf.annotations import FreeText

def write_rows(df: pd.DataFrame, writer: PdfWriter, page_idx):
    MARGIN_X = 2
    MARGIN_Y = 4
    ROW_H = 18.6
    Y_START = 503.6
    N_ROWS = 20
    OFF_X = [51, 55.5, 191, 92.3, 92.3, 57]
    
    col_x = np.cumsum(OFF_X)
    
    if len(df) > N_ROWS:
        raise Exception("diocan")
    
    for i in range(len(df)):
        
        morning = ""
        afternoon = ""
        
        if df["hours_morning"].iloc[i] > 0:
            morning = df["morning_from"].iloc[i].strftime("%H:%M") + " / " + df["morning_to"].iloc[i].strftime("%H:%M")
        if df["hours_afternoon"].iloc[i] > 0:
            afternoon = df["afternoon_from"].iloc[i].strftime("%H:%M") + " / " + df["afternoon_to"].iloc[i].strftime("%H:%M")
        
        data = [
            df["date"].iloc[i].strftime("%d/%m/%Y"),
            df["description"].iloc[i],
            morning,
            afternoon,
            str(df["hours"].iloc[i])
        ]
        
        assert (len(data) == len(col_x)-1)
        
        for j in range(len(col_x)-1):
            x1 = col_x[j]
            x2 = col_x[j+1]
            y = Y_START - ROW_H * i
            
            annotation = FreeText(
                text=data[j],
                rect=(x1 + MARGIN_X, y-ROW_H, x2, y - MARGIN_Y),
                font="Helvetica",
                bold=False,
                italic=False,
                font_size="20pt",
                font_color="00ff00",
                border_color=None, # change these to some other color for calibrating
                background_color=None,
            )

            # Set annotation flags to 4 for printable annotations.
            # See "AnnotationFlag" for other options, e.g. hidden etc.
            annotation.flags = 4

            writer.add_annotation(page_number=page_idx, annotation=annotation)

def write_tot_hours(df: pd.DataFrame, writer: PdfWriter, page_idx):
    X = 497
    Y = 119
    
    W = 30
    H = 10
    
    annotation = FreeText(
        text=str(df["hours"].sum()),
        rect=(X, Y - H, X + W, Y),
        font="Helvetica",
        bold=False,
        italic=False,
        font_size="20pt",
        font_color="00ff00",
        border_color=None, # change these to some other color for calibrating
        background_color=None,
    )

    # Set annotation flags to 4 for printable annotations.
    # See "AnnotationFlag" for other options, e.g. hidden etc.
    annotation.flags = 4

    writer.add_annotation(page_number=page_idx, annotation=annotation)

def write_tot_days(df: pd.DataFrame, writer: PdfWriter, page_idx):
    X = 497
    Y = 95
    
    W = 30
    H = 10
    
    annotation = FreeText(
        text=str(len(df)),
        rect=(X, Y - H, X + W, Y),
        font="Helvetica",
        bold=False,
        italic=False,
        font_size="20pt",
        font_color="00ff00",
        border_color=None, # change these to some other color for calibrating
        background_color=None,
    )

    # Set annotation flags to 4 for printable annotations.
    # See "AnnotationFlag" for other options, e.g. hidden etc.
    annotation.flags = 4

    writer.add_annotation(page_number=page_idx, annotation=annotation)

def write_page_number(df: pd.DataFrame, writer: PdfWriter, page_idx):
    X = 105
    Y = 665
        
    W = 25
    H = 10
    
    annotation = FreeText(
        text=str(page_idx + 1),
        rect=(X, Y - H, X + W, Y),
        font="Helvetica",
        bold=False,
        italic=False,
        font_size="20pt",
        font_color="00ff00",
        border_color=None, # change these to some other color for calibrating
        background_color=None,
    )

    # Set annotation flags to 4 for printable annotations.
    # See "AnnotationFlag" for other options, e.g. hidden etc.
    annotation.flags = 4

    writer.add_annotation(page_number=page_idx, annotation=annotation)

def write_person(surname, name, registration_num, writer: PdfWriter, page_idx):
    MARGIN_X = 5
    MARGIN_Y = 2
    
    X = 110
    Y = 579
        
    W = 152
    H = 12.7
    
    data = [surname, name, registration_num]
    for i in range(len(data)):
        annotation = FreeText(
            text=data[i],
            rect=(X+MARGIN_X, Y - H - i*H, X + W, Y - i*H - MARGIN_Y),
            font="Helvetica",
            bold=False,
            italic=False,
            font_size="20pt",
            font_color="00ff00",
            border_color=None, # change these to some other color for calibrating
            background_color=None,
        )

        # Set annotation flags to 4 for printable annotations.
        # See "AnnotationFlag" for other options, e.g. hidden etc.
        annotation.flags = 4

        writer.add_annotation(page_number=page_idx, annotation=annotation)

def write_course(course, writer: PdfWriter, page_idx):
    X = 247
    Y = 701
        
    W = 200
    H = 13
    
    annotation = FreeText(
        text=course,
        rect=(X, Y - H, X + W, Y),
        font="Helvetica",
        bold=False,
        italic=False,
        font_size="20pt",
        font_color="00ff00",
        border_color=None, # change these to some other color for calibrating
        background_color=None,
    )

    # Set annotation flags to 4 for printable annotations.
    # See "AnnotationFlag" for other options, e.g. hidden etc.
    annotation.flags = 4

    writer.add_annotation(page_number=page_idx, annotation=annotation)

def write_month_year(month, year, writer: PdfWriter, page_idx):
    MARGIN_X = 5
    MARGIN_Y = 7
    
    Y = 630.6
        
    W = [53, 110, 100]
    H = 28
    
    col_x = np.cumsum(W)
    
    MONTHS = [
        "Gennaio",
        "Febbraio",
        "Marzo",
        "Aprile",
        "Maggio",
        "Giugno",
        "Luglio",
        "Agosto",
        "Settembre",
        "Ottobre",
        "Novembre",
        "Dicembre"
    ]
    
    data = [MONTHS[month-1], year]
    for i in range(len(data)):
        annotation = FreeText(
            text=data[i],
            rect=(MARGIN_X + col_x[i], Y - H, col_x[i+1], Y - MARGIN_Y),
            font="Helvetica",
            bold=False,
            italic=False,
            font_size="20pt",
            font_color="00ff00",
            border_color=None, # change these to some other color for calibrating
            background_color=None,
        )

        # Set annotation flags to 4 for printable annotations.
        # See "AnnotationFlag" for other options, e.g. hidden etc.
        annotation.flags = 4

        writer.add_annotation(page_number=page_idx, annotation=annotation)

import dataclasses

@dataclasses.dataclass
class Person:
    surname: str
    name: str
    registration: str
    course: str

def write(df: pd.DataFrame, person: Person, page_template: PageObject, writer: PdfWriter):
    N = 20
    
    dfs_by_month = {
        period: group.copy()
        for period, group in df.groupby(df["date"].dt.to_period("M"))
    }
    
    for period, period_df in dfs_by_month.items():
        for start in range(0, len(period_df), N):
            data = period_df.iloc[start:start + N]

            page = writer.add_page(page_template)
            write_rows(data, writer, page.page_number)
            write_tot_hours(data, writer, page.page_number)
            write_tot_days(data, writer, page.page_number)
            write_page_number(data, writer, page.page_number)
            write_person(person.surname, person.name, person.registration, writer, page.page_number)
            write_course(person.course, writer, page.page_number)
            write_month_year(period.month, period.year, writer, page.page_number)
