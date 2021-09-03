# TESTING My healthy recipe

[README file](https://github.com/yuyu78/my-healthy-recipe/blob/main/README.md)  

* When I use the url method on the link "home" of the navbar, it shows an error message in the console 
![error message violation console](https://user-images.githubusercontent.com/76018052/128433103-67578485-901a-42e0-9ba1-e190fae5b67a.PNG)
To avoid this error message in the console, checked the solution in [Stackoverflow](https://stackoverflow.com/questions/46094912/added-non-passive-event-listener-to-a-scroll-blocking-touchstart-event/55388961#55388961) and added in script.js file the code below:  

![solution to avoid error message violation](https://user-images.githubusercontent.com/76018052/128433343-7c927d89-087e-4a7d-9ae7-49e28f8d7829.PNG)

* To use list-inline like bootstrap and align the social media links on the footer, I checked the solution in [stackoverflow](https://stackoverflow.com/questions/42884750/how-to-create-inline-lists-in-materializecss) and copy paste in the css the bootstrap style

* To change the welcome message when the user is login, checked the solution to [stackoverflow](https://stackoverflow.com/questions/58089743/how-to-fix-login-and-logout-in-jinja-template-based-on-user-session)

* I added this code below in the function get_recipes() to display the username in the welcome message when the user is logged in:  
    *if session["user"]:  
    return render_template("homepage.html", username=session['user'])*

    but the problem is when I logout, it shows an error message in the page:  
    ![key error](https://user-images.githubusercontent.com/76018052/128783479-51bbeeca-4f51-45e4-bc59-e0cc56cc54ea.PNG)
    I contacted the tutor and adviced me to use the the get method like the code below:  
    *if not session.get("user") is None:*  
    In this code, we are checking if the get() method returned None. If it is not None, that means there is a user in the session.

* The image stored Mongodb was not retrieved on the website. I found a solution on the Slack community by one student: host the image in the site [Imgur](https://imgur.com/) and store the URL on MongoDB.  

* Each time I add the recipe, it will add in the same page after the first recipe like in the screenshot below:  
![recipe bug](https://user-images.githubusercontent.com/76018052/129475114-f07d3835-b228-48e2-8e92-6c1b5150af4c.PNG)  
The problem was because of the for loop added in the page show_recipe, to fix the issue: 
1. Remove the for loop *for recipe in recipes* in the show_recipe.html
2. Add the object id to the link of the recipe list in the homepage so that the link pass the object id to the route  
![recipe id](https://user-images.githubusercontent.com/76018052/129477781-2c05d934-0b67-42c8-a8e1-ae39530beb7b.png)


* To show the ingredients and preparation as a list, I added in CSS the style: "*white-space: pre-wrap;*" so that everytime the user will type enter after each ingreedient or preparation steps, it will show as a list.  
In the page add_recipe, I added a note to return to the line by clicking enter in the ingredients and preparation input to aware the user. 

* Issue the the size of the card,: each card has different height as in thr screenshot below:  
![card not align](https://user-images.githubusercontent.com/76018052/129977981-a7e2e3ed-89f9-495e-a2d2-9b7f95e4139f.PNG)  
Found the solution in [Dogfalo's github](https://github.com/Dogfalo/materialize/issues/3814) : to fix the size issue, I have to set manually the height image using css style below:   
*.card .card-image img {  
    max-height:100%;  
    height: 300px;  
    object-fit: cover;  
}*  
The name of the user who created the recipe could be long so I put the recipe's name and user's name in different row.

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