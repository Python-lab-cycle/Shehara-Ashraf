import csv
with open('emp.csv',newline='')as csvfile1:
    data=csv.DictReader(csvfile1)
    print("Emp NO: Emp Name")
    print("-----------")
    for row in data:
        print(row['Emp NO:'],row['Emp Name'])
        
