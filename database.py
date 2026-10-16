import mysql.connector
import pandas as pd
from werkzeug.security import generate_password_hash
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="thenewdb12#$",
        database="test",
    )

def register_student(student,password):
    mydb = get_db_connection()
    try:
        mycursor = mydb.cursor()
        password_hash = generate_password_hash(password)
        query = "INSERT INTO Student(stu_id, stu_name, stu_class, password) VALUES (%s, %s, %s,%s)"
        values = (student.student_id, student.name, student.student_class,password_hash)
        mycursor.execute(query, values)
        mydb.commit()
        mycursor.close()
        return True
    except mysql.connector.Error as exc:
        print(f"Database error: {exc}")
        return False
    finally:
        mydb.close()

def get_student_by_id(student_id):
    mydb = get_db_connection()
    mycursor = mydb.cursor()
    query = "SELECT * FROM Student WHERE stu_id = %s"
    mycursor.execute(query, (student_id,))
    student = mycursor.fetchone()
    mycursor.close()
    mydb.close()
    return student

def get_menu_items():
    mydb = get_db_connection()
    mycursor = mydb.cursor()
    query = "SELECT * FROM Menu"
    mycursor.execute(query)
    column_names = [column[0] for column in mycursor.description]
    menu_items = mycursor.fetchall()
    mycursor.close()
    mydb.close()
    return pd.DataFrame(menu_items, columns=column_names)

def update_menu(edited_menu):
    mydb = get_db_connection()
    mycursor = mydb.cursor()
    query = "UPDATE Menu SET price = %s, available = %s WHERE item_id = %s"
    for item in edited_menu.to_dict("records"):
        values = (item["price"], item["available"], item["item_id"])
        mycursor.execute(query, values)
    mydb.commit()
    mycursor.close()
    return True

def get_available_menu():
    mydb= get_db_connection()
    mycursor = mydb.cursor()
    query = "SELECT * FROM Menu WHERE available = 1"
    mycursor.execute(query)
    menu_items = mycursor.fetchall()
    mycursor.close()
    mydb.close()
    return menu_items
