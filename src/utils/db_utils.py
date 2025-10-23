import pyodbc
from config import DB_CONFIG

def get_connection():
    print(pyodbc.drivers())
    conn_str = (
        f"DRIVER={DB_CONFIG['driver']};"
        f"SERVER={DB_CONFIG['server']};"
        f"DATABASE={DB_CONFIG['database']};"
        f"UID={DB_CONFIG['username']};"
        f"PWD={DB_CONFIG['password']}"
    )
    return pyodbc.connect(conn_str)

def get_all_users(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT CODIGO_ADI FROM SIADUS_TBACCPRO")
    return [row[0] for row in cursor.fetchall()]

def get_users_not_in_csv_adi(conn, valid_users: list[str]):
    cursor = conn.cursor()
    if not valid_users:
        return []

    placeholders = ",".join("?" for _ in valid_users)
    query = f"""
        SELECT DISTINCT USU_CODIGO
        FROM SIADUS_TBACCADI
        WHERE USU_CODIGO NOT IN ({placeholders})
    """
    cursor.execute(query, valid_users)
    return [row[0] for row in cursor.fetchall()]


def get_users_not_in_csv_pro(conn, valid_users: list[str]):
    cursor = conn.cursor()
    if not valid_users:
        return []

    placeholders = ",".join("?" for _ in valid_users)
    query = f"""
        SELECT DISTINCT CODIGO_ADI
        FROM SIADUS_TBACCPRO
        WHERE CODIGO_ADI NOT IN ({placeholders})
    """
    cursor.execute(query, valid_users)
    return [row[0] for row in cursor.fetchall()]