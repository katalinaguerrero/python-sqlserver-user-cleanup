from utils.file_utils import read_valid_users, write_sql_file_profile_users
from utils.db_utils import get_connection, get_users_not_in_csv

def main():
    conn = get_connection()
    valid_users = read_valid_users("data/valid_users.csv")
    invalid_users = get_users_not_in_csv(conn, valid_users)
    write_sql_file_profile_users(invalid_users)

    conn.close()

if __name__ == "__main__":
    main()
