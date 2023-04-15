"""Code for flask application."""

import json
import os

from time import localtime, asctime
from sqlite3 import OperationalError
from flask import Flask, request, make_response, render_template, abort
from query import LuxQuery, LuxDetailsQuery, NoSearchResultsError


DB_NAME = "./lux.sqlite"

app = Flask(__name__)


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():

    html = render_template('index.html')
    response = make_response(html)
    return response
