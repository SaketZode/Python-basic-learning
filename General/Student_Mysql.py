import mysql.connector as mysql_connector


class Student:
    def __init__(self, name, college, email):
        self.name = name
        self.college = college
        self.email = email

    def __str__(self):
        return "Name : {}  College : {}  Email : {}".format(self.name, self.college, self.email)

    def __repr__(self):
        return str(self)


database = mysql_connector.connect(host="127.0.0.1", user="root", password="root123", database="demo")

if database.is_connected():
    cursor = database.cursor()
    cursor.execute("SELECT * FROM student")
    data = cursor.fetchall()
    students = []
    for row in data:
        name = row[0]
        college = row[1]
        email = row[2]
        student = Student(name, college, email)
        students.append(student)
    print(students)
    cursor.close()
    database.close()
