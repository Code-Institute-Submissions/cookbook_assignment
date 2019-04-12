import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config["MONGO_DBNAME"] = "cookbook"
app.config["MONGO_URI"] = "mongodb://admin:7hayfield@ds135776.mlab.com:35776/cookbook"

mongo = PyMongo(app)

@app.route('/')
@app.route('/add_recipe')
def add_recipe():
    return render_template("add_recipe.html", categories=mongo.db.categories.find())

@app.route('/insert_recipe', methods=["POST"])
def insert_recipe():
    recipes=mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipe'))
    

@app.route('/get_recipe')
def get_recipe():
    return render_template("recipes.html", recipes=mongo.db.recipes.find())
    
@app.route('/edit_recipe')
def edit_recipe(recipe_id):
    the_recipe=mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_categories= mongo.db.cateogories.find()
    return render_template("edit_recipe.html", recipe=the_recipe, categories=all_categories)
    
    
    

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)