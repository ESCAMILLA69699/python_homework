import csv

employees = []

with open("../csv/employees.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        employees.append(row)

names = [row[0] + " " + row[1] for row in employees[1:]]
print(names)

e_names = [name for name in names if "e" in name]
print(e_names)
