import csv
occupations_dict = {}

#with open('occupations.csv') as csvfile:
#	reader = csv.DictReader(csvfile)
#	for row in reader:
#		print(row)

reader = csv.reader(open('occupations.csv', 'r'))
for row in reader:
	k, v = row
	occupations_dict[k] = v
	
print occupations_dict