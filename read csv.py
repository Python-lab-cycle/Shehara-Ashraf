import csv
with open('emp.csv','r') as file:
    reader=csv.reader(file1)
    for row in reader:
        print(row)
