import os
from flask import Flask, render_template, redirect, request, session, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = "cookbook"
app.config["MONGO_URI"] = "mongodb://admin:7hayfield@ds135776.mlab.com:35776/cookbook"

mongo = PyMongo(app)

@app.route('/')

@app.route('/homepage')
def homepage():
    return render_template("homepage.html")
    
@app.route('/breakfast')    
def breakfast():
    return render_template('breakfast.html',
    recipes = mongo.db.recipes.find())

@app.route('/lunch')    
def lunch():
    return render_template('lunch.html',
    recipes = mongo.db.recipes.find())  
    
@app.route('/dinner')    
def dinner():
    return render_template('dinner.html',
    recipes = mongo.db.recipes.find())     
    
@app.route('/irish')    
def irish():
    return render_template('irish.html',
    recipes = mongo.db.recipes.find())    
    
@app.route('/french')    
def french():
    return render_template('french.html',
    recipes = mongo.db.recipes.find())     
    
@app.route('/italian')    
def italian():
    return render_template('italian.html',
    recipes = mongo.db.recipes.find())        
    

@app.route('/user')
def user():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html',
    users=mongo.db.users.find())

@app.route('/user_info', methods=['POST'])
def user_info():
    users = mongo.db.users
    users.insert_one(request.form.to_dict())
    return redirect(url_for('user'))
    
@app.route('/login', methods=["GET","POST"])
def login():
    users = mongo.db.users
    client = users.find_one({'username' : request.form['username']})

    if client:
        session['username'] = request.form['username']
        return redirect(url_for('homepage'))
    else:    
        return "not a valid username"

@app.route('/logout', methods=['GET','POST'])
def logout():
    session.pop('username')
    return redirect(url_for('homepage'))

@app.route('/add_recipe')
def add_recipe():
    return render_template("add_recipe.html", 
    categories=mongo.db.categories.find(), cuisines=mongo.db.origin_of_cuisine.find(), difficulty=mongo.db.difficulty.find())

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
    all_cuisine = mongo.db.origin_of_cuisine.find()
    return render_template('edit_recipe.html', recipe=the_recipe, categories=all_categories, cuisines=all_cuisine)
    
@app.route('/update_recipe/<recipe_id>', methods=['POST'])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.update( {"_id": ObjectId(recipe_id)},
    {
        'category_name':request.form.get('category_name'),
        'cuisine_name':request.form.get('cuisine_name'),
        'recipe_name':request.form.get('recipe_name'),
        'recipe_author':request.form.get('recipe_author'),
        'description':request.form.get('description'),
        'ingredient1':request.form.get('ingredient1'),
        'ingredient2':request.form.get('ingredient2'),
        'ingredient3':request.form.get('ingredient3'),
        'ingredient4':request.form.get('ingredient4'),
        'instruction1':request.form.get('instruction1'),
        'instruction2':request.form.get('instruction2'),
        'instruction3':request.form.get('instruction3'),
        'instruction4':request.form.get('instruction4'),
        'prep_time':request.form.get('prep_time'),
        'cooking_time':request.form.get('cooking_time'),
        'calories':request.form.get('calories'),
        'allergens':request.form.get('allergens'),
    })
    return redirect(url_for('get_recipe'))
    
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    return redirect(url_for('get_recipe'))

@app.route('/view_recipe/<recipe_id>')
def view_recipe(recipe_id):
    the_recipe =  mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_categories = mongo.db.categories.find()
    return render_template('view_recipe.html', recipe=the_recipe, categories=all_categories)   
    
@app.route('/new_cuisine')
def new_cuisine():
    return render_template('add_cuisine.html')    
    
@app.route('/add_cuisine', methods=['POST'])    
def add_cuisine():
    cuisines = mongo.db.origin_of_cuisine
    cuisine_doc = {'cuisine_name': request.form['cuisine_name']}
    cuisines.insert_one(cuisine_doc)
    return redirect(url_for('homepage'))
    
    
if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)