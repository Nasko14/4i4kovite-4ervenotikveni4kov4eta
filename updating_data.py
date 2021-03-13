import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def update_users(conn, user):
    sql = ''' UPDATE users
                username = ? ,
                pass = ? ,
                user_type = ?
            '''
    cur = conn.cursor()
    cur.execute(sql, user)
    conn.commit()

#def update_users(conn, task):
#    """
#    update priority, begin_date, and end date of a task
#    :param conn:
#    :param task:
#    :return: project id
#    """
#    sql = ''' UPDATE tasks
#              SET priority = ? ,
#                  begin_date = ? ,
#                  end_date = ?
#              WHERE id = ?'''
#    cur = conn.cursor()
#    cur.execute(sql, task)
#    conn.commit()

#def update_users(conn, task):
#    """
#    update priority, begin_date, and end date of a task
#    :param conn:
#    :param task:
#    :return: project id
#    """
#    sql = ''' UPDATE tasks
#              SET priority = ? ,
#                  begin_date = ? ,
#                  end_date = ?
#              WHERE id = ?'''
#    cur = conn.cursor()
#    cur.execute(sql, task)
#    conn.commit()

def main():
    database = r"C:\Users\Atanas\Desktop\Test-repo2\pythonsqlite.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        update_users(conn, ('Gosho1', '123456', 'farmer'))


if __name__ == '__main__':
    main()