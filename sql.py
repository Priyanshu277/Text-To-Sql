import sqlite3 

# Connect to sqlite
connection=sqlite3.connect("student.db")

#Create a cursor object to insert record, create table, retrieve
cursor = connection.cursor()

#Create the table
table_info= """
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARHCAR(25),MARKS INT);
"""

cursor.execute(table_info)

#insert some more records

cursor.execute('''Insert Into STUDENT Values('Krish','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT Values('Sudhanshu','Data Science','B',100)''')
cursor.execute('''Insert Into STUDENT Values('Darius','Data Science','A',86)''')
cursor.execute('''Insert Into STUDENT Values('Vikas','Dev Ops','A',50)''')
cursor.execute('''Insert Into STUDENT Values('Dipesh','Dev Ops','A',35)''')

connection.commit()
connection.close()



