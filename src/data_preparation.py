import pandas as pd

def clean_columns(df):
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
        .str.replace("(", "")
        .str.replace(")", "")
    )
    return df


def preprocess_datasets(exercises, members, calories):
    # Clean column names
    exercises = clean_columns(exercises)
    members = clean_columns(members)
    calories = clean_columns(calories)
    print("____________________________________________")
    ### --- exercises_data  --- ###
    # --- Standardize Exercises Dataset ---
    exercises = exercises.rename(columns={
        "level": "difficulty",
        "bodypart": "body_part"
    })
    exercises = exercises.drop(columns=["ratingdesc"], errors="ignore")
    exercises = exercises[["title", "type", "body_part", "equipment", "difficulty", "desc"]]
    exercises["exercise_name_clean"] = exercises["title"].str.lower().str.strip()

    ### --- Calories_data  --- ###
    # --- Standardize Calories Dataset ---
    calories = calories.rename(columns={
        "activity_exercise_or_sport_1_hour": "activity",    
        "130_lb": "calories_130lb",
        "155_lb": "calories_155lb",
        "180_lb": "calories_180lb",
        "205_lb": "calories_205lb",
        "calories_per_kg": "calories_per_kg_hour"
    })
    for col in ["calories_130lb","calories_155lb","calories_180lb","calories_205lb"]:
        calories[col+"_per_min"] = calories[col]/60.0
    calories["calories_per_kg_min"] = calories["calories_per_kg_hour"]/60.0
    calories.head()
    calories["activity_clean"] = calories["activity"].str.lower().str.strip()
    
    ### --- Members_data  --- ###
    # --- Standardize Members Dataset ---
    members = members.rename(columns={
        "weight_(kg)": "weight",
        "height_(m)": "height",
        "session_duration_(hours)": "session_duration_hours",
        "workout_frequency_(days/week)": "workout_frequency_per_week",
        "water_intake_(liters)": "water_intake_liters"
    })
    numeric_cols = [
        "age", "weight", "height", "max_bpm", "avg_bpm", "resting_bpm",
        "session_duration_hours", "calories_burned", "fat_percentage",
        "water_intake_liters", "workout_frequency_per_week", "bmi"
    ]
    members[numeric_cols] = members[numeric_cols].apply(pd.to_numeric, errors="coerce")
    members["workout_type"] = members["workout_type"].str.lower().str.strip()

    return exercises, members, calories
