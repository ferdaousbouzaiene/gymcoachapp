#preprocess_calories.py

from .clean_columns import clean_column
import pandas as pd

def preprocess_calories(df):
    df = clean_column(df)
    df = df.rename(columns={
        "activity_exercise_or_sport_1_hour": "activity",
        "130_lb": "calories_130lb",
        "155_lb": "calories_155lb",
        "180_lb": "calories_180lb",
        "205_lb": "calories_205lb",
        "calories_per_kg": "calories_per_kg_hour"
    })
    for col in ["calories_130lb", "calories_155lb", "calories_180lb", "calories_205lb"]:
        df[col + "_per_min"] = df[col] / 60.0
    df["calories_per_kg_min"] = df["calories_per_kg_hour"] / 60.0
    df["activity_clean"] = df["activity"].str.lower().str.strip()
    return df
