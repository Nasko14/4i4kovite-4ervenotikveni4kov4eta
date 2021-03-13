from flask import Flask, redirect, url_for, render_template, request
import sqlite3
from sqlite3 import Error


def create_connection(db_file):
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
    database = r"C:\Users\Atanas\Desktop\4i4kovite-4ervenotikveni4kov4eta\pythonsqlite.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        # create a new user
        user = (user_name, password, user_type , email)
        user_id = create_users(conn, user)

def save_hive_in_db(user_name, longitude1, latitude1):
    database = r"C:\Users\Atanas\Desktop\4i4kovite-4ervenotikveni4kov4eta\pythonsqlite.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        # create a new hive
        hive = (longitude1, latitude1, user_name)
        create_hive(conn, hive)

""""""

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("homePage.html")

@app.route("/bee_request")
def bee_request():
    return render_template("bee_request.html")

@app.route("/login_signin")
def login_signin():
    return render_template("login_signin.html")

@app.route("/signin", methods=["POST"])
def signin():
    print(request.form)

    save_user_in_db(request.form['name'], request.form['pass'], 
            request.form['user_type'], request.form['email'])
    return render_template("beekeeper.html")

@app.route("/login", methods=["POST"])
def login(): 
    return render_template("farmer.html")
    
if __name__ == "__main__":
    app.run()
