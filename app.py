import pickle
from flask import Flask, render_template, jsonify, make_response
from flask_cors import CORS, cross_origin

# Load from file
pickle_model = None
pkl_filename = "housing.pkl"
with open(pkl_filename, 'rb') as file:
    pickle_model = pickle.load(file)

# Create an instance of Flask
app = Flask(__name__)
CORS(app, resources={
    r"/*": {
        "origins": "*"
    }
})
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['CORS_ORIGINS'] = '*'
app.config['DEBUG'] = True
app.config['JSON_SORT_KEYS'] = False
