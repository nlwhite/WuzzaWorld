from datetime import datetime

from application import app
from flask import render_template, request
from geoalchemy2 import functions
from .models import *
import ast

@app.route('/', methods=['GET'])
def home():

    streets = session.query(functions.ST_AsGeoJSON(Street)).all()

    street_json = []

    for s in streets:
        try:
            street_json.append({'type': 'MultiLineString', 'coordinates': ast.literal_eval(s[0])['geometry']['coordinates']})
        except:
            pass

    return render_template('index.html', date=datetime.now(), streets=street_json)

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/contact/')
def contact():
    return render_template('contact.html')

@app.route('/hello/')
@app.route('/hello/<name>')
def hello_there(name = None):
    return render_template(
        'index.html',
        name=name,
        date=datetime.now()
    )
