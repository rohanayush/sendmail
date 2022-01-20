import smtplib


from flask import Flask, request
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify

# import pandas as pd
from werkzeug.utils import secure_filename

# import datacompy
from pytrends.request import TrendReq

app = Flask(__name__)
api = Api(app)
CORS(app)
conn = ""


@app.route("/")
def hello():
    # pytrends = TrendReq(hl='en-US', tz=360)

    # global conn a[]
    # conn= pytrends

    return "connected to google"


@app.route("/suggest", methods=["POST"])
def kuchh_bhi_nhin():
    a = request.get_data(as_text=True)
    print(a)
    print(type(a))
    aa=a.split('+')

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login("app.rohanayush@gmail.com", "MydreamiiitA5*")
    server.sendmail("soureshjha123@gmail.com", aa[1], aa[0])

    return jsonify(aa[0])


if __name__ == "__main__":
    app.run(port=5000)
