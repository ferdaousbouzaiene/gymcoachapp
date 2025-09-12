#preprocess_members.py
from .clean_columns import clean_column
import pandas as pd

def preprocess_members(df):
    # Rename columns using raw names
    df = clean_column(df)
    print('_____________11111______________________')
    df = df.rename(columns={
        "weight_(kg)": "weight",
        "height_(m)": "height",
        "session_duration_(hours)": "session_duration_hours",
        "workout_frequency_(days/week)": "workout_frequency_per_week",
        "water_intake_(liters)": "water_intake_liters"
    })
    print('_____________11111______________________')

    # Convert numeric columns
    numeric_cols = [
        "age", "weight", "height", "max_bpm", "avg_bpm", "resting_bpm",
        "session_duration_hours", "calories_burned", "fat_percentage",
        "water_intake_liters", "workout_frequency_per_week", "bmi"
    ]
    print('_____________11111______________________')

    df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors="coerce")
    print('_____________11111______________________')

    # Normalize workout type
    df["workout_type"] = df["workout_type"].str.lower().str.strip()

    return df
