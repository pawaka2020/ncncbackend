# routes/portal/second/page.py

from flask import Flask, Blueprint, render_template, send_file
from os.path import dirname, join
from blueprints import main_bp

def calculate(starting_number):
    return (starting_number * 2)

@main_bp.route('/second', methods=['GET'])
def page():
    
    return render_template('second/page.html')