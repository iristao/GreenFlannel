from flask import Flask, render_template

app = Flask(__name__)

@app.route('/occupations')

def occupations():
    return render_template("table.html")

if __name__ == '__main__':
    app.debug = True
    app.run()
