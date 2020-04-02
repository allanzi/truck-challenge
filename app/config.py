from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)