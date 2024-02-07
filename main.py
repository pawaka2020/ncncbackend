from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:ylteicz@localhost/mydatabase'
db = SQLAlchemy(app)

class Country(db.Model):
    __tablename__ = 'countries'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

@app.route('/countries', methods=['GET'])
def get_countries():
    countries = Country.query.all()
    country_list = [{'id': country.id, 'name': country.name} for country in countries]
    return jsonify(country_list)

@app.route('/')
def hello_world():
    countries = Country.query.all()
    country_names = [country.name for country in countries]
    return 'Hello World! Countries: ' + ', '.join(country_names)

#Set the host to be the same as ipv4 address found on 'ipconfig' if launching on local machine.
#Else, use http address provided by online providers ie Heroku.
#if you get 'The requested address is not valid in its context' error when running 'python main.py',
#it means the ipv4 address of the modem has changed. Check it again on ipconfig and
#replace 
if __name__ == '__main__':

    app.run(host='192.168.1.19', debug=True)    