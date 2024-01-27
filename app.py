from flask import Flask, render_template, request
from sklearn.linear_model import LinearRegression

import joblib

model = joblib.load("manamodel1.pkl")


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    rm = 0
    if request.method == "POST":
        rm = request.form["ip"]
        converted = float(rm)
        ans = model.predict([[converted]])
        return render_template("index.html", content=ans)
    else:
        return "nothing"


if __name__ == "__main__":
    app.run()
