import pandas as pd

def read_valid_users(csv_path: str) -> list[str]:
    df = pd.read_csv(csv_path, header=None, names=["username"])
    return df["username"].dropna().tolist()