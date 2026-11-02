#Leon Wong (me) and Lucas Ou
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

studentList = getRecordsFromCSV("students-beeg.csv")

# Input data into our db.
c.execute("DROP TABLE IF EXISTS students;") # Delete old table
c.execute("CREATE TABLE IF NOT EXISTS students (name TEXT, age INTEGER, id INTEGER PRIMARY KEY);")

for student in studentList:
    c.execute(f"INSERT INTO students VALUES (\"{student['name']}\", \"{student['age']}\", \"{student['id']}\");")

courseList = getRecordsFromCSV("courses-beeg.csv")

c.execute("DROP TABLE IF EXISTS courses;")
c.execute("CREATE TABLE IF NOT EXISTS courses (code TEXT, mark INTEGER, id INTEGER);")

for course in courseList:
    c.execute(f"INSERT INTO courses VALUES (\"{course['code']}\", \"{course['mark']}\", \"{course['id']}\");")


# Print out our data
print("\nList of all students:")
c.execute("SELECT * FROM students;")
while True:
    row = c.fetchone()
    if row is None:
        break
    print(f"Name: {row[0]} Age: {row[1]} ID: {row[2]}")

print("\nList of all courses:")
c.execute("SELECT * FROM courses;")
while True:
    row = c.fetchone()
    if row is None:
        break
    print(f"Code: {row[0]} Mark: {row[1]} ID: {row[2]}")
    
print("\nStudents over age 50:")
c.execute("SELECT * FROM students WHERE age > 50;")
while True:
    row = c.fetchone()
    if row is None:
        break
    print(f"Name: {row[0]} Age: {row[1]} ID: {row[2]}")

studentID = 694
c.execute(f"SELECT * FROM students WHERE id = {studentID};")
studentName = c.fetchone()[0] # Get the student's name
print(f"\nListing all of {studentName}'s (StudentID {studentID}) grades")
c.execute(f"SELECT * FROM courses WHERE id = {studentID};")
while True:
    row = c.fetchone()
    if row is None:
        break
    print(f"Course: {row[0]} Mark: {row[1]} ID: {row[2]}")

courseCode = "systems"
c.execute(f"SELECT * FROM courses WHERE code = \"{courseCode}\";")
marks = c.fetchall()
print(f"\nListing all of {courseCode}'s students")
for mark in marks:
    c.execute(f"SELECT * FROM students WHERE id = {mark[2]}")
    s = c.fetchone()
    print(f"Name: {s[0]} Age: {s[1]} ID: {s[2]}")


# Create course_info table
c.execute("DROP TABLE IF EXISTS course_info;")
c.execute("CREATE TABLE course_info (code TEXT PRIMARY KEY, title TEXT, credits INTEGER, dept TEXT);")

courseInfo = [
    ("systems", "Computer Systems", 3, "CS"),
    ("softdev", "Software Development", 3, "CS"),
    ("ethics", "Ethics", 3, "Philosophy"),
    ("bio", "Biology", 4, "Science"),
    ("ai", "Artificial Intelligence", 3, "CS"),
    ("geometry", "Geometry", 3, "Math"),
    ("greatbooks", "Great Books", 3, "English"),
    ("european cinema", "European Cinema", 3, "Film"),
    ("orgo", "Organic Chemistry", 4, "Science"),
    ("ceramics", "Ceramics", 3, "Art")
]

for course in courseInfo:
    c.execute("INSERT INTO course_info VALUES (?, ?, ?, ?);", course)

#==========================================================

db.commit() #save changes
db.close()  #close database
