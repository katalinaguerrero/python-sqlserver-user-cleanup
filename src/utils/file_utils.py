import pandas as pd

def read_valid_users(csv_path: str) -> list[str]:
    df = pd.read_csv(csv_path, header=None, names=["username"])
    return df["username"].dropna().tolist()

def write_sql_file_users(invalid_users: list[str], output_path: str = "./output/SIADUS_TBACCADI.sql") -> None:
    if not invalid_users:
        return

    with open(output_path, "w", encoding="utf-8") as outfile:
        for user in invalid_users:
            user_clean = user.strip()
            if not user_clean:
                continue 
            sql = f"UPDATE SIADUS_TBACCADI SET USU_ESTADO = 'NH' WHERE USU_CODIGO = '{user_clean}';"
            outfile.write(sql + "\n")

def write_sql_file_profile_users(invalid_users: list[str], output_path: str = "./output/SIADUS_TBACCPRO.sql") -> None:
    if not invalid_users:
        return

    with open(output_path, "w", encoding="utf-8") as outfile:
        for user in invalid_users:
            user_clean = user.strip()
            if not user_clean:
                continue 
            sql = f"DELETE FROM SIADUS_TBACCPRO WHERE RTRIM(LTRIM(CODIGO_ADI)) = '{user_clean}';"
            outfile.write(sql + "\n")