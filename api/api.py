import time
from flask import Flask, jsonify, request
from turing_machine import TM_ANBN, TM_ANBNCN, TM_EQUAL, TM_AND, TM_PLUS1
from turing_machine import accept_tm
import sys
import io

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
    tm = request.args.get('tm')
    inputStr = request.args.get('inputStr')

    captured_output = io.StringIO()
    
    # Save the current stdout so we can restore it later
    old_stdout = sys.stdout
    
    # Redirect stdout to the captured_output StringIO object
    sys.stdout = captured_output

    result = ""

    try:
        # result = accept_tm(TM_PLUS1, "#0")
        if tm == "TM_ANBN":
            result = accept_tm(TM_ANBN, inputStr)
        elif tm == "TM_ANBNCN":
            result = accept_tm(TM_ANBNCN, inputStr)
        elif tm == "TM_EQUAL":
            result = accept_tm(TM_EQUAL, inputStr)
        elif tm == "TM_AND":
            result = accept_tm(TM_AND, inputStr)
        # elif tm == "TM_PLUS1":
        else:
            result = accept_tm(TM_PLUS1, inputStr)
    finally:
        sys.stdout = old_stdout

    printed_output = captured_output.getvalue()

    return jsonify({'result': result, 'steps': printed_output})

