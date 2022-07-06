from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template("index.html")

@app.route('/thank-you', methods=['POST'])
def thank_you():
    name = request.form.get("exampleInputName")
    email = request.form.get("exampleInputEmail")
    print(name, email)
    return render_template("thank-you.html")
