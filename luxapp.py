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


@app.route("/searchresults", methods=["GET"])
def searchresults():
    label_search = request.args.get('l', "")
    classification_search = request.args.get('c', "")
    agent_search = request.args.get('a', "")
    department_search = request.args.get('d', "")
    print(label_search, classification_search, agent_search, department_search)
    results = ""

    # show search results from LuxQuery
    results = LuxQuery(DB_NAME).search(agt=agent_search, dep=department_search,
                                       classifier=classification_search,
                                       label=label_search)
    results = json.loads(results)
    results_data = results["data"]

    # parse multiple agents and multiple classifiers
    for obj in results_data:
        obj[3] = obj[3].replace(",", "<br/>")
        obj[4] = obj[4].replace(",", "<br/>")

    # print(results_data)

    html = '''
    <table class="data-table">
        <thead>
            <tr>
                <th>Label</th>
                <th>Date</th>
                <th>Agents</th>
                <th>Classified As</th>
            </tr>
        </thead>
    <tbody>
    '''

    pattern = '''
    <tr>
        <div class='row'>
            <td hidden>%d</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
        </div>
    </tr>
    '''

    # insert label, date, agents, classifiers into html
    for result in results_data:
        print(result)
        html += pattern % tuple(result)

    html += '''
    </tbody>
    </table>
    '''

    response = make_response(html)
    return response