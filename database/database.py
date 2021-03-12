import sqlite3

conn = sqlite3.connect('users.db')

#create cursor
curr = conn.cursor()

#Create a Table for users
#curr.execute("""CREATE TABLE users (
#    username text,
#    password text,
#    type text,
#    county text
#)""")

#conn.commit()

#Create a Table for hives
#curr.execute("""CREATE TABLE hives (
#   x1 int,
#    y1 int,
#    user text
#)""")

#conn.commit()

#Create a Table for Grounds
#curr.execute("""CREATE TABLE grounds (
#    x1 int,
#    y1 int,
#    x2 int,
#    y2 int,
#    user text
#)""")

conn.commit()

conn.close()