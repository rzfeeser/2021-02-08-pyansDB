#!/usr/bin/python3
import pyodbc 

conn = pyodbc.connect('DRIVER={MariaDB};User=root;Password=mysecretpassword;Server=127.0.0.1;Port=33306')
cursor = conn.cursor()                                            
cursor.execute("CREATE DATABASE newestDemo;")                                   

cursor.execute("SHOW DATABASES;")                                      

result = cursor.fetchall()                                              

print(result)
