# ------------------------------------------------------
# -- Advanced_Lessons => Timing Your Code With Timeit --
# ------------------------------------------------------
# - timeit: - Get Execution Time Of Code By Running 1M Time And Give You Minimal Time
# -         - It Used For Performance By Testing All Functionality
# - timeit(stmt, setup, timer, number)
# - timeit(pass, pass, default, 1.000.000) Default Values
# -------------------------------------------------------
# - stmt: Code You Want To Measure The Execution Time
# - setup: Setup Done Before The Code Execution (Import Module Or Anything)
# - timer: The Timer Value
# - number: How Many Execution That Will Run
# -------------------------------------------------------

# from timeit import timeit

# name="Ahmed"

# print(name*1000)

# print(timeit("name = 'Ahmed';name*1000"))


# print(timeit(stmt="random.randint(0,50)",setup="import random"))


# def Calculator():
#      num1=int(input())
#      num2=int(input())
#      return num1 + num2 

# Time_Taken=timeit(stmt=Calculator)

# print(f"Time Taken {Time_Taken} seconds")



# --------------------------------------------------
# -- Advanced_Lessons => Add Logging To Your Code --
# --------------------------------------------------
# - Print Out To Console Or File
# - Print Logs Of What Happens
# ------------------------------
# - DEBUG
# - INFO
# - WARNING
# - ERROR
# - CRITICAL
# ----------
# name => Logging Module Give It To The Default Logger.
# -----------------------------------------------------
# Basic Config
# - level => Level of Severity
# - filename => File Name and Extension
# - mode => Mode Of The File a => Append
# - format => Format For The Log Message
# ------------------------
# getLogger => Return a Logger With the Specified Name

# import logging

# logging.basicConfig(filename="test.app",
#                     filemode="a",
#                     format="(%(asctime)s) | %(name)s | %(levelname)s => '%(message)s'",
#                     datefmt="%d -%B -%Y , %H:%M:%S ",
#                     level=logging.DEBUG)

# logging.warning("This is Waring Message")
# logging.error("This is Error Message")
# logging.debug("This is debug Message")
# logging.info("this is INFO Message")
# logging.critical("This is CRITICAL Message")




