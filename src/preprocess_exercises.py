#preprocess_exercices.py


from .clean_columns import clean_column
import pandas as pd

def preprocess_exercises(df):
    print('_____________11111______________________')
    df = clean_column(df)
    print('_____________11111______________________')
    df = df.rename(columns={
        "level": "difficulty",
        "bodypart": "body_part"
    })
    print('_____________11111______________________')
    df = df.drop(columns=["ratingdesc"], errors="ignore")
    print('_____________11111______________________')
    df = df[["title", "type", "body_part", "equipment", "difficulty", "desc"]]
    print('_____________11111______________________')
    df["title_clean"] = df["title"].str.lower().str.strip()
    return df
