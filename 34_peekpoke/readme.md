# K34: More Tables More Problems
Team: GOD BLESS AMERICA
Roster: Leon Wong, Lucas Ou

## DISCOVERIES

- `wc` returns the line count, word count, and character count of a file. 
    This is useful for checking if any data gets lost or anything unintentional happens following editing a file with a program.
- `cursor.fetchone()` retrieves one row, while `cursor.fetchall()` retrieves all matching rows.
- `DROP TABLE IF EXISTS` removes an old table if it exists, allowing the script to recreate it.
- `PRIMARY KEY` makes each course code unique in the course_info table.
- `JOIN` combines records from two tables based on a matching column.
- The courses table contains individual grades, while course_info contains information about each course.

## QUESTIONS/COMMENTS/CONCERNS

- Q: Should course_info get its courses from the CSV or the existing table?

`cursor.fetchall()`
https://pytutorial.com/python-sqlite3-fetchall-fetch-all-query-results/

`cursor.fetchone()`
https://pytutorial.com/python-sqlite3-fetchone-fetch-query-row-guide/