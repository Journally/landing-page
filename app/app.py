from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template("index.html")

@app.route('/thank-you')
def thank_you():
    return render_template("thank-you.html")
