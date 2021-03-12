import sqlite3

conn = sqlite3.connect('database.db')

with open('schema.sql') as f:
    conn.executescript(f.read())

cur = conn.cursor()

# Adding elements manually

cur.execute("INSERT INTO users (username, pass, user_type) VALUES (?, ?, ?)", 
    ('Gosho1', '1234', 'farmer'))
cur.execute("INSERT INTO users (username, pass, user_type) VALUES (?, ?, ?)", 
    ('Gosho2', '12345', 'beekeeper'))


cur.execute("INSERT INTO hives (x1, y1, user) VALUES (?, ?, ?)", (100, 123, 'Gosho2'))

cur.execute("INSERT INTO grounds (x1, y1, x2, y2, user) VALUES (?, ?, ?, ?, ?)", (100, 200, 300, 400, 'Gosho1'))

conn.commit()
conn.close()
