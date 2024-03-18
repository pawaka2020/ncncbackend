# routes/country/get_countries.py

# from flask import Blueprint, jsonify
# from models.country import Country

# get_countries_bp = Blueprint('get_countries_bp', __name__)

# @get_countries_bp.route('/get_countries', methods=['GET'])
# def get_countries():
#     countries = Country.query.all()

#     serialized_countries = [country.serialize() for country in countries]
#     return jsonify(serialized_countries)

# routes/country/get_countries.py

from flask import Flask, Blueprint, jsonify
from models.mongodb.db import db
from models.mongodb.countries import Country
from blueprints import country_bp

# Displays all objects of Country in JSON format on the browser
@country_bp.route('/get_countries', methods=['GET'])
def get_countries():
    country_list = list(db['countries'].find({})) 

    result = [{
        'name' : country['name'],
        'population' : country['population']
        } for country in country_list]
        
    return jsonify(result)