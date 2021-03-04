import csv
csv_col=['ID:','Name','Place']
dict_data=[{'ID':1,'Name':'Alex','Place':'Muvattupuzha'}],
{'ID':2,'Name':'Shehara','Place':'Perumbavoor'}
{'ID':3,'Name':'Shri Ram','Place':'alpuzha'}
{'ID':4,'Name':'Smith','Place':'Pathanamthitta'}
csv_file="Names.csv"
try:
    with open("names.csv",'w')as file1:
        writer=csv.dictWriter(file,fieldnames=csv_col)
        writer.writeheader()
        for data1 in dict_data:
            writer.writerow(data1)
except IOError:
                print("I/O error")
                data1=csv.dictReader(open(csv_file))
                print("CSV file as a dictonary:\n")
for row in data1:
                      print(row)
