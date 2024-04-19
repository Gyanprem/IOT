# import mysql connector
import mysql.connector
import dbconn
conn = dbconn.get_connection()
# create connection with mysql server
query1 = "select * from employee;"
query2 = "select department from employee;"
query3 = "select * from employee order by salary DESC;"
query4 = "select * from employee order by salary ASC;"

# create a cursor to execute query
cursor = conn.cursor()

# execute query using cursor
cursor.execute(query1)
records = cursor.fetchall()     #   returns list of tuples
print(records)
cursor.execute(query2)
records = cursor.fetchall()     #   returns list of tuples
print(records)
cursor.execute(query3)
records = cursor.fetchall()     #   returns list of tuples
print(records)
cursor.execute(query4)
records = cursor.fetchall()     #   returns list of tuples
print(records)
# #cursor.execute(query2)

# get data from cursor


# close the cursor
cursor.close()

# close the connection
conn.close()