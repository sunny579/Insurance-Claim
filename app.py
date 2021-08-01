#!/usr/bin/env python
# coding: utf-8

# In[3]:

from flask import Flask, render_template, request
import pickle

#Global variables
app = Flask(__name__)
loadedModel = pickle.load(open("insurance.pkl", "rb"))

#User-defined functions
@app.route("/", methods=["GET"])
def Home():
    return render_template("insurance.html")

@app.route("/prediction", methods=["POST"])
def prediction():
    age = int(request.form['age'])
    sex = request.form['sex']
    bmi = float(request.form['bmi'])
    children = int(request.form['children'])
    smoker = request.form['smoker']
    region = request.form['region']
    charges = float(request.form['charges'])

    if sex=="Male":
        sex = 1
    else:
        sex = 0
        
    if smoker == "Yes":
        smoker =1
    else:
        smoker =0

    if region =="North East":
        region = 0
    elif region =="North West":
        region =1
    elif region =="South East":
        region =2
    else:
        region =3

    prediction = loadedModel.predict[[age,sex,bmi,children,smoker,region,charges]][0]
    
    if prediction == 0:
        prediction ="Insurance is not claimed"
    else:
        prediction = "Insurance is claimed"

    return render_template("insurance.html",prediction_output = prediction)


#Main function
if __name__ == "__main__":
    app.run(debug=True)


# In[ ]:




