import csv

csv_col=['ID','Name','Place']

dict_data=[{'ID':1,'Name':'Anjana','Place':'thrissur'},

           {'ID':2,'Name':'anagha','Place':'wayanad'},

           {'ID':3,'Name':'aiswarya','Place':'kannur'},

           {'ID':4,'Name':'swathisha','Place':'thrissur'},

           {'ID':5,'Name':'swetha','Place':'kannur'},

           {'ID':6,'Name':'salima','Place':'kannur'},

           {'ID':7,'Name':'kavya','Place':'kottayam'},

           {'ID':8,'Name':'selmi','Place':'kottayam'},

           {'ID':9,'Name':'adhithya','Place':'kannur'},

           {'ID':10,'Name':'anjanakp','Place':'palakkad'},]



csv_file="Names.csv"

try:

    with open(csv_file,'w')as file1:

        writer=csv.DictWriter(file1,fieldnames=csv_col)

        writer.writeheader()

        for data1 in dict_data:

            writer.writerow(data1)



except IOError:

    print("ioeror")



data1=csv.DictReader(open(csv_file))

print("csv file as dictionary:\n")

for row in data1:

    print(row)
