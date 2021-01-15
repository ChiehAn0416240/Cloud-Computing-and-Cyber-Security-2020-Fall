from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import compute  # python file that handles computation

app = Flask(__name__)

ENV = 'prod'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost/MRT'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://zxjigldkplbkwb:249535547bba6eb30413a40a046b78ca69bbd372139bae86d8db2f08fffd82d9@ec2-54-225-214-37.compute-1.amazonaws.com:5432/d9khv3p5jal5f6'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

time_morning = ['7:00', '8:00', '9:00']
time_noon = ['11:00', '12:00', '13:00']
time_evening = ['17:00', '18:00', '19:00']

class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    StationName = db.Column(db.String(200))
    TimePeriod = db.Column(db.String(200))

    def __init__(self, StationName, TimePeriod):
        self.StationName = StationName
        self.TimePeriod = TimePeriod


@app.route('/')
def index():
    print("Hello World")
    return render_template('index.html', station = '西門', results = [[] for i in range(7)], time = time_morning, show = 'No')


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        StationName = request.form['StationName']
        TimePeriod = request.form['TimePeriod']
        print(StationName, TimePeriod)

        if TimePeriod == 'Morning':
            time = time_morning
        elif TimePeriod == 'Noon':
            time = time_noon
        else:
            time = time_evening

        data = Feedback(StationName, TimePeriod)
        db.session.add(data)
        db.session.commit()
        
        results = compute.compute(StationName,TimePeriod)   # call the function in compute.py
        for r in results:
	        print(r)
        return render_template('index.html', station = StationName, results = results, time = time, show = 'Yes')


if __name__ == '__main__':
    app.run()