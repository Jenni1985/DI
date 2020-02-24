import sqlite3

sqlite_file = 'class.db'    # name of the sqlite database file
table_name = 'students'   # name of the table to be queried

conn = sqlite3.connect(sqlite_file)

# def Sql_Fetch(conn):
#     Cursor_Obj = conn.cursor()
#     #Cursor_Obj.execute('SELECT Last_name, First_name FROM students WHERE id=2')
#     #Cursor_Obj.execute("SELECT First_name, Last_name FROM students WHERE First_name LIKE'%a%'; ")
#     #Cursor_Obj.execute("SELECT First_name FROM students WHERE First_name LIKE'a%';")
#     Cursor_Obj.execute("SELECT First_name, Last_name FROM students WHERE id=1 OR id=3")
#      Cursor_Obj.execute("UPDATE students SET birth_date = '1998-11-02' WHERE last_name = 'Dupont'")
#     Cursor_Obj.execute("DELETE FROM students WHERE id = 6;")
#     rows = Cursor_Obj.fetchall();
#     for row in rows:
#         print(row)
#
#
# Sql_Fetch(conn)
#SELECT first_name, last_name FROM students WHERE id = 1 OR id =3;
#4.Fetch only the student where the last_name is equal to Dupont AND the first_name is equal to Marc (show his first_name and last_name)
#Fetch the students which first_name contains the letter “a”. (show their first_name and * last_name)
#Fetch the students which first_name starts with the letter “a”. (show their first_name and last_name)
#Fetch the students which first_name starts with the letter “a”. (show their first_name and last_name)
#Fetch the students which first_name ends with the letter “a”. (show their first_name and last_name)
#Fetch the students which the id are 1 and 3. (show their first_name and last_name)

#Update
#I made a mistake when I inserted lea Dupont. The first letter of her first_name is in lower case. Update it to convert it to upper case
#Marc and Lea Dupont are twins. Change at the same time, their birth_date to 02/11/1998.
# Delete
# Delete Lea Dupont by her id, she is not a student anymore
def Sql_Update(conn):
    Cursor_Obj = conn.cursor()
    Cursor_Obj.execute("DELETE FROM students WHERE id = 6;")
    rows = Cursor_Obj.fetchall();
    for row in rows:
        print(row)
Sql_Update(conn)