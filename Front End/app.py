from flask import Flask, render_template, jsonify, json, request, redirect
from joblib import dump, load
from pickle import dump as dump_p, load as load_p
import numpy as np
import pickle
import pandas as pd

# Create an instance of Flask
app = Flask(__name__)
model = None
house_cost = None
cost_data = None

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = 0
    a = {}
    house_cost = None
    cost_data = None

    if request.method == "POST":
        print(request.form)
        house_cost = None
        cost_data = None
        # read form data inputed by user
        ktch = request.form["ktch"] 
        car = request.form["car"]
        f1 = request.form["f1"]
        cond = request.form["cond"]
        fbath = request.form["fbath"]
        year = request.form["year"] 
        bed = request.form["bed"] 
        f2 = request.form["f2"]
        lot = request.form["lot"]
        hbath = request.form["hbath"]
        garea = request.form["garea"]
        print(ktch)

        # Place user inputs into a list and create df for label encoding
        inputs = [cond, fbath, bed, f1, year, hbath, f2, garea, lot, car, ktch]
        inputs_pd = pd.DataFrame([inputs])
        
        model = pickle.load(open('housing.pkl','rb'))
        ml_value = model.predict(inputs_pd)
        print(model.predict(inputs_pd))

        house_cost = ml_value
        print(house_cost)
        
        cost_data = (750000 - 34900) * house_cost + 34900
        cost_data = round(cost_data[0], 2)
        print(cost_data)
        # # Dict of user inputs to reload
        a = {
        "car": car,
        "year": year,
        "f1": f1,
        "f2": f2,
        "lot": lot,
        "fbath": fbath,
        "garea": garea,
        "bed": bed,
        "cond": cond,
        "kitchen": ktch,
        "hbath": hbath
        }
        
        print(a)
    return render_template("house.html", cost_data=cost_data)

if __name__=='__main__':
   app.run()
