# The Gabby Gourmand

![The Gabby Gourmand](documentation/am_i_responsive.png)

Live Version: [The Gabby Gourmand](https://gabby-gourmand-a59f21db8e77.herokuapp.com/)


Repository: [GitHub Repo](https://github.com/Jem212Mac/the-gabby-gourmand)

Developed by [Jemima MacKenzie](https://github.com/Jem212Mac).

## About
This is a website intended to provide interested parties with a review of various restaurants.  The intended user of the site is someone who is interested in food (a foodie) who loves to dine out but also likes to cook and try new recipes.  The home page for the site provides the user with a list of restaurant reviews that they can look through to help them decide on where to dine out next, but the site also includes a page listing food recipes and a page listing cocktail recipes where users can leave comments.

## UX Design
The target audience for the site would be foodies that potentially love to travel, to eat, and to cook and make cocktails.  They would likely be cultured and sophisticated people, and as such I wanted to style the site with a clean, clear, uncluttered and sophisticated design with a colour scheme that makes the site feel modern.  I chose a fairly muted colour pallete with mostly black, white and grey, but with an occasional pop of colour coming from pink headings and buttons.  I felt that this would provide the ideal backdrop for the colourful plates of food and cocktails that would be displayed in featured images.  At the outset of the project, I created the following wireframe designs using [Figma](https://www.figma.com/):

![Desktop List Screens](documentation/wireframes/Desktop_List_Screens.png)
![Mobile List and About Screens](documentation/wireframes/Mobile_List_About_Screens.png)
![Desktop About Screens](documentation/wireframes/Desktop_About_Screen.png)
![Desktop Post Screens](documentation/wireframes/Desktop_Post_Screens.png)
![Mobile Post Screens](documentation/wireframes/Mobile_Post_Screens.png)

## Database Schema

The planning and design of the wireframes helped me to decide on the database schema I would need, and this was created using [LucidChart](https://www.lucidchart.com/), as shown below:

![Gabby Gourmand ERD](documentation/Gabby_Gourmand_ERD.jpeg)

As detailed above, the main database models for the site are the review and recipe models.  The user model comes from the Django built in model.  There is also a model to allow comments to be left for recipes, but not reviews.  I did not want users to be able to add comments to reviews since my aim for the site was to encourage restaurant owners to make requests to the site admins for restaurant reviews, without the fear of having random user comments added to their reviews.  Restaurant reviews would include an overall rating and a measure of the price / cost of a meal at the restaurant.  Recipes, however, are more informal blog posts where users can add comments that perhaps suggest the use of a different ingredient or technique to make the recipe better.  Recipes can be either 'food' or 'cocktail' recipes through the use of 'choices' on the type field.

## Features & User Story Planning

In order to plan the project, I used agile methodologies.  I created a project kanban board and populated it with a number of user stories (see below), based on the following epics.

 - Epic 1: Create a website thats displays restaurant reviews to allow users to plan their next restaurant visit.  Includes user stories [#8](https://github.com/Jem212Mac/the-gabby-gourmand/issues/8), [#13](https://github.com/Jem212Mac/the-gabby-gourmand/issues/13), [#9](https://github.com/Jem212Mac/the-gabby-gourmand/issues/9), and [#2](https://github.com/Jem212Mac/the-gabby-gourmand/issues/2).
 - Epic 2: Create a website that displays food and cocktail recipes to allow users to plan their next meal / cocktail.  Includes user stories [#8](https://github.com/Jem212Mac/the-gabby-gourmand/issues/8), [#11](https://github.com/Jem212Mac/the-gabby-gourmand/issues/11), [#12](https://github.com/Jem212Mac/the-gabby-gourmand/issues/12), [#9](https://github.com/Jem212Mac/the-gabby-gourmand/issues/9) and [#2](https://github.com/Jem212Mac/the-gabby-gourmand/issues/2).
 - Epic 3: Create a website that allows users to comments on recipe's and to interact with each other through blog comments.  Includes user stories [#4](https://github.com/Jem212Mac/the-gabby-gourmand/issues/4), [#3](https://github.com/Jem212Mac/the-gabby-gourmand/issues/3), [#6](https://github.com/Jem212Mac/the-gabby-gourmand/issues/6), [#7](https://github.com/Jem212Mac/the-gabby-gourmand/issues/7) [#10](https://github.com/Jem212Mac/the-gabby-gourmand/issues/10) and [#5](https://github.com/Jem212Mac/the-gabby-gourmand/issues/5).
 - Epic 4: Create a website that allows restaurant owners to request reviews and users to collaborate with the site owner.  Includes user stories [#14](https://github.com/Jem212Mac/the-gabby-gourmand/issues/14), [#21](https://github.com/Jem212Mac/the-gabby-gourmand/issues/21), [#20](https://github.com/Jem212Mac/the-gabby-gourmand/issues/20), and [#22](https://github.com/Jem212Mac/the-gabby-gourmand/issues/22).

I decided on two iterations for the project.  My main aim for the first iteration would be to complete most of the user stories, while the second iteration would focus more on styling the website, testing the website and completing documentation.  I used MoSCow prioritisation to prioritise the user stories and tasks in each iteration.  I estimated user stories and tasks based on the following user story since I thought it was one of the smallest pieces of work to be undertaken.  Giving this an estimate of one story point, I estimated other user stories relative to this one using a Fibonnaci sequence.

![Baseline for estimates](documentation/kanban/Baseline_for_estimates.png)

Since I had no 'team velocity' measures to use to give an indication of how many story points I could complete in an iteration, I estimated, based on my baseline user story, that I could complete 50 story points per iteration.  As such, I ensured that iteration one included no more that 30 story points (60%) that were MUST HAVE or COULD HAVE priorities.  The kanban board for iteration one at the outset looked like this:

![](documentation/kanban/Iteration1-Must_Should.png)
![](documentation/kanban/Iteration1-Could_Wont.png)

Towards the end of Iteration 1, I found that I had completed all of the tasks and user stories for the iteration, and I had some time left spare.  Therefore, I moved some more user stories from the backlog to Iteration 1:

![](documentation/kanban/Iteration1-Extra_1.png)
![](documentation/kanban/Iteration1-Extra_2.png)

These additional user stories totalled 5 story points, so by the end of iteration 1 I had completed 55 story points, and this provided me with a 'velocity' measure that I could use for Iteration 2.

For Iteration 2, I included user stories totally 55 story points, with MUST HAVE and COULD HAVE priorities totalling 32 story points (less than 60%):

![](documentation/kanban/Iteration_2_all.png)

At the end of Iteration 2, however, I have found that I did not have time to complete the following user stories, and I marked these as WONT DO and moved them back to the backlog.  In Iteration 2 I completed 48 story points.

![](documentation/kanban/Wont_Do.png)

## Local Development


## Testing
For details of all testing performed, including validator testing, manual testing, and automated testing, please see TESTING.md.  This also includes details of bugs found and resolved throughout the development process.

## Forking


## Deployment


## Future Enhancements


## Credits & Acknowledgements