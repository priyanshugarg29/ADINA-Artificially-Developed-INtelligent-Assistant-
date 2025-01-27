import csv
row = []
with open("UserCredentials.csv", 'r') as csvfile: 
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                print(row)
                if (row[3]=="oreo" and row[4]=="oreo123"):
                    flag = 1
                    break
            print(row)
