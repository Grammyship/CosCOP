from flask import Flask, render_template, request
import json
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Loki')))
from CosCOP import CosCOP


app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/api/analyze', methods=['POST'])
def analyze():
    content = request.data.decode('utf-8')
    result = CosCOP(content)
    # result = dict({"utterances":[
    #                     { 
    #                         "utterance": "經實驗證實",
    #                         "status": 'StatusEnum.RULE_EXAGG'
    #                     },
    #                     { 
    #                         "utterance": "刺激毛囊",
    #                         "status": 'StatusEnum.RULE_EXAGG'
    #                     },
    #                     { 
    #                         "utterance": "告別禿頭",
    #                         "status": 'StatusEnum.RULE_MEDICAL'
    #                     }
    #                 ]})
    result = json.dumps(result)
    result = result.replace('\n', '').replace(' ', '')
    result = result.replace("StatusEnum.RULE_EXAGG", '2').replace("StatusEnum.RULE_MEDICAL", '1').replace("StatusEnum.RULE_OTHER", '3')
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)