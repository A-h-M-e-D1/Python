# import sqlite3

# connect with DataBase

# connection = sqlite3.connect('test.db')

# print(type(connection))

# create the database in temporary memory

# connection = sqlite3.Connection(':memory:')

# cursor = connection.cursor()

# create_data = cursor.execute('CREATE TABLE employe (name TEXT , age INT , salary INT)')

# add_data = cursor.execute("INSERT INTO employe Values('ahmed','18','300000')")
# add_data = cursor.execute("INSERT INTO employe Values('Ali','19','300000')")
# add_data = cursor.execute("INSERT  INTO employe Values('Mo','21','300000')")
# add_data = cursor.execute("INSERT  INTO employe Values('D','30','300000')")
# add_data = cursor.execute("INSERT  INTO employe Values('c','50','300000')")
# add_data = cursor.execute("INSERT  INTO employe Values('a','16','300000')")
# add_data = cursor.execute("INSERT  INTO employe Values('eng','34','300000')")
# connection.commit()

# طرق اخري لاضافه بيانات

# conn = sqlite3.connect('student.db')

# cur = conn.cursor()

# student_values = (
#     ('ahmed','arbic',18),
#     ('ali','math',20),
#     ('mohamed','english',23),

# )

# add_data = cur.execute('CREATE TABLE student(name TEXT,object TEXT,grades INT)')

# insert_data = cur.executemany("INSERT INTO student values(?,?,?)",student_values)

# conn.commit()

# Get person data from user

# first_name = input("Enter Your First name: ")
# last_name = input("Enter Your last name: ")
# age = int(input("Enter Your age: "))

# Excute insert statment for supplied person data

# conn = sqlite3.connect('app.db')
# cur = conn.cursor()

# add_data = cur.execute('CREATE TABLE people(first_name TEXT,last_name TEXT,age INT)')

# data = (first_name,last_name,age)

# ins_data = cur.execute(f"INSERT INTO people Values(?,?,?);",data)

# conn.commit()


# SQLite Retrieve Data From Database

# conn = sqlite3.connect('exercise.db')

# cur = conn.cursor()

# creat_table = cur.execute("CREATE TABLE student1(course TEXT,prograss INT)")

# data = (
#     ('python',50),
#     ('html',90),
#     ('css',70),
#     ('js',66),
# )

# add_data = cur.executemany('INSERT INTO student1 Values(?,?)',data)
# conn.commit()
# # fetch 
# Retrieve = cur.execute("SELECT course,prograss FROM student1 WHERE prograss")

# for row in Retrieve.fetchone():
#     print(row)

# for row in cur.fetchall():
#     print(row)


# simple project 
# import sqlite3
# from sqlite3 import Error


# class main:
#      def __init__(self) -> None:
#          self.conn = sqlite3.connect("task.db")
#          self.cur = self.conn.cursor()

# class create_table(main):
#      def create(self):
#          self.cur.execute("CREATE TABLE Tasks(ip INT,task_name TEXT)")
#          self.conn.commit()

# class insert_data(main):
#      data =(
#          (1,'math'),
#          (2,'English'),
#          (3,'r'),
#          (4,'py'),
#          (5,'cs'),
#          (6,'js'),
#      )

#      def insert(self,data):
#          self.cur.executemany("INSERT INTO Tasks Values(?,?)",data)
#          self.conn.commit()

# class quary_data(main):
#      def select(self):
#          self.cur.execute("SELECT ip,task_name From Tasks")
#          data = self.cur.fetchall()
#          return data
    

# conn = sqlite3.connect('task.db')
# cur = conn.cursor()

# table_create = create_table(conn,cur)

# table_create.create()


# update and delect data

# import sqlite3

# conn = sqlite3.connect('web.db')

# cur = conn.execute('CREATE TABLE IF NOT EXISTS detail(ip INT , name TEXT,age INT)')

# data = (
#     (1,'ahmed',30),
#     (2,'mohamed',20),
#     (3,'ali',40),
#     (4,'ibrahim',25),

)

# ins_data = cur.executemany("INSERT  OR IGNORE INTO detail Values(?,?,?)",data)

# update_data = cur.execute("UPDATE OR IGNORE detail SET  ip=5 where  age = 20")
# update_data = cur.execute("UPDATE  OR IGNORE detail SET name = 'CY' WHERE ip = 5 ")

# delet_data = cur.execute("DELETE FROM detail WHERE age = 40")


# selcet_data = cur.execute("SELECT age,name FROM detail WHERE age >20")

# for age in selcet_data.fetchone():
#      print(age)

# conn.commit()
# conn.close()





