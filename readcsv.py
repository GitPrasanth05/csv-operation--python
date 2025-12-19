import csv
with open("./employees.csv" ,"r") as rcsv: # open the file in the reader mode 
        csv_reader = csv.reader(rcsv)
        # csv_reader = csv.reader(rcsv , skipinitialspace=True ,quoting=csv.QUOTE_ALL) if u add this skipinitialspace it will does skip the additional extra spaces in between area  
        # quote all is used to take care of the quotes in the csv file 


        print(rcsv) # reads the file and send an object (iterator object )
        
        
        fields = next(rcsv) # gives the first line of the csv file the next function iterates to the next
        fields2 = next(rcsv) # gives the next line of the iteration 
        fields3 = next(csv_reader)
        fields4 = next(csv_reader)

        """ check all the files and print the read lines in a format print for knowing those formats   """
        print(fields) 
        print(fields2)
        print(fields3)
        print(fields4)

        for line in csv_reader:
                print(line)  # used to print all line in from the csv 
                print(line[0]) # print the first line alone 
        
