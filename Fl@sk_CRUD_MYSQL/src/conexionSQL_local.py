import mysql.connector

conexion = mysql.connector.connect(user="root", password="Chelsea@01", host="localhost", 
database= "sql_store", port="3306")

print (conexion)
