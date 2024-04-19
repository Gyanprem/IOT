import mysql.connector
connection = mysql.connector.connect(
    host = "localhost",
    port = 3306,
    user = "sunbeam",
    password = "sunbeam",
    database = "iotdb"
)
empid = int(input("enter empid : "))
name = input("Enter name : ")
department = input("enter department : ")
email = input("enter email: ")
salary = int(input("enter salary: "))
date_of_joining = input("enter date of joining")
query = f"insert into employee value({empid},'{name}','{department}','{email}',{salary},'{date_of_joining}');"

cursor = connection.cursor()
cursor.execute(query)  
connection.commit()
cursor.close()
connection.close()