import csv
with open("./employees.csv" ,"r") as rcsv:
        csv_reader = csv.reader(rcsv)
        print(rcsv) # reads the file and send an object (iterator object )
        
        
        fields = next(rcsv) # gives the first line of the csv file the next function iterates to the next
        fields2 = next(rcsv) # gives the next line of the iteration 
        print(fields)
        print(fields2)