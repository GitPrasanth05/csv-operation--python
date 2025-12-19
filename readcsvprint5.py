# read a csv file and print only 5 rows 
import csv
rows = []

with open("./employees.csv","r") as rcsv:
    csv_reader = csv.reader(rcsv)
    fields= next(csv_reader)
    for line in csv_reader:
        rows.append(line) # appending all the data to the rows -> array 
print(fields) # prints up the title and making it avail

for i in rows[0:5] :# slicing the row till the 5 the index which is the row of  0 , 1 , 3 , 4
    print(i)

"""
    ['EMPLOYEE_ID', 'FIRST_NAME', 'LAST_NAME', 'EMAIL', 'PHONE_NUMBER', 'HIRE_DATE', 'JOB_ID', 'SALARY', 'COMMISSION_PCT', 'MANAGER_ID', 'DEPARTMENT_ID']
['198', 'Donald', 'OConnell', 'DOCONNEL', '650.507.9833', '21-JUN-07', 'SH_CLERK', '2600', ' - ', '124', '50']
['199', 'Douglas', 'Grant', 'DGRANT', '650.507.9844', '13-JAN-08', 'SH_CLERK', '2600', ' - ', '124', '50']
['200', 'Jennifer', 'Whalen', 'JWHALEN', '515.123.4444', '17-SEP-03', 'AD_ASST', '4400', ' - ', '101', '10']
['201', 'Michael', 'Hartstein', 'MHARTSTE', '515.123.5555', '17-FEB-04', 'MK_MAN', '13000', ' - ', '100', '20']
['202', 'Pat', 'Fay', 'PFAY', '603.123.6666', '17-AUG-05', 'MK_REP', '6000', ' - ', '201', '20']
"""