import time
from flask import Flask, jsonify
from turing_machine import GR_ANBN, GR_ANBM, GR_A, GR_B, GR_C, GR_D

app = Flask(__name__)

@app.route('/time')
def get_current_time():
    return {'time': time.time()}


@app.route('/grammarNames')
def get_grammar_names():
    grammar_data = {
        'grammarNames': ["GR_ANBN","GR_ANBM","GR_A","GR_B","GR_C","GR_D"],
        # 'grammarContents': ', '.join([GR_ANBN, GR_ANBM, GR_A, GR_B, GR_C, GR_D])
        'grammarContents': {
            "GR_ANBN": GR_ANBN, 
            "GR_ANBM": GR_ANBM, 
            "GR_A": GR_A, 
            "GR_B": GR_B, 
            "GR_C": GR_C, 
            "GR_D": GR_D
        }
    }
    return jsonify(grammar_data)



