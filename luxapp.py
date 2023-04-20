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
    """Function for the '/' route."""

    html = render_template('index.html')
    response = make_response(html)
    return response


@app.errorhandler(404)
def page_not_found(error_message):
    """Function for 404 error handler."""

    message = error_message.description
    return render_template("error.html", message=message), 404


@app.route('/obj/', methods=["GET"])
def missing_obj():
    """If object id not provided, abort with 404 and message."""

    abort(404, description="missing object id.")


@app.route("/search", methods=["GET"])
def search():
    """Function for the '/search' route."""

    # set each of the following four variables as user input or null
    label_search = request.args.get('l', "")
    classification_search = request.args.get('c', "")
    agent_search = request.args.get('a', "")
    department_search = request.args.get('d', "")

    if label_search or classification_search or agent_search or department_search:
        # query the database and select data that we need
        try:
            # show search results from LuxQuery
            results = LuxQuery(DB_NAME).search(agt=agent_search, dep=department_search,
                                               classifier=classification_search,
                                               label=label_search)
            results = json.loads(results)
            results_data = results["data"]
        except OperationalError:
            # if can not query database, then exits with 1
            print(f"Database {DB_NAME} unable to open")
            os._exit(1)
    else:
        results_data = []

    # parse multiple agents and multiple classifiers
    for obj in results_data:
        obj[3] = obj[3].replace(",", "<br/>")
        obj[4] = obj[4].replace(",", "<br/>")

    # html format for each row
    pattern = '''
    <tr>
        <div class='row'>
            <td><a href="obj/%d" target="_blank">%s</a></td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
        </div>
    </tr>
    '''

    # get label, date, agents, classifiers data html pattern
    pattern_res = ""
    for result in results_data:
        pattern_res += pattern % tuple(result)

    # html format for table
    html = f'''
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
    {pattern_res}
    </tbody>
    </table>
    '''

    response = make_response(html)
    return response


@app.route('/obj/<object_id>', methods=['GET'])
def search_obj(object_id):
    """Function for the '/obj/<object_id>' route."""

    try:
        search_response = LuxDetailsQuery(DB_NAME).search(object_id)
    except NoSearchResultsError:
        # if no search results, abort with 404 and message
        return abort(404, description=f"no object with id {object_id} exists.")
    except OperationalError:
        # if can not query database, then exits with 1
        print(f"Database {DB_NAME} unable to open")
        os._exit(1)

    # if no exception, then render_template with luxdetails
    search_response = json.loads(search_response)
    html = render_template(
        'luxdetails.html', time=asctime(localtime()), object_id=object_id,
        search_response=search_response)
    response = make_response(html)

    return response
