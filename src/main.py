from utils.file_utils import read_valid_users, write_sql_file_users, write_sql_file_profile_users
from utils.db_utils import get_connection, get_users_not_in_csv_adi,get_users_not_in_csv_pro

def main():
    conn = get_connection()
    valid_users = read_valid_users("data/valid_users.csv")
    write_sql_file_users( get_users_not_in_csv_adi(conn, valid_users))
    write_sql_file_profile_users(get_users_not_in_csv_pro(conn, valid_users))

    conn.close()

if __name__ == "__main__":
    main()
