import pandas as pd

def load_all_data():
    return {
        "sym_des": pd.read_csv("data/symtoms_df.csv"),
        "precautions": pd.read_csv("data/precautions_df.csv"),
        "workout": pd.read_csv("data/workout_df.csv"),
        "description": pd.read_csv("data/description.csv"),
        "medications": pd.read_csv("data/medications.csv"),
        "diets": pd.read_csv("data/diets.csv"),
        "severity": pd.read_csv("data/Symptom-severity.csv"),
    }
