import os
from flask import Flask, render_template, redirect, request, session, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = "cookbook"
app.config["MONGO_URI"] = "mongodb://admin:7hayfield@ds135776.mlab.com:35776/cookbook"

mongo = PyMongo(app)

def get_recipe(recipe):
    recipe=mongo.db.recipes.find()
    return recipe
