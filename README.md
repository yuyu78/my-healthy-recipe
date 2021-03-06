# Yuki Ishii

## My Healthy Recipe 

The goal of this project is to allow the user to access, store, share  and review healthy recipe. The user can search the recipe by typing the keyword in th search bar. 

[View the website here](https://flask-recipe-manager-project.herokuapp.com/) 
 
![screenshot web healthy](https://user-images.githubusercontent.com/76018052/132963463-7b200ec1-c1b9-4855-96d5-257ff0b32ded.PNG)

## Table of contents
1. [UX](#ux)   
a.[User Stories](#user-stories)  
b.[Strategy plane](#strategy-plane)  
b.[Design](#design)  
b.[Wireframe](#wireframe)  

2. [Features](#features)  

3. [Database](#database)  

4. [Wireframe](#wireframe)  

5. [Technologies used](#technologies-used)  

6. [Testing](#testing)

7. [Deployment](#deployment)

8. [Credits](#credits)

## UX <a name="ux"></a>

### User Stories <a name="user-stories"></a>

As a **first-time visitor**, I want:
* To have easy and clear information so I know quickly how to use the website
* To view the recipe so I can check the ingredients and preparation to cook
* To find a recipe by typing the keyword in the search bar so I can choose the recipe I want
* To search some recipes by choosing the category so I can search easily based on the category
* To create an account to access more functionality so I can create, add, edit and delete recipes

As a **returning visitor**, I want:
* To pin my favorite recipe from my recipe book or other users so when I come back to the website, I will find easily my favorites recipes
* To create my recipe by adding the title, the image, the ingredients, and the preparation so I can show my recipe through the website to other visitors
* To be able to update, modify the recipe so I can improve the recipe
* To delete my recipe so the recipe won´t appear on the website anymore 
* To review the recipe of other users so I can provide feedback 

### Strategy plane <a name="strategy-plane"></a>

The **targeted audiences** are: 
* People who like healthy food
* People of all age 
* People who enjoy cooking 

**Goal**:
* Have an easy understanding of the website 
* View recipe from other users
* Search recipe by typing keyword and/or choosing the category
* Add, view, update, and delete the recipe  

**Need**:
* Create an account to access more functionality
* Save the favorite recipe 
* Check the review of the recipe 
* Add review of the recipe 
* For admin users, manage categories 

### Design <a name="design"></a>
**Colour Scheme**  
The main color is light green and blue, which represents health, wellness, balance, harmony, peace. 

## Features <a name="features"></a>

**Existing Features** 

* Each page has a responsive fixed navigation bar with recipes (in the home page), login, and register
* Each page has a footer with the name of the website, copyright, and social media link
* Search a recipe by typing the keyword and/or choosing the category: starter, main, dessert, breakfast
* The user can click on the button “reset” to reset the research
* Register page to create an account with a username, password
* Login page with the input username and password
* When the user registered or login, it will direct to the home page with a different link in the navbar: Home, Add recipe, Log out 
* Add pagination to not overwhelm the website 
* To modify or delete recipes, the user has to click on one of their recipes and click on the option either “edit” or “delete”. 
* By clicking on “delete”, will appear a modal message “are you sure you want to delete this recipe?”
* By clicking on “edit”, it will appear the edit page with 2 buttons on the bottom: "edit" to confirm the modification or "cancel" 

**Features left to implement**

* Able to share recipes on social media
* Add admin user to manage category
* Delete the account
* Update username 
* Able to save the favorites recipes
* Able to reset the password of the user's account. 
* Able to upload Images from the computer. This feature will be covered in the upcoming Fullstack with Django lesson so for the moment, I am using the input with the type=URL.  
* Add pagination if the search result exceeds more than 6 recipes. For the moment, when the user searches a recipe, it will show the result without pagination. 
 
## Database <a name="database"></a>

The schema for the database below:   
![schema mongodb](https://user-images.githubusercontent.com/76018052/132092572-e1b18587-18ab-411d-a9c8-f2d9b4d108ec.PNG)

## Wireframe <a name="wireframe"></a>

[Home page](https://github.com/yuyu78/my-healthy-recipe/blob/main/wireframe/homepage.pdf)

[Show recipe page](https://github.com/yuyu78/my-healthy-recipe/blob/main/wireframe/show_recipe.pdf)

[Edit recipe page](https://github.com/yuyu78/my-healthy-recipe/blob/main/wireframe/edit_page.pdf)

[Add recipe page](https://github.com/yuyu78/my-healthy-recipe/blob/main/wireframe/add_recipe.pdf)

[Login page](https://github.com/yuyu78/my-healthy-recipe/blob/main/wireframe/login.pdf)

[Register page](https://github.com/yuyu78/my-healthy-recipe/blob/main/wireframe/register.pdf)

## Technologies used <a name="technologies-used"></a>

### Languages
* HTML5 
* CSS3
* Javscript
* Python

### Frameworks, Libraries & Programs Used
* [Git](https://git-scm.com/) for version control
* [Github](https://github.com/) to store repositories.
* [Gitpod](https://www.gitpod.io/), for the workspace. 
* [Balsamiq](https://balsamiq.com/wireframes/) to create a mockup.
* [Dbdiagram](https://dbdiagram.io/home) to create the database schema.
* [MongoDB](https://mongodb.com/) to store database
* [Heroku](https://heroku.com/) to deploy the site
* [Materialize css 1.0.0](https://materializecss.com/) to make the website responsive
* [Flask](https://flask.palletsprojects.com/) to create templates
* [Jquery](https://code.jquery.com/) to initialize materialize script
* [Imgur](https://imgur.com/) to host images

## Testing <a name="testing"></a>

The testing process can be found [here](https://github.com/yuyu78/my-healthy-recipe/blob/main/TESTING.md)

## Deployment <a name="deployment"></a>
* Sign up or log in to Heroku
* Click on "New" on the right and select "Create a new app"
* Enter your app name and select the region the closest to you
* Click on "Create app"
* From the dashboard, click on the "Deploy" tab
* Go to "Deployment method" and select "Github"
* Search your Github repository and click on "Connect"
* Go to the setting tab and click on "Reveal Config Vars"
* Enter the keys/values which also match with your env. py file 

| Key| Value | 
| --- | --- | 
| IP | 0.0.0.0 | 
| PORT | 5000 |
| SECRET_KEY | *Your secret key* |
| MONGO_URI | *Your Mongo URI* |
| MONGO_DBNAME | *Name of your database* |

* Go to the 'Deploy' tab and click 'Enable Automatic Deployment'.
* Choose the branch and click on "Deploy Branch"

### Forking the GitHub Repository

1. Go to the repository [my healthy recipe](https://github.com/yuyu78/my-healthy-recipe)
2. In the top right corner of the page, click on the "Fork" button
3. You will have a copy of the original repository in your Github account  

Forking allows making a change to the new repository without changing the original one.

### Cloning the GitHub Repository
1. Go to the repository [my healthy recipe](https://github.com/yuyu78/my-healthy-recipe)
2. Click the green button Code
3. Choose HTTPS, SSH, or GitHub CLI, then copy the URL
4. Open Git Bash
5. Change the directory to the location where you want the cloned directory
6. Type "git clone" and paste the URL you copied from step 3.
7. Press enter to create your local clone

## Credits <a name="credits"></a>

### Inspiration
A few parts of the python code on the function register, login, logout, add, edit, delete, search are inspired from the course of Code Institute: **Backend development mini-project putting all it together**

### Code

#### Materialize

* Navbar from [Materializecss](https://materializecss.com/navbar.html)
* Footer from [Materializecss](https://materializecss.com/footer.html)
* Cards recipes from [Materializecss](https://materializecss.com/cards.html#)
* Modal message from [Materializecss](https://materializecss.com/modals.html)
* Select input from [Materializecss](https://materializecss.com/select.html)

#### Bugs
* To avoid error message in the console, checked in [stackoverflow](https://stackoverflow.com/questions/46094912/added-non-passive-event-listener-to-a-scroll-blocking-touchstart-event/55388961#55388961)
* To use list-inline like bootstrap and align the social media links on the footer, I checked the solution in [stackoverflow](https://stackoverflow.com/questions/42884750/how-to-create-inline-lists-in-materializecss)
* To change the welcome message when the user is login, checked the solution to [stackoverflow](https://stackoverflow.com/questions/58089743/how-to-fix-login-and-logout-in-jinja-template-based-on-user-session)
* To adjust card's size in all the same height, checked in [Dogfalo's github](https://github.com/Dogfalo/materialize/issues/3814)
* To align the pagination horizontally, checked in [developer mozilla](https://developer.mozilla.org/en-US/docs/Web/CSS/Layout_cookbook/Pagination)

### Media

All the image are from [Unplash](https://unsplash.com/) and [Pexels](https://www.pexels.com/)

### Acknowledgment

* My mentor Miguel who provided advice and feedback during the project
* All the tutors of Code Institute
* Code Institute Slack community