import os
from flask import Flask, render_template, request
from pymongo import MongoClient
from dotenv import load_dotenv
import certifi

load_dotenv()

app = Flask(__name__)

if os.getenv('ENV') == 'prod':
    client = MongoClient(os.getenv('MONGODB_URI'), connect=False, tlsCAFile=certifi.where())
    # client = MongoClient(f"mongodb+srv://admin:{os.getenv('MONGODB_PASSWORD')}@journally.ywk9p1u.mongodb.net/?retryWrites=true&w=majority", connect=False, tlsAllowInvalidCertificates=True)
    db = client.landing_page
    prereg = db.prereg

@app.route('/')
def welcome():
    return render_template("index.html")

@app.route('/thank-you', methods=['POST'])
def thank_you():
    name = request.form.get("exampleInputName")
    email = request.form.get("exampleInputEmail")
    print(name, email)

    if os.getenv('ENV') == 'prod':
        prereg.insert_one({'name': name, 'email': email})

    return render_template("thank-you.html")
