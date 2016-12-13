from flask import Flask, jsonify, request
from modeller.tile import TileTopicModeller
app = Flask(__name__)

@app.route('/topics', methods=['POST'])
def model_topics():
    #Params is a map containing the data in the spec. 
    #force=True means the caller does not have to specify the content type header.
    params = request.get_json(force=True)
    
    #This is the call to the topic modelling system.
    modeller = TileTopicModeller()
    topics = modeller.model_topics(params["terms"], params["tiles"])
    
    #Return the json output.
    return jsonify(topics)