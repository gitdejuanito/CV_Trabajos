import mysql.connector

conexion = mysql.connector.connect(user="", password="", host="localhost", 
database= "sql_store", port="3306")

print (conexion)
