
     ,-----.,--.                  ,--. ,---.   ,--.,------.  ,------.
    '  .--./|  | ,---. ,--.,--. ,-|  || o   \  |  ||  .-.  \ |  .---'
    |  |    |  || .-. ||  ||  |' .-. |`..'  |  |  ||  |  \  :|  `--, 
    '  '--'\|  |' '-' ''  ''  '\ `-' | .'  /   |  ||  '--'  /|  `---.
     `-----'`--' `---'  `----'  `---'  `--'    `--'`-------' `------'
    ----------------------------------------------------------------- 


Hi there! Welcome to Cloud9 IDE!

To get you started, create some files, play with the terminal,
or visit http://docs.c9.io for our documentation.
If you want, you can also go watch some training videos at
http://www.youtube.com/user/c9ide.

Happy coding!
The Cloud9 IDE team

{% for recipe in recipes %} {{recipe.category_name}} {{recipe.recipe_name}} {{recipe.Ingredients}} {{recipe.Prep_time}} {{recipe.cooking_time}} {{recipe.Instructions}} {{recipe.recipe_author}} {{recipe.calories}} {{recipe.vegan}} {{recipe.gluten_free}} {{recipe.allergens}} {% endfor %}

<div class="row">
              <div class="input-field col s12">
                  <i class="material-icons prefix">poll</i>
                <select class="category" name="category_name" required="" aria-required="true">
                  <option value="" disabled selected>Choose a Category</option>
                  {% for category in categories%}
                  <option value="{{category.category_name}}">{{category.category_name}}</option>
                  {% endfor %}
                </select>
                    <label>Categories</label>
              </div>
            </div>