#a Python script for interacting with an SQLite db:
import sqlite3 #enable SQLite operations

#open db if exists, otherwise create
db = sqlite3.connect("foo")

c = db.cursor() #facilitate db ops

c.execute("CREATE TABLE IF NOT EXISTS roster(name TEXT, userid INTEGER);")
c.execute("INSERT INTO roster VALUES (\"\", \"234329\");")


db.commit() #save changes
db.close()