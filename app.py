#Flask & dependencies modules
from flask import Flask, jsonify, render_template, request, redirect, current_app
import pymongo
from flask_pymongo import PyMongo
import pandas as pd
import json


################
#Flask Setup
################

#Create an app for Flask setup
app = Flask(__name__)



################
#Database Setup
################
mongo = pymongo.MongoClient("mongodb+srv://jeopardy:jeopardy@jeopardy.n13te.mongodb.net/jeopardy?retryWrites=true&w=majority")

db = mongo['jeopardy']

################
#Flask Routes
################

#List all available api routes
@app.route("/")
def welcome():
    return render_template("index.html")


@app.route("/projectoverview")
def projectoverview():
    return render_template("whatis.html")

@app.route("/tableau")
def tableau():
    return render_template("tableau.html")

@app.route("/mlresearch")
def mlresearch():
    return current_app.send_static_file("mlresearch.html")

@app.route("/originaldata")
def originaldata():
    return render_template("originaldata.html")

@app.route("/editeddata")
def editeddata():
    return render_template("editeddata.html")

#Define main behavior
if __name__ == "__main__":
    app.run()