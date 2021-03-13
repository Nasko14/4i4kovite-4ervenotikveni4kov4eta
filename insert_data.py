import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def create_users(conn, users):
    sql = ''' INSERT INTO users(username, pass, user_type, email)
              VALUES(?, ?, ?, ?) '''
    cur = conn.cursor()
    cur.execute(sql, users)
    conn.commit()
    return cur.lastrowid

def create_hive(conn, hives):
    sql = ''' INSERT INTO hives(longitude1, latitude1, username)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, hives)
    conn.commit()
    return cur.lastrowid

def save_user_in_db(user_name, password, user_type, email):
    database = r"C:\Users\Atanas\Desktop\Test-repo2\pythonsqlite.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        # create a new user
        user = (user_name, password, user_type , email)
        user_id = create_users(conn, user)

def save_hive_in_db(user_name, longitude1, latitude1):
    database = r"C:\Users\Atanas\Desktop\Test-repo2\pythonsqlite.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        # create a new hive
        hive = (longitude1, latitude1, user_name)
        create_hive(conn, hive)

"""
def main():
    save_in_db()

if __name__ == '__main__':
    main()
"""