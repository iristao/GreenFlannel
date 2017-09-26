from flask import Flask, render_template
import csv
import random
occupations_dict = {}

reader = csv.DictReader(open('occupations.csv'))
for row in reader:
	k, v = row['Job Class'], float(row['Percentage'])
	occupations_dict[k] = v

app = Flask(__name__)

@app.route('/')

def root():
        return 'Visit the "/occupations" route for more information'

@app.route('/occupations')

def occupations():
    return render_template("table.html", foo = occupations_dict, woo = getRandOcc())  

def getRandOcc():
    x = random.uniform(0,99.8)
    for k in occupations_dict:
	if (x - (occupations_dict.get(k)) < 0):
	    return k
	else:
	    x = (x - (occupations_dict.get(k)))

if __name__ == '__main__':
    app.debug = True
    app.run()
