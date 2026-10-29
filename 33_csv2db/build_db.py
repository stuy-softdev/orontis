#Clyde "Thluffy" Sinclair
#Software Development
#skeleton/stub :: SQLITE3 BASICS
#Oct 2026

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================


"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
< < < INSERT YOUR TEAM'S DB-POPULATING CODE HERE > > >
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Below, you will find a bit more scaffolding.
USAGE:
As you address each piece of functionality, 
 "talk shop" as you design it, 
 TEST it in sqlite3 shell, 
 then...
"""

def getRecordsFromCSV(filename):
    """Gets data from a CSV file by row.

    Args:
        filename: The name of the CSV file

    Returns:
        A list of dictionaries for each row, with keys dependent on CSV's first row / heading.
    """
    temp = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            temp.append(row)
    return temp

studentList = getRecordsFromCSV("students.csv")

c.execute("CREATE TABLE IF NOT EXISTS students (name TEXT, age INTEGER, id INTEGER);")

for student in studentList:
    c.execute(f"INSERT INTO students VALUES (\"{student['name']}\", \"{student['age']}\", \"{student['id']}\");")

courseList = getRecordsFromCSV("courses.csv")

c.execute("CREATE TABLE IF NOT EXISTS courses (code TEXT, mark INTEGER, id INTEGER);")

for course in courseList:
    c.execute(f"INSERT INTO courses VALUES (\"{course['code']}\", \"{course['mark']}\", \"{course['id']}\");")

command = ""          # <-- insert tested stmt in quotes
c.execute(command)    # run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database
