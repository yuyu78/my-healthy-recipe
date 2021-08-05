# Yuki Ishii

## My Healthy Recipe 

The goal of this project is to allow the user to access, store, share  and review healthy recipe. The user can search the recipe by typing the keyword in th search bar. 

## Table of contents
1. [UX](#ux)   
a.[User Stories](#user-stories)  
b.[Strategy plane](#strategy-plane)  
b.[Design](#design)  
b.[Wireframe](#wireframe)  

2. [Features](#features)  

3. [Database](#database)  

4. [Technologies used](#technologies-used)  

5. [Testing](#testing)

6. [Deployment](#deployment)

7. [Credits](#credits)
---
## UX <a name="ux"></a>

### User Stories <a name="user-stories"></a>

As a **first-time visitor**, I want:
* To have easy and clear information about the website
* To view the recipe
* For Vegan people, to be able to view Vegan recipe 
* To find the recipe I want by typing the keyword in the search bar 
* To search some recipe by choosing the category
* To create an account to access more functionality like creating, updating, deleting and saving recipe

As a **returning visitor**, I want:
* To pin my favorite recipe from my own recipe book or from other user
* To create my own recipe by adding the title, the ingredients and the preparation
* To be able to update, modify the recipe
* To delete my own recipe 
* To review the recipe of other users 

### Strategy plane <a name="strategy-plane"></a>
The **targeted audiences** are: 
* People who like healthy food
* People for all age 
* People who enjoy cooking 

**Goal**:
* Have easy undestanding of the website 
* View recipe from other user
* Search recipe by typing keyword and/or choosing category
* Add, view, update and delete recipe  

**Need**:
* Create an account to access more functionality
* Save the favorite recipe 
* Check the review of the recipe 
* Add review of the recipe 
* For admin user, manage categories 

### Design <a name="design"></a>
**Colour Scheme**  
The main color is light green and blue, which represents health, wellness, balance, harmony, peace. 

## Features <a name="features"></a>

**Existing Features** 

* Each page has a responsive fixed navigation bar with recipes(which is the home page), favorites, login and register.
* Each page has a footer with the name of the website, copyright and social media link
* Search a recipe by typing the keyword and/or choosing the category: starter, main, desert, snack, drink
* The user can click on the button “reset” to reset the the research
* Register page to create an account with an username, password, and confirm password
* Login page with the input username and password
* When the user registered or login, it will direct to the home page with different navbar: Home, profile,New recipe, Favorites, Log out 
* Add pagination to not overwhelm the website 
* Able to save a recipe by clicking on the heart icon, this feature is available for user who logs in to the website
* If the user is not registered and click on the heart icon, it will direct to the register page 
* The user can check their own recipe by clicking on the profile in the navbar
* To modify or delete recipes, the user has to click on one recipe in the profile and click on the option either “edit” or “delete”. The button “profile” is available to able the user to come back to the profile page
* By clicking on “delete”, it will appear a modal message “are you sure you want to delete this recipe?”
* By clicking on “edit”

**Features implemented left**

* Able to share recipe in social media
* Delete the account
* Update username 
* Filter recipe for Vegan people, allergen
* Able to reset password if the user forgot 
 
## Database <a name="database"></a>

The schema for the database below: 
![Database Schema](https://user-images.githubusercontent.com/76018052/128268702-08d6f61b-38bf-4a5e-8f48-50a35c41fc18.PNG)



## Technologies used <a name="technologies-used"></a>
---
* [Git](https://git-scm.com/) for version control
* [Github](https://github.com/) to store repositories.
* [Gitpod](https://www.gitpod.io/), for the workspace. 
* [Balsamiq](https://balsamiq.com/wireframes/) to create a mockup.
* [Dbdiagram](https://dbdiagram.io/home) to create the database schema.
* [MongoDB](https://mongodb.com/)
* [Heroku](https://heroku.com/)
* [Materialize css 1.0.0](https://materializecss.com/)
* [Flask](https://flask.palletsprojects.com/)
* [Jquery](https://code.jquery.com/)

## Testing <a name="testing"></a>
When I use the url method on the link "home" of the navbar, it shows an error message in the console 
![error message violation console](https://user-images.githubusercontent.com/76018052/128433103-67578485-901a-42e0-9ba1-e190fae5b67a.PNG)
To avoid this error message in the console, checked the solution in [Stackoverflow](https://stackoverflow.com/questions/46094912/added-non-passive-event-listener-to-a-scroll-blocking-touchstart-event/55388961#55388961) and added in script.js file the code below:  

![solution to avoid error message violation](https://user-images.githubusercontent.com/76018052/128433343-7c927d89-087e-4a7d-9ae7-49e28f8d7829.PNG)

## Deployment <a name="deployment"></a>

## Credits <a name="credits"></a>