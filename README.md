
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


<!DOCTYPE html>
<html>
<head>
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/css/materialize.min.css">
    <link rel="stylesheet" href="{{url_for('static', filename='css/style.css')}}" type="text/css" />
</head>
<body class="indigo lighten-5"></body>
    <nav class="nav indigo lighten-3">
    <div class="nav-wrapper">
      <a href="{{url_for('homepage')}}" class="brand-logo" style="margin-left:10px">CookBook</a>
      <ul id="nav-mobile" class="right hide-on-med-and-down">
          {% if session['username'] %}
            <li><a href="{{url_for('homepage')}}">{{session['username']}}</a></li>
            <li><a href="{{url_for('add_recipe')}}">Add A Recipe!</a></li>
            <li><a href="{{url_for('get_recipe')}}">Recipes</a></li>
            <li><a href="{{url_for('logout')}}">Log Out</a></li>
          {% else %}
            <li><a href="{{url_for('user')}}">Log In</a></li>
            <li><a href="{{url_for('register')}}">Sign Up!</a></li>
          {% endif %}        
        
      </ul>
    </div>
  </nav>
    {% block content %}
    {% endblock %}
    
    
    
    
    
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/js/materialize.min.js"></script>
    
    <script>
    
    //For category dropdown functionality//
    
        $(document).ready(function() {
            $('.collapsible').collapsible();
            $('select').material_select();
        });
        
        
    //Plugin used for form validation to make sure all areas are filled in//    
        
        $(document).ready(function() {
        $('select').material_select();
    
        // for HTML5 "required" attribute
        $("select[required]").css({
          display: "inline",
          height: 0,
          padding: 0,
          width: 0
        });
      });
        

    </script>
    
</body>
</html>