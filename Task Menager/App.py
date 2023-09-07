# MY Task Manager

# Create Database

import sqlite3

Data_App = sqlite3.connect("App.db")
cursor = Data_App.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Plan(Task_order INT, name_Task TEXT, date DATE, Time INT,  execution TEXT)")

def Commit_And_closed():

   Data_App.commit()
   Data_App.close()
     


# Select From this list
Control_List="""
a =>add New Task
m => Modification Task
d => Delete Task
s => Show Current Task
q => quit the App
Select From this list:
"""

# user Input
user_input=input(Control_List).strip().lower()


commed_list=['a','M','d','s','q']


def add_Task():
    """
    This Methods To Add Task
    """
    Task_order=int(input("Enter Number Task: "))
    name_Task=input("Enter Name Task: ")
    date=input("What date You Start Task: ")
    time=input("What time Do Start Task:  ")
    excution=input("DO you  Start Task: ")

    Task_done=input("Do You Finish The Task: ")
    if Task_done == "yes":
        print("Very Good Do you add other plan ?")
    else:
        print("You should finish The Task: ")

    cursor.execute(f"INSERT INTO Plan(Task_order, name_Task, date, Time,  execution) Values('{Task_order}','{name_Task}','{date}','{time}','{excution}')")
    
    
    Commit_And_closed()
def modify_Task():
    """
    This methods To Modify Task
    """
    pass
def delete_Task():
      """
    This methods To Delete Task
    """
      pass
def show_Task():
    """
    This methods to show Tasks
    """
    pass

# Check Commend list
if user_input =='a':
    add_Task()

