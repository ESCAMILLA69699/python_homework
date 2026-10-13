import csv
import traceback

#Task 2
def read_employees():
    mydict = dict()
    mylist = []

    try:
        with open("../csv/employees.csv", "r") as file:
            reader = csv.reader(file)

            for index, row in enumerate(reader):
                if index == 0:
                    mydict["fields"] = row
                else:
                    mylist.append(row)

            mydict["rows"] = mylist

    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        raise SystemExit(1)

    return mydict

employees = read_employees()
print(employees)


#Task 3
def column_index(column_name):
    return employees["fields"].index(column_name)

employee_id_column = column_index("employee_id")



#Task 4
def first_name(row_number):
    index = column_index("first_name")
    name = employees["rows"][row_number][index]
    return name

#Task 5
def employee_find(employee_id):

    def employee_match(row):
        return int(row[employee_id_column]) == employee_id

    matches = list(filter(employee_match, employees["rows"]))

    return matches


#Task 6
def employee_find_2(employee_id):
    lmatch = list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]))
    return lmatch

#Task 7
def sort_by_last_name():
    index = column_index("last_name")
    employees["rows"].sort(key=lambda row: row[index])
    return employees["rows"]

sort_by_last_name()
print(employees)


#Task 8 
def employee_dict(row):
    mydict = dict()

    for index, field in enumerate(employees["fields"]):
        if field != "employee_id":
            mydict[field] = row[index]

    return mydict

print(employee_dict(employees["rows"][0]))


#Task 9
def all_employees_dict():
    mydict = dict()

    for row in employees["rows"]:
        employee_id = row[employee_id_column]
        mydict[employee_id] = employee_dict(row)

    return mydict

print(all_employees_dict())

#Task 10
import os
def get_this_value():
    return os.getenv("THISVALUE")

#Task 11
import custom_module

def set_that_secret(secret):
   custom_module.set_secret(secret)


set_that_secret("Hello im a goat")
print(custom_module.secret)


#Task 12
def read_minutes():
    minutes1 = dict()
    minutes2 = dict()

    mylist1 = []
    mylist2 = []

    with open("../csv/minutes1.csv", "r") as file:
        reader = csv.reader(file)

        for index, row in enumerate(reader):
            if index == 0:
                minutes1["fields"] = row
            else:
                mylist1.append(tuple(row))

        minutes1["rows"] = mylist1

    with open("../csv/minutes2.csv", "r") as file:
        reader = csv.reader(file)

        for index, row in enumerate(reader):
            if index == 0:
                minutes2["fields"] = row
            else:
                mylist2.append(tuple(row))

        minutes2["rows"] = mylist2

    return minutes1, minutes2


minutes1, minutes2 = read_minutes()

print(minutes1)
print(minutes2)


#Task 13
def create_minutes_set():
    myset1 = set(minutes1["rows"])
    myset2 = set(minutes2["rows"])

    myset = myset1.union(myset2)

    return myset


minutes_set = create_minutes_set()
print(minutes_set)

#Task14
from datetime import datetime

def create_minutes_list():
    mylist = list(minutes_set)

    mylist = list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), mylist))

    return mylist


minutes_list = create_minutes_list()
print(minutes_list)
