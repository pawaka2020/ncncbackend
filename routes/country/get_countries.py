# routes/country/get_countries.py

from flask import Blueprint, jsonify
from models.country import Country

get_countries_bp = Blueprint('get_countries_bp', __name__)

@get_countries_bp.route('/get_countries', methods=['GET'])
def get_countries():
    countries = Country.query.all()

    serialized_countries = [country.serialize() for country in countries]
    return jsonify(serialized_countries)