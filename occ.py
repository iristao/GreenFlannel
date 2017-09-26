import csv
import random
occupations_dict = {}
# create an empty dictionary

#with open('occupations.csv') as csvfile:
#	reader = csv.DictReader(csvfile)
#	for row in reader:
#		print(row)

reader = csv.DictReader(open('occupations.csv'))
# open the csv file as a dictionary
for row in reader:
	k, v = row['Job Class'], float(row['Percentage'])
	# key = each element in the 'Job Class' column of the csv file
  	# value = each number in the "Percentage" column of the csv file
        # (typecastsing need to convert String to float)
	occupations_dict[k] = v
	# add keys to the empty dict one by one and match their value slots with the corresponding percentages
	
#print occupations_dict

def getRandOcc():
	x = random.uniform(0,99.8)
	# 'Return a random floating point number N such that a <= N <= b for a <= b and b <= N <= a for b < a'
	for k in occupations_dict:
		 #going through all the keys in the dict
		
		if (x - (occupations_dict.get(k)) < 0):
		# use .get() to get the key's corresponding value
                # compare the value with the random floating point number x
                # if x < percentage, return the percentage's corresponding job title
  
			return k
		else:
		# if x >= percentage, set x to their difference
			x = (x - (occupations_dict.get(k)))
	
# ------- explanation: (using Management as an example) -------
# the possibility of getting a random number between 0 and 99.8 that is less than Management's percentage, 6.1, is 6.1/99.8 --> 0.06112
# that means, there is a 6.11% possiblity that the number returned will be Management, which fillfull the goal to return a job based on its percentage

# on the other hand, the possibility of getting a random number between 6.1 and 99.8 (larger than the given percentage) is as high as (99.8-6.1)/99.8 = 0.9388 --> 93.88%
# that means, there is a 93.88% possibility that x (the random number) will be changed into the difference between x and the given percentage
# for example, if x = 20.
# 20 --> 20 - 6.1
# 20 --> 11.9
# nothing is returned. the for loop will get to the next number. The difference is that, now, 6.1% out of 100% possibility is taken out from the range as x is decreased by 6.1
# thus, the following process will look like this:

# x = 11.9
# x = 11.9 - 5 --> 6.9
# x = 6.9 - 2.7 --> 4.2
# x = 4.2 - 1.7 --> 2.5
# x = 2.5 - 0.9 --> 1.6
# x = 1.6
# 1.6 = 1.6
# return "Community and Socail Service"


print getRandOcc()
print getRandOcc()
print getRandOcc()
print getRandOcc()
print getRandOcc()
print getRandOcc()
print getRandOcc()
print getRandOcc()
print getRandOcc()
print getRandOcc()
