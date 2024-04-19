import mysql.connector
import dbconn
conn = dbconn.get_connection()
empid = int(input("enter empid : "))
name = input("Enter name : ")
department = input("enter department : ")
email = input("enter email: ")
salary = int(input("enter salary: "))
date_of_joining = input("enter date of joining")
query = f"insert into employee value({empid},'{name}','{department}','{email}',{salary},'{date_of_joining}');"
cursor = conn.cursor()
cursor.execute(query)  
conn.commit()
cursor.close()
conn.close()
def delete_employee(empid):
    conn = dbconn.get_connection()
    query = f"delete from employee where empid = %s;"
    val = (empid,)
    cursor = conn.cursor()
    cursor.execute(query, val)
    conn.commit()
    cursor.close()
    conn.close()
delete_employee(1001)

def update_employee(empid, salary):
    conn = dbconn.get_connection()
    query = f"update employee SET salary = %s where empid = %s;"
    val = (salary, empid)
    cursor = conn.cursor()
    cursor.execute(query, val)
    conn.commit()
    cursor.close()
    conn.close()
update_employee(84055, "20000")