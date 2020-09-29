from flask import Flask, render_template, redirect, request
import joblib

app = Flask(__name__)

model = joblib.load("model.pkl")

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/', methods = ["POST"])
def marks():
    if request.method == "POST":
        hours = float(request.form['hours'])

        marks = model.predict([[hours]])[0][0]
        if marks > 1000:
            marks = 1000
        return render_template("index.html", your_marks = marks)

if __name__ == "__main__":
    app.run(debug=True)