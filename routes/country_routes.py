# routes/country_routes.py

from flask import Blueprint, jsonify
from models.country import Country

country_bp = Blueprint('country_bp', __name__)

@country_bp.route('/countries', methods=['GET'])
def get_countries():
    countries = Country.query.all()

    # country_list = [{'id': country.id, 'name': country.name} for country in countries]
    # return jsonify(country_list)

    #serialized_countries = [countries.serialize() for country in countries]
    serialized_countries = [country.serialize() for country in countries]
    return jsonify(serialized_countries)
    
