import csv

def read_input():
	#read the csv file, making a list of each row in the csv file. Data read as strings
	rows = []
	with open('mnist/mnist_sample.csv') as csvfile:
		readCSV = csv.reader(csvfile, delimiter=',')
		for row in readCSV:
			rows.append(row)

	#convert all data to int.
	data = []
	for row in rows:
		temp = []
		for item in row:
			temp.append(int(item))
		data.append(temp)

	#obtain labels from the file
	labels = []
	for i in range(len(data)):
		labels.append(data[i][0])

	print("The labels are:",labels)

	#obtain pixel data from the file
	pixels = []
	for i in range(len(data)):
		temp = []
		for j in range(1,len(data[i])):
			temp.append(data[i][j])
		pixels.append(temp)

	return(pixels, labels)