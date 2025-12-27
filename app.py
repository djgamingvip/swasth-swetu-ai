from flask import Flask, render_template, request
from data_loader import load_all_data
from helper_functions import get_disease_info, get_severity_for_symptoms
from prediction import predict_from_symptoms

app = Flask(__name__)

data = load_all_data()
sym_des = data["sym_des"]
precautions = data["precautions"]
workout = data["workout"]
description = data["description"]
medications = data["medications"]
diets = data["diets"]
severity = data["severity"]

@app.route("/")
def index():
    return render_template("index.html", logo="/static/logo.jpg")

@app.route("/predict", methods=["POST"])
def predict():
    symptoms = request.form.get("symptoms", "")
    user_symptoms = [s.strip() for s in symptoms.split(",") if s.strip()]

    if len(user_symptoms) == 0:
        return render_template("index.html", message="Please enter valid symptoms.")


    predicted_disease = predict_from_symptoms(user_symptoms)
    desc, pre, med, die, wrkout = get_disease_info(predicted_disease, description, precautions, medications, diets, workout)
    sev = get_severity_for_symptoms(user_symptoms, severity)

    return render_template(
        "index.html",
        logo="/static/logo.jpg",
        predicted_disease=predicted_disease,
        dis_des=desc,
        my_precautions=pre[0] if pre else [],
        medications=med,
        my_diet=die,
        workout=wrkout,
        severity=sev,
    )
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
