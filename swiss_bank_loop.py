import csv
from sys import argv

script, input_file = argv

#	Open csv file for reading
csv_file = open(input_file, 'r')
csv_reader = csv.reader(csv_file)

# Declare row and column variables in order to loop through each row and column to map dates with observations.
current_row = 0
date_colnum = 0
series_colnum = 1

#	Loop through first column and print the 'Date' header and all dates in the column.
for row in csv_reader:
	if current_row == 0:
		header = row
		print(header[date_colnum] + "\t" + header[series_colnum])
	else:
		print (row[date_colnum] + "\t" + row[series_colnum])

	current_row += 1	
			
csv_file.close() 
