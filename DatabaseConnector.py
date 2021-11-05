import mysql.connector

mydb=mysql.connector.connect(host='localhost',user='root',passwd='',database='ethiomallbot',autocommit=True)
print('it works')