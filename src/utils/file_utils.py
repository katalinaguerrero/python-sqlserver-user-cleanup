import pandas as pd

def read_valid_users(csv_path: str) -> list[str]:
    df = pd.read_csv(csv_path, header=None, names=["username"])
    return df["username"].dropna().tolist()

def write_sql_file_profile_users(invalid_users: list[str], output_path: str = "./SIADUS_TBACCPRO.sql") -> None:
    with open(output_path, "w", encoding="utf-8") as outfile:
        placeholders = ",".join("?" for _ in invalid_users)
        sql = f"""
            SELECT CODIGO_ADI
            FROM SIADUS_TBACCPRO
            WHERE CODIGO_ADI IN ({placeholders})
        """
        outfile.write(sql)
