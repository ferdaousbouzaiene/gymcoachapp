#main_preprocessing.py

from .preprocess_exercises import preprocess_exercises
from .preprocess_members import preprocess_members
from .preprocess_calories import preprocess_calories

def preprocess_datasets(exercises, members, calories):
    print("📀📀📀📀📀📀📀📀📀📀📀📀📀📀📀📀📀")
    exercises_clean = preprocess_exercises(exercises)
    print("💄💄💄💄💄💄💄💄💄💄💄💄💄💄💄💄💄")
    members_clean = preprocess_members(members)
    print("🍀🍀🍀🍀🍀🍀🍀🍀🍀🍀🍀🍀🍀🍀🍀🍀🍀")
    calories_clean = preprocess_calories(calories)
    return exercises_clean, members_clean, calories_clean
