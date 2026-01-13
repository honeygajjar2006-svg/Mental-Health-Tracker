import pandas as pd

def load_data(path="data/mental_health_dataset.csv"):
    
    try:
        df = pd.read_csv(path)
        return df
    except FileNotFoundError:
        print("⚠️ Dataset not found. Using default empty dataset.")
        return None
