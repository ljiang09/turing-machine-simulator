import time
from flask import Flask, jsonify
from turing_machine import TM_ANBN, TM_ANBNCN, TM_EQUAL, TM_AND, TM_PLUS1
from turing_machine import accept_tm

app = Flask(__name__)

@app.route('/time')
def get_current_time():
    return {'time': time.time()}


@app.route('/tmNames')
def get_tm_names():
    tm_data = {
        'tmNames': ["TM_ANBN", "TM_ANBNCN", "TM_EQUAL", "TM_AND", "TM_PLUS1"],
        'tmContents': {
            "TM_ANBN": TM_ANBN, 
            "TM_ANBNCN": TM_ANBNCN, 
            "TM_EQUAL": TM_EQUAL, 
            "TM_AND": TM_AND, 
            "TM_PLUS1": TM_PLUS1
        }
    }
    return jsonify(tm_data)


@app.route('/runMachine')
def run_machine():
    accept_tm(TM_PLUS1, "#0")
    return {'result': time.time()}

