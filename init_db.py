import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO atmosphere (tim, temperature, humidite, pression) VALUES (?, ?, ?, ?)",
            ('10h00', 15, '40%', 1.3)
            )
cur.execute("INSERT INTO atmosphere (tim, temperature,humidite,pression) VALUES (?, ?, ?,?)",
            ('10h20', 16, '50%', 1.4)
            )

connection.commit()
connection.close()
