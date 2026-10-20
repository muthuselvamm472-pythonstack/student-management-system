import sqlite3

def connect():
    return sqlite3.connect("student.db")

def create_table():
    con=connect()
    cur=con.cursor()
    cur.execute(""" CREATE TABLE IF NOT EXISTS STUDENT_TABLE(
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    NAME VARCHAR(20) NOT NULL,
                    EMAIL VARCHAR(100) UNIQUE,
                    COURSE VARCHAR(30),
                    MARK REAL CHECK(MARK>=0 AND MARK<=100)) """)
    con.commit()
    con.close()

def add_student(NAME,EMAIL,COURSE,MARK):
    con=connect()
    cur=con.cursor()
    try:
        cur.execute(" INSERT INTO STUDENT_TABLE(NAME,EMAIL,COURSE,MARK) VALUES (?,?,?,?)", (NAME,EMAIL,COURSE,MARK))
        con.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        con.close()


def view_student():
    con=connect()
    cur=con.cursor()
    try:
        cur.execute("""SELECT * FROM STUDENT_TABLE""" )
        res=cur.fetchall()
        return res
    finally:
        con.close()


def search_student(ID):
    con=connect()
    cur=con.cursor()
    try:
        cur.execute("""SELECT * FROM STUDENT_TABLE WHERE ID=?""",(ID,))
        rows=cur.fetchone()
        return rows
    finally:
        con.close()


def update_student(NAME,EMAIL,COURSE,MARK,ID):
    con=connect()
    cur=con.cursor()
    try:
        cur.execute("""UPDATE STUDENT_TABLE
                        SET NAME=?,EMAIL=?,COURSE=?,MARK=? WHERE ID=?""",(NAME,EMAIL,COURSE,MARK,ID))
        con.commit()
        return cur.rowcount
    except sqlite3.IntegrityError:
        return None
    finally:
        con.close()

def delete_student(ID):
    
    con=connect()
    cur=con.cursor()
    try:
        cur.execute("""DELETE FROM STUDENT_TABLE WHERE ID=?""",(ID,))
        con.commit()
        return cur.rowcount
    finally:
        con.close()
    


