from flask import Flask, render_template, jsonify, json, request, redirect
from joblib import dump, load
from pickle import dump as dump_p, load as load_p
import numpy as np
import pickle
import pandas as pd

# Load pipeline
# pipeline = load_p(open("../housing.pkl"))

# Create an instance of Flask
app = Flask(__name__)
model = None

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = 0
    a = {}

    if request.method == "POST":
        print(request.form)
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
        inputs = [car, year, f1, f2, lot, fbath, garea, bed, cond, ktch, hbath]
        inputs_pd = pd.DataFrame([inputs])
        # inputs_pd[1] = le_gender.transform(inputs_pd[1])
        # inputs_pd[3] = le_body.transform(inputs_pd[3])
        # inputs_pd[4] = le_make.transform(inputs_pd[4])
        # inputs_pd[5] = le_day.transform(inputs_pd[5])
        # inputs_pd[6] = le_gender.transform(inputs_pd[6])
        # inputs_pd[7] = le_body.transform(inputs_pd[7])
        # inputs_pd[8] = le_make.transform(inputs_pd[8])
        # inputs_pd[9] = le_day.transform(inputs_pd[9])
        # inputs_pd[10] = le_day.transform(inputs_pd[10])

        # # Run the pipeline (Scaler and rf_model) on user inputs
        # prediction_vector = pipeline.predict_proba(inputs_pd)
        # # Extract the probability to get 1(Serious or Fatal crash)
        # prediction = prediction_vector
        # print(prediction)
        
        model = pickle.load(open('housing.pkl','rb'))
        ml_value = model.predict(inputs_pd)
        print(model.predict(inputs_pd))
        # reverse = ((max_sales - min_sales)*(predictions))+ min_sales
        # print(reverse)
        house_cost = ml_value
        print(house_cost)

        house_cost = (750000 - 34900) * house_cost + 34900
        print(house_cost)
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
    return render_template("house.html")

if __name__=='__main__':
   app.run()
