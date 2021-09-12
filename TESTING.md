# TESTING My healthy recipe

[README file](https://github.com/yuyu78/my-healthy-recipe/blob/main/README.md)   

## Table of contents
1. [Devices tested](#device-tested)   

2. [Browsers tested](#browsers-tested)   

3. [Testing User Stories](#testing-user-stories)  

4. [Manual Testing](#manual-testing)  

5. [Bugs](#bugs)  

6. [Validators](#validators)

7. [Lighthouse Testing](#lighthouse-testing)

## Devices tested <a name="device-tested"></a>

Devices tested during the project: 
* Desktop
* Moto G4 
* Galaxy S5
* Pixel 2
* Pixel 2Xl
* Iphone 5/SE 
* Iphone 6/7/8
* Iphone x
* Ipad 
* Ipad Pro
* Surface Duo
* Galaxy Fold

## Browsers tested <a name="browsers-tested"></a>
Browsers tested during the project:   
* Chrome
* Edge
* Firefox   

## Testing User Stories <a name="testing-user-stories"></a>

As a **first-time visitor**, I want:  
1. To have easy and clear information so I know quickly how to use the website  
    * When the visitors land on the home page, under the welcome message, it explains that to create the recipes, the visitors have to register
    * The search input and select category are straightforward, with the button reset and search
2. To view the recipe so I can check the ingredients and preparation to cook  
    * When the visitors click on one recipe from the homepage, it will direct to a page with the ingredients and preparation
    * The page of the recipe selected is clear, simple, and not overwhelming, with the picture, name, ingredients, and preparation
3. To find a recipe by typing the keyword in the search bar so I can choose the recipe I want  
    * The visitors can search by typing a keyword in search with or without category
    * The visitors can type the name of the recipe or an ingredient: for example if the visitors type "milk", it will appear all the recipes related to the milk
4. To search some recipes by choosing the category so I can search easily based on the category  
    * The visitors can select one or multiple categories 
    * the visitors can search recipes by selecting the category with or without typing anything in the search input
    
As a **returning visitor**, I want:  
1. To create my recipe by adding the title, the ingredients, and the preparation   
    * After logged in to their account, the visitors have an option on the navbar or in the link under the welcome message to add a recipe 
    * If the category is not selected, the fields are not filled in, or the URL doesn´t match, it will show a message that it requires
2. To be able to update, modify the recipe
    * After logged in to their account, the visitors have an option to edit their recipe 
    * The visitors have the option to cancel if they don´t want to edit 

3. To delete my recipe so the recipe won´t appear anymore on the website
    * After logged in to their account, the visitors have an option to delete their recipe 
    * By clicking on the delete button, it will appear a modal message asking if the visitors are sure to delete the recipe, this feature is to avoid that the visitors delete the recipe by mistake. 

## Manual Testing <a name="manual-testing"></a>

### Navigation bar 
1. Check if the link "My healthy recipe" will change the color when hover and check if after clicking on this link. it will direct to the homepage  
2. Check if all the links on the right side of the navbar will change the color after hovering 
3. Check if, on mobile size and Ipad, it will collapse to hamburger
4. User in session and not in session  
**User in session**:  
In the navbar on the right, it will appear the homepage, add recipe, and logout.    
In the welcome message, it will appear the username and the message above will be "You can search your favorites recipes below or add a new recipe by clicking here" with the link on "here" which will direct to the add page.    
When the user logged out, check that the message "You have been logged out
" will show.   
**User not in session**:  
It will appear in the navbar: homepage, login, register.  
The welcome message "Welcome to my Healthy Recipe! To create your favorites healthy recipes, register here" with a link in "here" which will direct to the register page

### Footer  
1. When hovering on the social media link, the color changes  
2. All the links direct to the correct social media page
3. The footer is responsive on all devices

### Homepage (homepage.html)  
1. Check if the homepage is responsive on all devices.  
2. Search and select category    

| Search Input | Select Category | Result |  
| --- | --- | --- | 
| Type keyword | Select one or multiple categories | If the keyword is for example "porridge" which is in MongoDB and select the category breakfast, the recipe porridge will appear. If the keyword is not available in MongoDB or doesn´t match with the category (for example, select category starter and there is no recipe called "porridge" in starter category), there will be a message "No Results found".|  
| Type keyword | Without selecting category | It will appear all the recipes related to the keyword without taking account of the category. For example, if I type "milk", it will show all the recipes with milk. |  
| No keyword | Select one or multiple categories | If the user just select one or multiple categories, it will show all the recipes related to the category (or categories) selected| 

3. Buttons Reset and Search   
**Search button**  
When the user clicks on the search button after typing a keyword in search input or selecting a category or both, it will appear either the result if available on Mongodb, or will render a message "No Results Found".  
**Reset button**       
After showing the result, by typing on the reset button, it will reset and display all the recipes available.  
If the user is on the next page and clicks on the reset button, it will direct to the first page.   

4. Recipe list  
When hovering over one recipe, it will show the box-shadow color in blue. 
By clicking on one recipe, it will direct to the page show_recipe, with the name, picture, ingredient, and preparation.    

5. Pagination
Check by clicking on the next page that the background color of the number of pages related is changing.   
![pagination color](https://user-images.githubusercontent.com/76018052/132110269-6b70e73c-f6d8-42a7-9b76-3b5246859060.PNG)

### Show recipe page (show_recipe.html)
1. When clicking on one recipe on the homepage, check if it directs to the page with all information about the recipe selected including the name, image, ingredients, and preparation. 
2. Check if the page is responsive on all devices  
3. If the user is logged in, check if it appears the button "edit" and "delete" so that the user can edit or delete their recipe.  
4. If the user checks the recipe of another user, check it just appears the button homepage.  
5. Check the button edit directs to the edit page  
6. Check if the button delete will display a modal message asking if the user is sure to delete  the recipe:  
-If the user clicks "yes", it will delete the recipe.   
-If the user clicks  "no", it will stay on the edit page.  
7. Check if the button homepage will direct to the homepage

### Add recipe page (add_recipe.html) 
1. All the inputs and buttons are responsive on all devices.  
2. If the category is not selected or the inputs are not filled in, a message will specify that the category or the inputs have to be selected or filled in.
3. If the user adds the recipe by clicking the button "add", it will direct to the homepage with a message on the top "Recipe Successfully Added".  
4. By clicking the reset button, the category and all the inputs will be reset.  
5. By clicking the cancel button, it will direct to the homepage  
6. In the ingredients and preparation inputs, advise the user to return to the line after each information so that it will display like a list  
7. After adding the recipe, check that the recipe added appears in the list of all recipes on the homepage, with the image, name, and username.  

### Edit recipe page (edit_recipe.html)  
1. Check if the edit page is responsive on all devices.
2. Check if one input is empty, by clicking on the edit button, it will display the message "Please fill in this field" so that all the input has to be filled in.   
3. Check if after clicking on the edit button (if all inputs, categories are filled), it will direct to the homepage with the message "Recipe Successfully Updated" on the top.  
4. Check if the user clicks on the cancel button, it will direct to the show recipe page with the same recipe selected.  
5. Check if the homepage button directs to the homepage.   

### Login page (login.html)    
1. Check if the page is responsive on all devices.  
2. Check if click on the button "Log in" with one or all input empty, it will display a message to require to fill in.  
3. Check if fill in the username and/or password inputs with less than min length or more than max length, it will display a message to match the format requested.  
4. Check if the username or password is incorrect, it will display the message that the username or/and the password are incorrect.  
5. If click on the button log in with the correct username and password, check if it will direct to the homepage with the welcome message following by the username.  
6. Bellow the button, if the user doesn´t have an account yet, check if the link "Register here" will direct to the register page.  

### Register page (register.html)    
1. Check if the page is responsive on all devices.  
2. Check if click on the button "Register" with one or all input empty, it will display a message to require to fill in.  
3. Check if fill in the username and/or password input with less than min length or more than max length, it will display a message to match the format requested.  
4. Check if the username or password is incorrect, it will display the message that the username or/and the password are incorrect.  
5. If click on the button register with the correct username and password, check if it will direct to the homepage with the welcome message following by the username.  
6. Bellow the button, if the user has already an account, check if the link "Log in here" will direct to the login page.  

## Bugs <a name="bugs"></a>
---
* When I use the URL method on the link "home" of the navbar, it shows an error message in the console 
![error message violation console](https://user-images.githubusercontent.com/76018052/128433103-67578485-901a-42e0-9ba1-e190fae5b67a.PNG)  
To avoid this error message in the console, checked the solution in [Stackoverflow](https://stackoverflow.com/questions/46094912/added-non-passive-event-listener-to-a-scroll-blocking-touchstart-event/55388961#55388961) and added in script.js file the code below:  

![solution to avoid error message violation](https://user-images.githubusercontent.com/76018052/128433343-7c927d89-087e-4a7d-9ae7-49e28f8d7829.PNG)

* To use list-inline like bootstrap and align the social media links on the footer, I checked the solution in [stackoverflow](https://stackoverflow.com/questions/42884750/how-to-create-inline-lists-in-materializecss) and copy-paste in the CSS the bootstrap style

* To change the welcome message when the user is login, check the solution to [stackoverflow](https://stackoverflow.com/questions/58089743/how-to-fix-login-and-logout-in-jinja-template-based-on-user-session)

* I added this code below in the function get_recipes() to display the username in the welcome message when the user is logged in:  
    *if session["user"]:  
    return render_template("homepage.html", username=session['user'])*

    but the problem is when I logout, it shows an error message on the page:  
    ![key error](https://user-images.githubusercontent.com/76018052/128783479-51bbeeca-4f51-45e4-bc59-e0cc56cc54ea.PNG)
    I contacted the tutor and advised me to use the get method like the code below:  
    *if not session.get("user") is None:*  
    In this code, we are checking if the get() method returned "None". If it is not "None", that means there is a user in the session.

* The image stored in MongoDB was not retrieved on the website. I found a solution on the Slack community by one student: host the image in the site [Imgur](https://imgur.com/) and store the URL on MongoDB. 

* Each time I add the recipe, it will add in the same page after the first recipe like in the screenshot below:  
![recipe bug](https://user-images.githubusercontent.com/76018052/129475114-f07d3835-b228-48e2-8e92-6c1b5150af4c.PNG)  
The problem was because of the for loop added in the page show_recipe, to fix the issue: 
1. Remove the for loop *for recipe in recipes* in the show_recipe.html
2. Add the object id to the link of the recipe list on the homepage so that the link passes the object id to the route  
![recipe id](https://user-images.githubusercontent.com/76018052/129477781-2c05d934-0b67-42c8-a8e1-ae39530beb7b.png)


* To show the ingredients and preparation as a list, I added in CSS the style: "*white-space: pre-wrap;*" so that every time the user will type enter after each ingredient or preparation steps, it will show as a list.  
In the page add_recipe, I added a note to return to the line by clicking enter in the ingredients and preparation input to aware the user. 

* Issue the the size of the card,: each card has different height as in thr screenshot below:  
![card not align](https://user-images.githubusercontent.com/76018052/129977981-a7e2e3ed-89f9-495e-a2d2-9b7f95e4139f.PNG)  
Found the solution in [Dogfalo's github](https://github.com/Dogfalo/materialize/issues/3814) : to fix the size issue, I have to set manually the height image using css style below:   
*.card .card-image img {  
    max-height:100%;  
    height: 300px;  
    object-fit: cover;  
}*  
The name of the user who created the recipe could be long so I put the recipe's name and user's name in a different row.

* To filter the recipes that contain only the categories selected when the user is searching on the homepage:  
The advice from the tutor is:  
-make a new list  
-iterate over the recipe we got from mongo  
-check if the recipes category is in the list of the category the user selected  
-if it is, add that recipe to the new list   
Here is the code to allow to do this feature:  
![for loop](https://user-images.githubusercontent.com/76018052/130477810-b42f8cc7-61a6-4376-bd7d-d76b84dec0d9.PNG)  

* The recipes didn´t render just by selecting the category. The tutor told me the reason is because of the variable *query = request.form.get("query")*, if the user doesn´t type anything in search input, then the variable query will be empty as I added *recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))*.  
The solution is to add another condition as in the screenshot below (the code on highlight):  
![if condition search](https://user-images.githubusercontent.com/76018052/131267101-01025f28-5595-4e38-a1c7-fb604eb088ac.PNG)  

* To align the pagination horizontally, I checked in [developer mozilla](https://developer.mozilla.org/en-US/docs/Web/CSS/Layout_cookbook/Pagination) and copy paste the code below:  
![copy paginatino](https://user-images.githubusercontent.com/76018052/131819758-687a0534-5d2d-4014-bbc7-b87f27b15fb7.PNG)

* On mobile size on edit page, there was spaces above and below the URL input  
![edit url](https://user-images.githubusercontent.com/76018052/132046991-21460488-a995-4314-8688-d5622a2d3ddb.PNG)
The issue comes from materialize, so to get rid of these spaces of the URL input, I added a style with smaller height in HTML in the URL input tag:  
 *<input id="image_url" name="image_url" type="url"value="{{ recipe.image_url }}" required style="height: 54px;"></input>*  

## Validators <a name="validators"></a>

### HTML and CSS validators  
Checked the validity of the code with [HTML Markup Validation Service](https://validator.w3.org/) and [CSS Validation Service](https://jigsaw.w3.org/css-validator/).  

#### HTML  
In all the HTML files, there are errors due to the Jinja code.

* base.html:

    There were 2 errors:   
    ![html validator](https://user-images.githubusercontent.com/76018052/132140475-27dbd582-0329-4450-a861-ab25e0dce6dd.PNG)  
    These errors are due because of this code inside the head tag:  
    *{% block styles %}  
    {% endblock %}*   
    After removing this code, no error.  

* 404.html and 500.html  
    Except for the jinja code issue, no error.  

* add_recipe.html  
![error add](https://user-images.githubusercontent.com/76018052/132140813-2ce1586a-8151-4c45-8b7a-65786a649b61.PNG)
To avoid there errors:  
    - Remove the closing input
    - Remove the value="Resete form" and the type="button" from the a tag    

* edit_recipe.html 
    - Remove one selected option       
    ![error edit page select](https://user-images.githubusercontent.com/76018052/132141996-0bf6bc40-cbc7-4c60-aa65-694867517cad.PNG) 

    - Remove the closing input  
    ![edit page error input](https://user-images.githubusercontent.com/76018052/132142024-96051b5f-3132-4e55-adf5-e92ec1147da3.PNG)  
    
    - Remove the type attribute in textarea
    ![edit error textarea no attribute](https://user-images.githubusercontent.com/76018052/132142059-fb6e0b9e-2f5c-4a17-b5a7-a14435e3d689.PNG)  
    
* homepage.html   
    - Remove the type attribute in option.
    ![homepage attribute not  alloed in option](https://user-images.githubusercontent.com/76018052/132142212-f9d999cb-5e6a-40b8-afc1-d86682d055db.PNG)
    - Because I am using jinja template to retrieve mongodb image in the img tag, not possible to add alt.  
    ![homepage error img alt](https://user-images.githubusercontent.com/76018052/132142268-1b0fd645-2252-4b0e-915e-b65915f5dfea.PNG)  

* login.html     
    Except for the jinja code issue, no error.  

* register.html     
    Except for the jinja code issue, no error.  

* show_recipe.html  
    Except for the jinja code issue, no error.

#### CSS
No error.  

### Javascript    
Checked the validity of javascript with [JSHint](https://jshint.com/).  
There are two undefined variables:  
* The variable $ due to the jQuery  
* The variable EvenTarget: to avoid the error message as explained in the bugs section  

One unused variable forsReset: is used for the onclick function on the reset button.  

### Python
Checked the validity of Python with [PEP8 online](http://pep8online.com/).   
![pep online](https://user-images.githubusercontent.com/76018052/132146188-001f5e83-25c0-4bd4-93a2-3d409f25be66.PNG)

## Lighthouse testing <a name="lighthouse-testing"></a>  

### Homepage desktop  
![lighthouse homepage](https://user-images.githubusercontent.com/76018052/132250560-d2f5b729-77ea-4fab-805d-941ce6704792.PNG)
  