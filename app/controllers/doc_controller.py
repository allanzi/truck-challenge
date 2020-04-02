from flask_restful import Resource
from flask import jsonify, json
import os

class DocController(Resource):
    def get(self):
        root = os.path.realpath(os.path.dirname(__file__) + '/..')
        json_url = os.path.join(root, "static", "docs.json")
        response = json.load(open(json_url))


        return jsonify(response)