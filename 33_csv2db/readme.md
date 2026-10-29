<your team heading here>

DISCOVERIES:
----------------------------------------------------
* a thing
* another thing
* ...and more
====================================================


QUESTIONS/COMMENTS/CONCERNS:
----------------------------------------------------
Q: a question
Q: another question
C: a comment or concern
====================================================



## Relational Database

DB that stores info as collection of tables.
Field: "Column" data in RDB
RECORD: "Row" in RDB
Data can be linked between tables on field values

## SQL
Language for RDBs to query DBs (add, remove, modify info in DBs)
Implementations
 - SQLite
 - MySQL
 - Oracle
 - IBM DB2 (for more industry use)

## SQLite (an SQL implementation)
relies entirely on function calls in parent program. (no additional server)

## Data Organization
data type to convert entered values to a suggested type
data types: TEXT, INTEGER, REAL, NUMERIC, BLOB
Columns can be given a PRIMARY KEY attribute, denoting every entry in column is unique
Columns can be given a NOT NULL attribute, denoting no entry can be NULL

## SQLite Operations
CREATE TABLE <name> (<column name> <data type>, etcetc...)



INSERT INTO <tblname> VALUES (<field1>, <field2>, etcetc...)

each field needs quotation marks.


SELECT * FROM <tbl_name>

SELECT name FROM tpotusa;

SELECT name FROM tpotusa WHERE id = 0;

returns all rows in table



## SQLite Shell
sqlite3 <dbfilename>
Shell cmds begin with dot

.quit
.tables
.header on|off
.mode column|csv|list|insert|...
.help


## Simple
```python
import sqlite3

db = sqlite.connect("foo") # Check how works

c = db.cursor() # facilitate db ops

c.execute("CREATE TABLE roster(name TEXT, userid INTEGER)")

db.commit()
db.close()
```
