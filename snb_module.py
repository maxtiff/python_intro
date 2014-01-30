import csv

def series_id_map(list1, list2):

	'''(list1, list2)->(dictionary)

	This function maps the values of a list to the values of another list and stores them in a dictionary
	that the function then returns.

	Example:
	>>>series_id_map(titles,series_ids)
	series_dict = {'Example Title': 'exsrsid00', 'Another Title': 'anthrsid01', etc ...}
	
	'''

def create_data_files(series_file):

	'''(single csv file)->(multiple data files)

	This function takes a horizontally oriented csv file with multiple data columns and
	creates an equal number of time-series data files.

	Example:
	>>>create_data_files('example.csv')
	Created exsrsid00, anthrsid01.

	'''
	#	Open csv file for reading
	csv_file = open(series_file, 'r')
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
