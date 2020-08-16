import mysql.connector as mysql_connector

mysql_database = mysql_connector.connect(host="localhost", user="root", password="root123")
if mysql_database.is_connected():
    print("Connected")
    cursor = mysql_database.cursor()
    cursor.execute("show databases")
    result = cursor.fetchall()
    print(result)
mysql_database.close()
