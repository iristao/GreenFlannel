from flask import Flask, render_template
import csv
import random
occupations_dict = {}



linkL = ['http://www.careers-in-business.com/management/', 'https://www.bls.gov/oes/current/oes130000.htm','https://www.bls.gov/oes/current/oes150000.htm','https://www.bls.gov/ooh/architecture-and-engineering/home.htm','https://www.bls.gov/oes/current/oes190000.htm','https://www.bls.gov/ooh/community-and-social-service/home.htm','https://www.bls.gov/ooh/legal/home.htm','https://www.bls.gov/ooh/education-training-and-library/home.htm','https://www.bls.gov/oes/current/oes270000.htm','https://www.bls.gov/oes/current/oes290000.htm','https://www.healthcaresupport.com','https://www.bls.gov/ooh/protective-service/home.htm','https://www.bls.gov/ooh/food-preparation-and-serving/home.htm','https://www.bls.gov/oes/current/oes370000.htm','https://www.bls.gov/ooh/personal-care-and-service/home.htm','https://www.bls.gov/ooh/sales/home.htm','https://www.bls.gov/ooh/office-and-administrative-support/home.htm','https://www.bls.gov/ooh/farming-fishing-and-forestry/home.htm','https://www.bls.gov/oes/current/oes470000.htm','https://www.bls.gov/ooh/installation-maintenance-and-repair/home.htm','https://www.bls.gov/ooh/production/home.htm','https://www.bls.gov/ooh/transportation-and-material-moving/home.htm',' ']

comboL = []
# a list containing the corresponding percentage and link
ctr = 0
# counter for going through the list of links


reader = csv.DictReader(open('occupations.csv'))
for row in reader:
    comboL = [float(row['Percentage']), linkL[ctr]]
    ctr = ctr + 1
    k = row['Job Class']
    v = comboL
    occupations_dict[k] = v

# dict Reader looks like this:
# {'Job Class':'Management', 'Percentage':'6.1}
# {'Job Class':'Business and Financial operations', 'Percentage':'5'}
# ...

# for row 1, k takes the value of key 'Job Class", which is 'Magagemenet', and v takes the link composed of [percentage, link]
# thus, the first group added to the dictionary is: {k:v} --> {'Management': [6.1, 'http://www.careers-in-business.com/management/'}


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
        if (x - (occupations_dict.get(k)[0]) < 0):
            return k
        else:
            x = (x - (occupations_dict.get(k)[0]))

if __name__ == '__main__':
    app.debug = True
    app.run()

