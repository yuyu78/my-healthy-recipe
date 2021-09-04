import os, math
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# -------------------------------------- Homepage with all recipes
@app.route("/")
@app.route("/get_recipes/<int:page>")
def get_recipes(page = 1):
    # Pagination
    to_recipe_no = page * 6
    from_recipe_no = to_recipe_no - 6
    recipes = list(mongo.db.recipes.find())
    show_recipes = recipes[from_recipe_no:to_recipe_no]
    number_of_pages = math.ceil(len(recipes) / 6)

    categories = list(mongo.db.categories.find())
    # If user is logged in or registered
    if not session.get("user") is None:
        return render_template("homepage.html", 
                                username=session['user'], 
                                recipes=show_recipes, 
                                categories=categories, 
                                number_of_pages=number_of_pages, 
                                page=page)
    return render_template("homepage.html", 
                            recipes=show_recipes, 
                            categories=categories, 
                            number_of_pages=number_of_pages, 
                            page=page)


# -------------------------------------- Search in homepage
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    categories = request.form.getlist('categories')
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    list_to_return = []
    for recipe in recipes:
        # If search by typing search input and selecting category
        if recipe["category_name"] in categories:
            list_to_return.append(recipe)
        # If search without selecting category 
        elif len(categories) < 1:
            list_to_return.append(recipe)
    # If search without input search
    if len(recipes) < 1:
        recipes = list(mongo.db.recipes.find())
        for recipe in recipes:
            if recipe["category_name"] in categories:
                list_to_return.append(recipe)       
    categories = list(mongo.db.categories.find())
    return render_template("homepage.html", 
                            recipes=list_to_return, 
                            categories=categories, 
                            search=True)


# -------------------------------------- Registration
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exist in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        print(f"REGISTER: {register}")
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        return redirect(url_for("get_recipes"))
    return render_template("register.html")


# -------------------------------------- Login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
    
        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    return redirect(url_for("get_recipes"))
            else:
                #invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))
            
        else:
            #username doesn´t exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


# -------------------------------------- Logout
@app.route("/logout")
def logout():
    #remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("get_recipes"))


# -------------------------------------- show_recipe.html(after clicking one recipe in the homepage)
@app.route("/show_recipe/<recipe_id>")
def show_recipe(recipe_id):
    #show the recipe page with image, name, ingredients and preparation
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("show_recipe.html", recipe=recipe)


# -------------------------------------- Add_recipe.html
@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        my_recipe = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "image_url": request.form.get("image_url"),
            "ingredients": request.form.get("ingredients"),
            "preparation": request.form.get("preparation"), 
            "created_by": session["user"] 
        }
        mongo.db.recipes.insert_one(my_recipe)
        flash("Recipe Successfully Added")
        return redirect(url_for("get_recipes"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_recipe.html", categories=categories)


# -------------------------------------- edit_recipe.html
@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        my_recipe = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "image_url": request.form.get("image_url"),
            "ingredients": request.form.get("ingredients"),
            "preparation": request.form.get("preparation"), 
            "created_by": session["user"] 
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, my_recipe)
        flash("Recipe Successfully Updated")
        return redirect(url_for("get_recipes"))
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})  
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_recipe.html", recipe=recipe, categories=categories)


# Delete function
@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted")
    return redirect(url_for("get_recipes"))


# -------------------------------------- error page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(e):
    return render_template('500.html'), 500

    
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
