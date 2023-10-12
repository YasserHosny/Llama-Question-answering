from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import json as jsn
#from llama2chat import get_llama_response


app = Flask(__name__)
CORS(app)

@app.route('/api/qa', methods=['Post'])
# @cross_origin()
def qa():
    json = request.get_json()
    model_name = json['model_name']
    user_input = json['user_input']
    print(user_input)
    response = jsonify({'bot_response': "Hello"})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
    # prompt = 'Give me innovative ideas for a chatbot using question-answer on tabular data. I need to visualize output answer and anymore enhance to results output'
    # get_llama_response(prompt)  

if __name__ == '__main__':
    app.run(debug=True)