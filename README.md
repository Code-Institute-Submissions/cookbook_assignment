HotPot’s Cook Book
===

**Milestone Project Three: Data Centric Development - Code Institute.**

HotPot’s is an online cookbook dedicated to allowing users to display and share their recipes with people from all over the world. The site is category-focused and highlights recipes based on attributes such as cuisine, cooking ability and meal type. The user can structure, create and edit their recipes to their preference and store recipes on the site for other users to view. HotPot’s is an opportunity for users to see the joy of cooking and to understand that making something great can be very simple. After all, anyone can cook!

Through a series of colorful and easy-to-navigate webpages, the user can assess and decide which recipe they want to make. Most importantly, HotPot’s is user inclusive. Whether the user wishes to interact and add a recipe, or simply browse and view what’s available from other members, there’s something for anyone looking to make their meal great!


Features
---

In this section, I will briefly describe each user available feature which this project has to offer.

**Existing Features**

* **Navigation bar** – Allows users to navigate between web pages on the site using marked buttons.
* **Home Page Cards** – Another way for users to navigate the site, but each card includes an image and each link is specific to a different variety of recipes they can view. The varieties include Recipes by Meal Type, Recipes by Cuisine and Recipes by Ability.
* **Sign Up!** – A page which prompts the user for their email address, username and password to register them for the site.
* **Log in** – A page which prompts the user for their username. Log in are both required for users to avail of certain features on the site.
* **Username icon** – A neat little icon of the user’s username which will appear on the right hand side of the navbar to welcome the user when they successfully log in. It is will also bring the user back to the home page when clicked.
* **Recipe Menu** – A list of every recipe available to view on the site. The list is organised alphabetically by Recipe Name and Author’s Surname.
* **Recipe Cards** – These cards appear on all Recipe Menus. They are coloured blue and they give a brief synopsis of the recipe that include Title, Author, Description, Meal Category, Cuisine and Difficulty. Depending on whether or not a user is logged in, the choices for each card can differ from simply viewing the recipe or, if logged in, the ability to edit and delete that recipe.
* **View Recipe** – One of the Recipe Card options which allows the user to view a webpage with the full details of the Recipe Card they clicked including Ingredients and Instructions.
* **Add A Recipe!** – A navigation button which will bring a logged in user to a form for adding a recipe to the site. The form Requires each field to be filled out and is validated at certain marks to make sure the recipe satisfies all requirements necessary to be added to the site.
* **Edit a Recipe** – A feature of the Recipe Card. Edit a Recipe is similar to the Add a Recipe! feature, except this form allows the user to improve an existing recipe on the site. Every detail of the recipe will appear in the prompt and the user can make adjustments where necessary.
* **Delete Recipe** – A feature of the Recipe Card. Delete a recipe allows a user to permanently delete a recipe from the database.

**Features Left to Implement**
* I hope to implement a feature which will allow users to upload their own images to display alongside their recipes. I believe it will make the user experience more personal and rewarding to share images of what they have cooked alongside recipes.
* I also hope to give the users the opportunity to upvote recipes and have those votes stored on the MongoDB. As of writing this, I haven’t found the solution to properly coding this function, but I hope to make it part of the site soon.
* I would also like to implement a more secure authentication system which uses password and this feature will also be rectified in the future.




Technologies Used
---

The following list contains all technologies used in the creation of this project.

