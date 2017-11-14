# Read data from csv file and do whatever you wish

import csv

with open('SampleCsv.csv') as sampleCsv:
    data = csv.reader(sampleCsv, delimiter=',')
    employee = []
    dob = []
    for row in data:
        print(row)
        print(row[0],row[1],row[2])
        employee.append(row[1])
        dob.append(row[2])
    try:
        emp = input("Whose date of birth do you wish to know? ")
        empIndex = employee.index(emp)
        print("Date of birth of ", emp, " is - ", dob[empIndex])
    except Exception as e:
        print(e)


