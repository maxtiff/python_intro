import csv
from sys import argv

script, input_filename = argv

#	Open csv file for reading
csv_file = open(input_filename, 'r')
csv_reader = csv.reader(csv_file)

# 	Declare variables of column locations in order to loop through each row and column to map dates with observations.
date_col_num = 0
series_col_num = 1

#	Count the number of columns in the CSV file and then return to the beginning of the file.
ncol = len(next(csv_reader))
print(ncol)
csv_file.seek(0)


#	Loop through each series id to print observations to the file.
while series_col_num < ncol:

	current_row = 0

	#	First, prints header with 'Date' and series id on the first line of the file; then prints each date and matching observation from every row on successive lines.
	for row in csv_reader:
		if current_row == 0:
			header = row
			f = open(header[series_col_num], 'w')
			f.write(header[date_col_num] + "\t" + header[series_col_num] + "\n")
		else:
			f.write(row[date_col_num] + "\t" + row[series_col_num] + "\n")

		current_row += 1

	#	Close the series file
	f.close()
	
	
	# 	Return to the beginning of the CSV file in order to create headers for all series data files.
	csv_file.seek(0)
	#	Move to next column that contains data
	series_col_num += 1

#	Close the CSV file	
csv_file.close()