* **Cloud9**
  * Platform used to write the necessary code for this project. Link for the official site provided [here]( https://c9.io/login).

* **Python**
  * The programming language used on this project. Link for the official site provided [here](https://www.python.org/).

* **Flask**
  * MicroFramework used along with Python. Allows all applications to be routed to the browser. Link for the official site provided [here](http://flask.pocoo.org/).

* **MongoDB**
  * Used for data storage. Link for the official site provided [here]( https://mlab.com/).

* **PyMongo**
  * Used to allow Python to communicate with MongoDB in retrieving necessary data. Link provided [here]( https://api.mongodb.com/python/current/).

* **BSON**
  * BSON was used to read ObjectIds from MongoDB as JSON.

* **Ginja**
  * Used to incorporate Python code in an HTML file setting.

* **JQuery**
  * The project uses JQuery to initialize the Materialize elements used. It was also used for the form validation. Link for the official site provided [here](https://jquery.com/).

* **HTML**
  * The project uses HTML as the mark-up language.

* **CSS**
  * The project uses CSS to style the HTML elements.

* **Bootstrap**
  * A Bootstrap CDN was initially used to add further style to the project. However, I later decided to solely use the Materialize library. Link for the official site provided [here](https://getbootstrap.com/).

* **Font Awesome**
  * Used to add visual icons for the form sections of the project. Link for the offical site provided [here](https://fontawesome.com/).

* **Google Fonts**
  * Used to add a specific font to certain sections of HTML text. Link for the offical site provided [here](https://fonts.google.com/).

* **Materialize**
  * Used for the over look and style of the page. Provided a majority of the elements used such as cards, navbar and footer.Link for the offical site provided [here](https://materializecss.com/).



Credits
---

**Content**

Excluding the recipes and all recipe attributes used on the site, all other content was written by me.

The following is a list of links for all recipes used (or, in some cases, partly used) for this project:

(Please note that in some cases, recipe authors did not appear on some of the selected official recipe pages used. In lieu of these missing names, I used pseudonyms. However, full credit is given below for every recipe used and its source.)

* **Basic Frittata** - Source: IncredibleEgg.org. Link provided [here]( https://www.incredibleegg.org/recipe/simple-frittata/).
* **Fantastic Fish Pie** – Source: JamieOliver.com. Link provided [here]( https://www.jamieoliver.com/recipes/fish-recipes/fantastic-fish-pie/). 
* **Hash Browns** – Source: BonAppétite.com. Link provided [here]( https://www.bonappetit.com/recipe/bas-best-hash-browns).
* **Irish Stew** – Source: BordBia.ie. Link provided [here]( https://www.bordbia.ie/consumer/recipes/lamb/pages/irishstew.aspx).
* **Martin Freeman’s Eggs Royale** – Source: JamieOliver.com. Link provided [here]( https://www.jamieoliver.com/recipes/egg-recipes/martin-freeman-s-eggs-royale/).
* **Skillet Garlic Butter Herb Steak & Potatoes** – Source: TheRecipeCritic.com. Link provided [here]( https://therecipecritic.com/skillet-garlic-butter-herb-steak-and-potatoes/).
* **Original Italian Pizza** – Source: KitchenStories.com. Link provided [here]( https://www.kitchenstories.com/en/recipes/original-italian-pizza).
* **Ratatouille** – Source: JamieOliver.com. Link provided [here]( https://www.jamieoliver.com/recipes/vegetables-recipes/classic-ratatouille/).
* **Scrambled Eggs with Bacon** – Source: BrooklynFarmGirl.com. Link provided [here]( https://brooklynfarmgirl.com/scrambled-eggs-with-bacon/).
* **Scrumptious Cheese and Veggies on Toast** – Source: AllRecipes.co.uk. Link provided [here]( http://allrecipes.co.uk/recipe/75/scrumptious-cheese-and-veggies-on-toast.aspx).
* **Spaghetti Bolognese** – Source: Lidl-Recipes.ie. Link provided [here]( https://www.lidl-recipes.ie/Recipes/Scrummy-Spaghetti-Bolognese).
* **Traditional Pancakes** – Source: Odlums.ie. Link provided [here]( https://www.odlums.ie/recipes/traditional-pancakes/).
* **Vegetable Soup** – Source: SafeFood.eu. Link provided [here]( https://www.safefood.eu/Recipes/Lunch/Homemade-vegetable-soup.aspx)

**Media**

The following is a list of links for all images used on this project:

* **Breakfast Image** - Source: TheWorkTop.com. Link provided [here]( https://www.theworktop.com/breakfast-brunch-recipes/healthy-breakfast-bowl-beans-sweet-potato/).
* **Lunch Image** – Source: LazyCatKitchen.com. Link provided [here]( https://www.lazycatkitchen.com/mexican-lunch-bowl-spicy-crumb/).
* **Dinner Image** – Source: DinnerAtTheZoo.com. Link provided [here]( https://www.dinneratthezoo.com/firecracker-chicken/).
* **Irish Cuisine Image** – Source: DonalSkehan.com. Link provided [here]( http://www.donalskehan.com/journal/my-top-traditional-irish-recipes/).
* **French Cuisine Image** – Source: Pinterest.com. Link provided [here]( https://www.pinterest.ie/pin/455145106086315521/).
* **Italian Cuisine Image** – Source: PlaysWellWithButter.com. Link provided [here]( https://playswellwithbutter.com/2016/09/19/pasta-bolognese-with-bucatini/).
* **Easy Recipes Image** – Source: MomOnTimeOut. Link provided [here]( https://www.momontimeout.com/easy-chicken-stir-fry-recipe/)
* **Intermediate Recipes Image** – Source: TheMediterraneanDish.com. Link provided [here]( https://www.themediterraneandish.com/easy-ratatouille-recipe/)
* **Expert recipes Image** – Source: ChefDeHome. Link provided [here]( https://www.chefdehome.com/recipes/561/ratatouille)

**Acknowledgements**

* Michael Parks (tutor) - Credit for showing me how to properly display images using Python and explaining how to use Ginja effectively in the project.
* Niel McEwan(tutor) – For guidance support and help during the parts of this projects I found tricky to get through.
* Pretty Printed (Youtube Channel) - Credit for instructional video for building login functionality which I followed for my own implementation. Link for this video [here](https://www.youtube.com/watch?v=vVx1737auSE).
* Full credit for form validation jQuery used in this project goes to code I found on CodePen from a user named Ian. Link to the code [here]( https://codepen.io/zzzian/pen/LZbrOP).
* A very useful tutorial on how to deploy the project using GitHub Pages.Click here for the video.
* A special thanks to the lecturers and coordinators at Code Institute for their tutorials and instruction through the User-Centric Frontend Development module. Their website can be found here
* Lastly, to my parents, Seamus and Susan, for their constant support and help throughout the prep and creation of this Milestone project.





