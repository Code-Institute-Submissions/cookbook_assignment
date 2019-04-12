import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

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
    
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id":ObjectId(recipe_id)})
    all_categories = mongo.db.categories.find()
    return render_template('edit_recipe.html', recipe=the_recipe, categories=all_categories)
    
@app.route('/update_recipe/<recipe_id>', methods=['POST'])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.update( {"_id": ObjectId(recipe_id)},
    {
        'category_name':request.form.get('category_name'),
        'recipe_name':request.form.get('recipe_name'),
        'recipe_author':request.form.get('recipe_author'),
        'date':request.form.get('date'),
        'gluten_free':request.form.get('gluten_free'),
    })
    return redirect(url_for('get_recipe'))
    
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    return redirect(url_for('get_recipe'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)