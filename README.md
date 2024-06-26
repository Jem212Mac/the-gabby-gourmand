# The Gabby Gourmand

![The Gabby Gourmand](documentation/am_i_responsive.png)

Live Version: [The Gabby Gourmand](https://gabby-gourmand-a59f21db8e77.herokuapp.com/)


Repository: [GitHub Repo](https://github.com/Jem212Mac/the-gabby-gourmand)

Developed by [Jemima MacKenzie](https://github.com/Jem212Mac).

## About
This is a website intended to provide interested parties with a review of various restaurants.  The intended user of the site is someone who is interested in food (a foodie) who loves to dine out but also likes to cook and try new recipes.  The home page for the site provides the user with a list of restaurant reviews that they can look through to help them decide on where to dine out next, but the site also includes a page listing food recipes and a page listing cocktail recipes where users can leave comments.  See selected screenshots (on different viewport sizes) below:

![](documentation/screen_1.png)
![](documentation/screen_2.png)
![](documentation/screen_3.png)
![](documentation/screen_4.png)
![](documentation/screen_5.png)

## UX Design
The target audience for the site is anyone that loves food, and loves to talk about food; foodies that potentially love to travel, to eat, and to cook and make cocktails.  They would likely be cultured and sophisticated people, and as such I wanted to style the site with a clean, clear, uncluttered, and sophisticated design with a colour scheme that makes the site feel modern.  I chose a fairly muted colour scheme with mostly black, white and grey, but with an occasional pop of colour coming from magenta headings and buttons.  I felt that this would provide the ideal backdrop for the colourful plates of food and cocktails that would be displayed in featured images.  

![Color Scheme](documentation/colour_scheme.png)

In terms of typography, I chose one clean, easy to read, style for most of the text (Raleway) and two cursive styles that were a bit more playful and adventurous for the headings (Glass Antiqua and Reenie Beanie):

![Raleway](documentation/raleway.png)
![Glass Antiqua](documentation/glass_antiqua.png)
![Reenie Beanie](documentation/reenie_beanie.png)

At the outset of the project, I created the following wireframe designs using [Figma](https://www.figma.com/):

![Desktop List Screens](documentation/wireframes/Desktop_List_Screens.png)
![Mobile List and About Screens](documentation/wireframes/Mobile_List_About_Screens.png)
![Desktop About Screens](documentation/wireframes/Desktop_About_Screen.png)
![Desktop Post Screens](documentation/wireframes/Desktop_Post_Screens.png)
![Mobile Post Screens](documentation/wireframes/Mobile_Post_Screens.png)

## Database Schema

The planning and design of the wireframes helped me to decide on the database schema I would need, and this was created using [LucidChart](https://www.lucidchart.com/):

![Gabby Gourmand ERD](documentation/Gabby_Gourmand_ERD.jpeg)

As detailed above, the main database models for the site are the review and recipe models.  The user model comes from the Django built in model.  There is also a model to allow comments to be left for recipes, but not reviews.  I did not want users to be able to add comments to reviews since my aim for the site was to encourage restaurant owners to make requests to the site admins for restaurant reviews, without the fear of having random user comments added to their reviews.  Restaurant reviews would include an overall rating and a measure of the price / cost of a meal at the restaurant.  Recipes, however, are more informal blog posts where users can add comments that perhaps suggest the use of a different ingredient or technique to make the recipe better.  Recipes can be either 'food' or 'cocktail' recipes through the use of 'choices' on the type field.

## Features & User Story Planning

In order to plan the project, I used agile methodologies.  I created a project kanban board and populated it with a number of user stories (see below), based on the following epics.

 - Epic 1: Create a website thats displays restaurant reviews to allow users to plan their next restaurant visit.  Includes user stories [#8](https://github.com/Jem212Mac/the-gabby-gourmand/issues/8), [#13](https://github.com/Jem212Mac/the-gabby-gourmand/issues/13), [#9](https://github.com/Jem212Mac/the-gabby-gourmand/issues/9), and [#2](https://github.com/Jem212Mac/the-gabby-gourmand/issues/2).
 - Epic 2: Create a website that displays food and cocktail recipes to allow users to plan their next meal / cocktail.  Includes user stories [#8](https://github.com/Jem212Mac/the-gabby-gourmand/issues/8), [#11](https://github.com/Jem212Mac/the-gabby-gourmand/issues/11), [#12](https://github.com/Jem212Mac/the-gabby-gourmand/issues/12), [#9](https://github.com/Jem212Mac/the-gabby-gourmand/issues/9) and [#2](https://github.com/Jem212Mac/the-gabby-gourmand/issues/2).
 - Epic 3: Create a website that allows users to comment on recipes and to interact with each other through blog comments.  Includes user stories [#4](https://github.com/Jem212Mac/the-gabby-gourmand/issues/4), [#3](https://github.com/Jem212Mac/the-gabby-gourmand/issues/3), [#6](https://github.com/Jem212Mac/the-gabby-gourmand/issues/6), [#7](https://github.com/Jem212Mac/the-gabby-gourmand/issues/7) [#10](https://github.com/Jem212Mac/the-gabby-gourmand/issues/10) and [#5](https://github.com/Jem212Mac/the-gabby-gourmand/issues/5).
 - Epic 4: Create a website that allows restaurant owners to request reviews and users to collaborate with the site owner.  Includes user stories [#14](https://github.com/Jem212Mac/the-gabby-gourmand/issues/14), [#21](https://github.com/Jem212Mac/the-gabby-gourmand/issues/21), [#20](https://github.com/Jem212Mac/the-gabby-gourmand/issues/20), and [#22](https://github.com/Jem212Mac/the-gabby-gourmand/issues/22).

I decided on two iterations for the project.  My main aim for the first iteration was to complete most of the user stories, while the second iteration would focus more on styling the website, testing the website and completing documentation.  I used MoSCow prioritisation to prioritise the user stories and tasks in each iteration.  I estimated user stories and tasks based on the following user story since I thought it was one of the smallest pieces of work to be undertaken.  Giving this an estimate of one story point, I estimated other user stories relative to this one using a Fibonnaci sequence.

![Baseline for estimates](documentation/kanban/Baseline_for_estimates.png)

Since I had no 'velocity' measures to use to give an indication of how many story points I could complete in an iteration, I estimated, based on my baseline user story, that I could complete 50 story points per iteration.  As such, I ensured that iteration one included no more than 30 story points (60%) that were MUST HAVE or SHOULD HAVE priorities.  The kanban board for iteration one at the outset looked like this:

![](documentation/kanban/Iteration1-Must_Should.png)
![](documentation/kanban/Iteration1-Could_Wont.png)

Towards the end of Iteration 1, I found that I had completed all of the tasks and user stories for the iteration, and I had some time left spare.  Therefore, I moved some more user stories from the backlog to Iteration 1:

![](documentation/kanban/Iteration1-Extra_1.png)
![](documentation/kanban/Iteration1-Extra_2.png)

These additional user stories totalled 5 story points, so by the end of iteration 1 I had completed 55 story points, and this provided me with a 'velocity' measure that I could use for Iteration 2.

For Iteration 2, I included user stories totalling 55 story points, with MUST HAVE and SHOULD HAVE priorities totalling 32 story points (less than 60%):

![](documentation/kanban/Iteration_2_all.png)

At the end of Iteration 2, however, I found that I did not have time to complete the following user stories, and I marked these as WONT DO and moved them back to the backlog.  In Iteration 2, I completed 48 story points.

![](documentation/kanban/Wont_Do.png)

## Technologies used

- ### Languages:
    
    + [Python 3.12.2](https://www.python.org/downloads/release/python-385/): the primary language used to develop the server-side of the website.
    + [JS](https://www.javascript.com/): the primary language used to develop interactive components of the website.
    + [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML): the markup language used to create the website.
    + [CSS](https://developer.mozilla.org/en-US/docs/Web/css): the styling language used to style the website.

- ### Frameworks and libraries:

    + [Django](https://www.djangoproject.com/): python framework used to create all the logic.
    + [Bootstrap](https://getbootstrap.com/): used for styling the project.

- ### Databases:

    + Code Institute PostgreSQL Database: database used to store all the data.

- ### Other tools:

    + [Git](https://git-scm.com/): the version control system used to manage the code.
    + [Pip3](https://pypi.org/project/pip/): the package manager used to install the dependencies.
    + [Gunicorn](https://gunicorn.org/): the webserver used to run the website.
    + [Django-allauth](https://django-allauth.readthedocs.io/en/latest/): the authentication library used to create the user accounts.
    + [Django-crispy-forms](https://django-cryptography.readthedocs.io/en/latest/) was used to control the rendering behavior of Django forms.
    + [Heroku](https://id.heroku.com/login): the cloud platform used to host the website.
    + [GitHub](https://github.com/): used to host the website's source code.
    + [Chrome DevTools](https://developer.chrome.com/docs/devtools/open/) was used to debug the website.
    + [Font Awesome](https://fontawesome.com/) was used to create the icons used in the website.
    + [Google Fonts](https://fonts.google.com/) was used to select fonts for the website.
    + [Favicon.io](https://favicon.io/) was used to generate a favicon for the website.
    + [Coolers](https://coolors.co/) was used to generate the colour scheme for the website.
    + [LucidChart](https://www.lucidchart.com/) was used to create the ERD.
    + [Figma](https://www.figma.com/) was used to create wireframes for the site.
    + [Cloudinary](https://cloudinary.com/) was used to store featured images for the website.
    + [Am I Responsive](https://ui.dev/amiresponsive?) was used to create the headline image for the README.md
    + [W3C Validator](https://validator.w3.org/) was used to validate HTML5 code for the website.
    + [W3C CSS validator](https://jigsaw.w3.org/css-validator/) was used to validate CSS code for the website.
    + [JShint](https://jshint.com/) was used to validate JS code for the website.
    + [PEP8](https://pep8ci.herokuapp.com/) was used to validate Python code for the website.
    + [Table to Markdown](https://tabletomarkdown.com/) was used to convert excel tables into markdown for the TESTING.md file.

## Local Development
Gitpod was used as the IDE for local development of the application and GitHub was used for version control.

## Testing
For details of all testing performed, including validator testing, manual testing, and automated testing, please see [TESTING.md](TESTING.md).  This also includes details of bugs found and resolved throughout the development process.

## Forking

If you would like to work on this code you can click on the repository here (https://github.com/Jem212Mac/the-gabby-gourmand) and click on 'Fork' to create your own fork of the code to work on.

## Deployment

The application was deployed to Heroku.  In order to deploy to Heroku, the following steps were performed:

1. 'pip3 install gunicorn~=20.1' was used in the IDE terminal to install a production ready webserver for Heroku.
2. The command 'Pip3 freeze --local > requirements.txt' was used in the IDE terminal in order to create a requirements.txt file which included the dependencies for the project.  Heroku needs this file to install the required dependencies before the application is run.
3. A Procfile containing 'web: gunicorn gabbygourmand.wsgi' was created in the root of the project directory.
4. ,'.herokuapp.com' was added to the allowed hosts in the project settings.py file.
5. I created a new Heroku account here: (https://id.heroku.com/login).
6. From the Heroku dashboard I clicked 'Create new app' and input a unique name for the app, a region, and clicked 'create app'.
7. I clicked on the Settings tab and went to the Config Vars section.
8. I added the appropriate cloudinary and database url details to Config Vars.
9. I clicked on the 'Deploy' tab, chose Github as my deployment method, and searched for my github repository to connect.
10. For this project I chose to manually deploy at regular intervals.

## Future Enhancements

Given more time there are a number of enhancements I would like to make to the website:
1. I would use a modal or popup to edit comments to free up some space on the recipe pages.
2. I would add search functionality to the navbar to allow users to search for restaurants or recipes.
3. I would add 'forgot password' functionality to the Sign In page to allow a user to retrieve a new password via email address, or setup a new password.
4. I would allow Sign Up or Sign In with social media accounts.
5. I would add google maps iFrames to show where restaurants are located.


## Credits & Acknowledgements

 - On a number of occasions I contacted Tutor Support to help me better understand certain coding practices and techniques better (e.g. using bootstrap cards) and I would like to thank them for their help and support.
 - I would like to thank my mentor, Iuliia Konovalova, for her guidance during this project.  I really think her advice helped me from the outset.