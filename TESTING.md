# Testing

## Manual Testing

### User Story Testing

User story testing was performed throughout site development, for each new feature, before it was merged into the master file.  User story testing was based primarily on the acceptance criteria for each of the user stories.

User Story [#8](https://github.com/Jem212Mac/the-gabby-gourmand/issues/8) and User Story [#9](https://github.com/Jem212Mac/the-gabby-gourmand/issues/9).

| Test Case ID | Test Condition / Objective                                                                                                     | Test Steps                                                                                                                                                  | Expected Results                                            | Status |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- | ------ |
| 1            | Check that a logged in site admin can create a new restaurant review in django admin.                                          | Log in to django admin with site admin credentials & click to add a review.  Add review detail and save.                                                    | Review is saved and visible in django admin.                | Passed |
| 2            | Check that a logged in site admin can create a new food recipe in django admin.                                                | Log in to django admin with site admin credentials & click to add a recipe.  Add recipe detail with type = 0 and save.                                      | Review is saved and visible in django admin.                | Passed |
| 3            | Check that a logged in site admin can create a new cocktail recipe in django admin.                                            | Log in to django admin with site admin credentials & click to add a recipe.  Add recipe detail with type = 1 and save.                                      | Review is saved and visible in django admin.                | Passed |
| 4            | Check that a logged in site admin can read and update a review in django admin.                                                | Log in to django admin with site admin credentials & click on a review to view it.  Make changes to the review and save.                                    | Updated review is saved and visible in django admin.        | Passed |
| 5            | Check that a logged in site admin can read and update a food recipe in django admin.                                           | Log in to django admin with site admin credentials & click on a food recipe to view it.  Make changes to the recipe and save.                               | Updated recipe is saved and visible in django admin.        | Passed |
| 6            | Check that a logged in site admin can read and update a cocktail recipe in django admin.                                       | Log in to django admin with site admin credentials & click on a cocktail recipe to view it.  Make changes to the recipe and save.                           | Updated recipe is saved and visible in django admin.        | Passed |
| 7            | Check that a logged in site admin can delete a review post.                                                                    | Log in to django admin with site admin credentials & click on a review to view it.  Click on delete.                                                        | Review is deleted and is no longer visible in django admin. | Passed |
| 8            | Check that a logged in site admin can delete a food recipe post.                                                               | Log in to django admin with site admin credentials & click on a food recipe to view it.  Click on delete.                                                   | Recipe is deleted and is no longer visible in django admin. | Passed |
| 9            | Check that a logged in site admin can delete a cocktail recipe post.                                                           | Log in to django admin with site admin credentials & click on a cocktail recipe to view it.  Click on delete.                                               | Recipe is deleted and is no longer visible in django admin. | Passed |
| 10           | Check that a logged in site admin can create a draft restaurant review in django admin.                                        | Log in to django admin with site admin credentials & click to add a review.  Add review detail and save as a draft (do not tick published).                 | Recipe is saved as a draft.                                 | Passed |
| 11           | Check that a logged in site admin can create a draft food recipe in django admin.                                              | Log in to django admin with site admin credentials & click to add a recipe.  Add recipe detail (with type = 0) and save as a draft (do not tick published). | Recipe is saved as a draft.                                 | Passed |
| 12           | Check that a logged in site admin can create a draft cocktail recipe in django admin.                                          | Log in to django admin with site admin credentials & click to add a recipe.  Add recipe detail (with type = 1) and save as a draft (do not tick published). | Recipe is saved as a draft.                                 | Passed |
| 13           | Check that a logged in site admin can reopen a draft restaurant review, update it, and save it as published with django admin. | Log in to django admin with site admin credentials & click on a draft review to view it.  Update the review detail, tick published, and save.               | Review is saved as published.                               | Passed |
| 14           | Check that a logged in site admin can reopen a draft food recipe, update it, and save it as published with django admin.       | Log in to django admin with site admin credentials & click on a draft food recipe to view it.  Update the recipe detail, tick published, and save.          | Recipe is saved as published.                               | Passed |
| 15           | Check that a logged in site admin can reopen a draft cocktail recipe, update it, and save it as published with django admin.   | Log in to django admin with site admin credentials & click on a draft cocktail recipe to view it.  Update the recipe detail, tick published, and save.      | Recipe is saved as published.                               | Passed |

User Story [#13](https://github.com/Jem212Mac/the-gabby-gourmand/issues/13).

| Test Case ID | Test Condition / Objective                                                                                                    | Test Steps                                                                                                               | Expected Results                                                                                                                                                                                                                                           | Status |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| 16           | Check that if any user clicks on the homepage, a list of all published restaurant reviews is displayed.                       | Click on the homepage.                                                                                                   | A list of all published restaurant reviews is displayed, and only published restaurant reviews are displayed (no draft reviews are displayed).                                                                                                             | Passed |
| 17           | Check that if any user clicks on 'The Gabby Gourmand' in the navbar, a list of all published restaurant reviews is displayed. | Click on the 'The Gabby Gourmand' in the navbar.                                                                         | A list of all published restaurant reviews is displayed, and only published restaurant reviews are displayed (no draft reviews are displayed).                                                                                                             | Passed |
| 18           | Check that if there are sufficient reviews (more than 6), pagination links can be used to access additional reviews.          | Click on the homepage.  Click on the next button if it is visible.  Once on the next page, click on the previous button. |  If there are more than 6 reviews, a Next button should be visible.  Clicking on 'Next' moves to the next page where further reviews are displayed.  A 'Previous' button should now be visible, and clickable, to take the user back to the previous page. | Passed |

User Story [#11](https://github.com/Jem212Mac/the-gabby-gourmand/issues/11).

| Test Case ID | Test Condition / Objective                                                                                                | Test Steps                                                                                                                           | Expected Results                                                                                                                                                                                                                                           | Status |
| ------------ | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| 19           | Check that if any user clicks on the food recipes page, a list of all published food recipes is displayed                 | Navigate to the food recipes page.                                                                                                   | A list of all published food recipes is displayed, and only published food recipes are displayed (no draft recipes are displayed).                                                                                                                         | Passed |
| 20           | Check that if there are sufficient food recipes (more than 6), pagination links can be used to access additional recipes. | Navigate to the food recipes page.  Click on the next button if it is visible.  Once on the next page, click on the previous button. |  If there are more than 6 recipes, a Next button should be visible.  Clicking on 'Next' moves to the next page where further recipes are displayed.  A 'Previous' button should now be visible, and clickable, to take the user back to the previous page. | Passed |

User Story [#12](https://github.com/Jem212Mac/the-gabby-gourmand/issues/12).

| Test Case ID | Test Condition / Objective                                                                                                    | Test Steps                                                                                                                               | Expected Results                                                                                                                                                                                                                                           | Status |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| 21           | Check that if any user clicks on the cocktail recipes page, a list of all published cocktail recipes is displayed             | Navigate to the cocktail recipes page.                                                                                                   | A list of all published cocktail recipes is displayed, and only published cocktail recipes are displayed (no draft recipes are displayed).                                                                                                                 | Passed |
| 22           | Check that if there are sufficient cocktail recipes (more than 6), pagination links can be used to access additional recipes. | Navigate to the cocktail recipes page.  Click on the next button if it is visible.  Once on the next page, click on the previous button. |  If there are more than 6 recipes, a Next button should be visible.  Clicking on 'Next' moves to the next page where further recipes are displayed.  A 'Previous' button should now be visible, and clickable, to take the user back to the previous page. | Passed |

User Story [#2](https://github.com/Jem212Mac/the-gabby-gourmand/issues/2).

| Test Case ID | Test Condition / Objective                                                                      | Test Steps                                                                         | Expected Results            | Status |
| ------------ | ----------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | --------------------------- | ------ |
| 23           | Check that when a user clicks on a restaurant review, a detailed view of the post is displayed. | From the home page, click on a restaurant review title or image.                   | Review detail is displayed. | Passed |
| 24           | Check that when a user clicks on a food recipe, a detailed view of the post is displayed.       | Navigate to the food recipes page.  Click on a food recipe title or image.         | Recipe detail is displayed. | Passed |
| 25           | Check that when a user clicks on a cocktail recipe, a detailed view of the post is displayed.   | Navigate to the cocktail recipes page.  Click on a cocktail recipe title or image. | Recipe detail is displayed. | Passed |

User Story [#4](https://github.com/Jem212Mac/the-gabby-gourmand/issues/4).

| Test Case ID | Test Condition / Objective                                                            | Test Steps                                                                                                                                    | Expected Results                                                                                       | Status |
| ------------ | ------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | ------ |
| 26           | Check that a user can register / sign up for an account with a username and password. | Navigate to the Register / Sign Up page.  Complete the form providing a username and password and click on Sign Up.                           | A message is displayed to let the user know they have signed in.                                       | Passed |
| 27           | Once registered, check that a user can login with their username and password.        | If still logged in, log out.  Navigate to the Sign In  page.  Sign in with the username and password used to Sign Up.                         | A message is displayed to let the user know they have signed in.                                       | Passed |
| 28           | Check that when a user is logged in they can comment on a food recipe post.           | Log in via the Sign In page.  Navigate to a food recipe post.  Add content to the body of the 'Leave a Comment' section and click submit.     | A  message is displayed to let the user know that they have added a comment that is awaiting approval. | Passed |
| 29           | Check that when a user is logged in they can comment on a cocktail recipe post.       | Log in via the Sign In page.  Navigate to a cocktail recipe post.  Add content to the body of the 'Leave a Comment' section and click submit. | A  message is displayed to let the user know that they have added a comment that is awaiting approval. | Passed |

User Story [#3](https://github.com/Jem212Mac/the-gabby-gourmand/issues/3).

| Test Case ID | Test Condition / Objective                                                                    | Test Steps                                                                                    | Expected Results                                                  | Status |
| ------------ | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- | ------ |
| 30           | Check that if a food recipe contains one or more approved comments, a user can view them.     | Navigate to a food recipe with one or more approved comments (create comments if needed).     | Any user (logged in or otherwise) can view all approved comments. | Passed |
| 31           | Check that if a cocktail recipe contains one or more approved comments, a user can view them. | Navigate to a cocktail recipe with one or more approved comments (create comments if needed). | Any user (logged in or otherwise) can view all approved comments. | Passed |

User Story [#6](https://github.com/Jem212Mac/the-gabby-gourmand/issues/6).

| Test Case ID | Test Condition / Objective                                                                                            | Test Steps                                                                                                                          | Expected Results                                                                                                                                        | Status |
| ------------ | --------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| 32           | Check that if a user is logged in, they can modify a comment they have made on a food recipe post.                    | Login.  Navigate to a comment you have made on a food recipe post.  Click on the edit button, modify the comment and submit it.     | The edited comment should appear greyed out and awaiting approval.  The user will get a message to let them know that the comment is awaiting approval. | Passed |
| 33           | Check that if a user is logged in, they can modify a comment they have made on a cocktail recipe post.                | Login.  Navigate to a comment you have made on a cocktail recipe post.  Click on the edit button, modify the comment and submit it. | The edited comment should appear greyed out and awaiting approval.  The user will get a message to let them know that the comment is awaiting approval. | Passed |
| 34           | Check that if a user is logged in, they cannot modify a comment that someone else has made on a food recipe post.     | Login.  Navigate to a comment made by someone else on a food recipe post.  Check that you cannot modify it.                         | No edit button should be displayed for the comment.                                                                                                     | Passed |
| 35           | Check that if a user is logged in, they cannot modify a comment that someone else has made on a cocktail recipe post. | Login.  Navigate to a comment made by someone else on a cocktail recipe post.  Check that you cannot modify it.                     | No edit button should be displayed for the comment.                                                                                                     | Passed |
| 36           | Check that if a user is not logged in, they cannot modify a comment on any post, regardless of the comments author.   | Do not login.  Navigate to any comment.  Check that you cannot modify it.                                                           | No edit button should be displayed for the comment.                                                                                                     | Passed |

User Story [#7](https://github.com/Jem212Mac/the-gabby-gourmand/issues/7).

| Test Case ID | Test Condition / Objective                                                                                            | Test Steps                                                                                                      | Expected Results                                                                                                                                                                                  | Status |
| ------------ | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| 37           | Check that if a user is logged in, they can delete a comment they have made on a food recipe post.                    | Login.  Navigate to a comment you have made on a food recipe post.  Click on the delete button.                 | A popup / modal should appear to confirm you want to delete.  Clicking Delete on this should delete the comment and a message will appear to let the user know that the comment has been deleted. | Passed |
| 38           | Check that if a user is logged in, they can delete a comment they have made on a cocktail recipe post.                | Login.  Navigate to a comment you have made on a cocktail recipe post.  Click on the delete button.             | A popup / modal should appear to confirm you want to delete.  Clicking Delete on this should delete the comment and a message will appear to let the user know that the comment has been deleted. | Passed |
| 39           | Check that if a user is logged in, they cannot delete a comment that someone else has made on a food recipe post.     | Login.  Navigate to a comment made by someone else on a food recipe post.  Check that you cannot delete it.     | No delete button should be displayed for the comment.                                                                                                                                             | Passed |
| 40           | Check that if a user is logged in, they cannot delete a comment that someone else has made on a cocktail recipe post. | Login.  Navigate to a comment made by someone else on a cocktail recipe post.  Check that you cannot delete it. | No delete button should be displayed for the comment.                                                                                                                                             | Passed |
| 41           | Check that if a user is not logged in, they cannot delete a comment on any post, regardless of the comments author.   | Do not login.  Navigate to any comment.  Check that you cannot delete it.                                       | No delete button should be displayed for the comment.                                                                                                                                             | Passed |

User Story [#10](https://github.com/Jem212Mac/the-gabby-gourmand/issues/10).

| Test Case ID | Test Condition / Objective                                                                | Test Steps                                                                                                                    | Expected Results                                                               | Status |
| ------------ | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ | ------ |
| 42           | Check that a logged in site admin can approve comments on a food recipe post.             | Log in to django admin as a site admin.  Click on an unapproved comment for a food recipe post.  Click approved and save.     | The comment is approved and will appear in the comments section for all users. | Passed |
| 43           | Check that a logged in site admin can approve comments on a cocktail recipe post.         | Log in to django admin as a site admin.  Click on an unapproved comment for a cocktail recipe post.  Click approved and save. | The comment is approved and will appear in the comments section for all users. | Passed |
| 44           | Check that a logged in site admin can reject (delete) comments on a food recipe post.     | Log in to django admin as a site admin.  Click on an unapproved comment for a food recipe post.  Click on Delete.             | The comment is deleted and will no longer appear for the author.               | Passed |
| 45           | Check that a logged in site admin can reject (delete) comments on a cocktail recipe post. | Log in to django admin as a site admin.  Click on an unapproved comment for a cocktail recipe post.  Click on Delete.         | The comment is deleted and will no longer appear for the author.               | Passed |

User Story [#14](https://github.com/Jem212Mac/the-gabby-gourmand/issues/14).

| Test Case ID | Test Condition / Objective                                                                                                                             | Test Steps                  | Expected Results                                                                                          | Status |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------- | --------------------------------------------------------------------------------------------------------- | ------ |
| 46           | Check that as a site user I can navigate to an about page which displays content detailing the purpose of the site and information on the site creator | Navigate to the About page. | The About page should include content and information about the site creator and the purpose of the site. | Passed |

User Story [#19](https://github.com/Jem212Mac/the-gabby-gourmand/issues/19).

| Test Case ID | Test Condition / Objective                                           | Test Steps                                                                                                          | Expected Results                                     | Status |
| ------------ | -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------- | ------ |
| 47           | Check that as a site admin, I can create content for the About page. | Login to django admin as a site admin.  Click on add for the About content.  Add content and click on save.         | The added content should appear on the About page.   | Passed |
| 48           | Check that as a site admin, I can update content for the About page. | Login to django admin as a site admin.  Click on the existing About content.  Update the content and click on save. | The updated content should appear on the About page. | Passed |

User Story [#21](https://github.com/Jem212Mac/the-gabby-gourmand/issues/21).

| Test Case ID | Test Condition / Objective                                                | Test Steps                                                                                                                                                                                  | Expected Results                                                   | Status |
| ------------ | ------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | ------ |
| 49           | Check that as a site admin I can store and review collaboration requests. | Ensure that a collaboration request has been made via the About page (complete a request if needed).  Login to django admin as a site admin.  Click on collaboration requests to view them. | All collaboration requests made should be visible in django admin. | Passed |

User Story [#5](https://github.com/Jem212Mac/the-gabby-gourmand/issues/5).

| Test Case ID | Test Condition / Objective                                                                                                | Test Steps                                                                                                                                                                                                       | Expected Results                                                                    | Status |
| ------------ | ------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ------ |
| 50           | Check that as a site user I can leave comments on food recipe posts.                                                      | Login via the Sign In page.  Navigate to the food recipes page.  Click on a food recipe. Scroll to the bottom of the page and add content in the body of the 'Leave a Comment' section and click submit.         | The comment should appear greyed out and awaiting approval.                         | Passed |
| 51           | Check that as a site user I can leave comments on cocktail recipe posts.                                                  | Login via the Sign In page.  Navigate to the cocktail recipes page.  Click on a cocktail recipe. Scroll to the bottom of the page and add content in the body of the 'Leave a Comment' section and click submit. | The comment should appear greyed out and awaiting approval.                         | Passed |
| 52           | Check that comments are 'greyed out' to me, and are not visible to other user's, until they are approved by a site admin. | Add a comment to a recipe. Logout.  Check that the comment is not visible to a logged out user.  Login as another user.  Check that the comment is not visible.                                                  | The comment should not appear to a logged out user or a user other than the author. | Passed |

User Story [#20](https://github.com/Jem212Mac/the-gabby-gourmand/issues/20).

| Test Case ID | Test Condition / Objective                                                                               | Test Steps                                                                                                       | Expected Results                                                                                                                                        | Status |
| ------------ | -------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| 53           | Check that as a site user I can complete a collaboration request form to contact the site owner / admin. | Navigate to the About page.  Scroll down to the request collaboration form.  Complete the form and click submit. | The user should get a message to let them know the request has been made.  The collaboration request should be visible in django admin to a site admin. | Passed |

User Story [#21](https://github.com/Jem212Mac/the-gabby-gourmand/issues/21).

| Test Case ID | Test Condition / Objective                                                           | Test Steps                                                                                                                                 | Expected Results                       | Status |
| ------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------- | ------ |
| 54           | Check that as a site admin, I can read collaboration requests and mark them as read. | Log in to django admin as a site admin.  Navigate to an unread collaboration request. Click on it to view it.  Tick it as 'read' and save. | The request should be saved as 'read'. | Passed |

---

## Usability / User Acceptance Testing

In addition to the testing I performed throughout the developement process which was primarily based around the user stories and the acceptance criteria (as detailed above), I also performed some exploratory testing based on the following user journeys with the goal of ensuring that the site would meet the expectations of a user in terms of ease of use, ease of navigation, responsiveness of buttons and links etc.  My aim was to ensure that user's would have a pleasant experience interacting with the site and that the overall display of content to the user was appropriate and appealing (clear, clean and uncluttered).

1. View a list of restaurant reviews and navigate through the list with the pagination buttons, ensuring they were responsive and appealing to the user.
2. Select a restaurant review to view, and view it in both portrait and landscape on a mobile device.
3. Navigate to the About page and read the About content, ensuring that all text was clear and easy to read.
4. Complete a request for collaboration form, ensuring that the submit button was responsive, that appropriate feedback is given when the user does something unwanted (e.g. doesnt add content to a field in the form), and that appropriate messaging is displayed to the user to let them know that the submission was successful.
5. View a list of food recipes and navigate through the list with the pagination buttons, ensuring they were responsive and appealing to the user.
6. Select a food recipe to view, and view it in both portrait and landscape on a mobile device.
7. View a list of cocktail recipes and navigate through the list with the pagination buttons, ensuring they were responsive and appealing to the user.
8. Select a cocktail recipe to view, and view it in both portrait and landscape on a mobile device.
9. Sign up to the site and ensure that the Sign Up process and buttons work as expected and that appropriate feedback is provided when the user tries to do something not allowed (e.g. not adding a username or password).
10. Sign in to the site and ensure that the user is provided with appropriate messaging to let them know their sign in was successful.
11. Leave a comment on a recipe ensuring that the submit button is easy to use and responsive, and the user is provided with appropriate messaging to let them know their submission was successful.
12. Edit a comment on a recipe ensuring that it is easy to do, that the buttons were responsive and that the messaging to the user is appropriate.
13. Delete a comment on a recipe ensuring that appropriate status updates are provided to the user so they know what is happening.
14. Sign out of the site and ensure that the user is provided with appropriate messaging to let them know they have successfully signed out.


All input fields / forms were checked with both positive and negative tests to ensure that users could not submit empty fields, and that feedback to the user was appropriate.

---

## Automated Testing

---

## Browser Testing

The site was tested on the below browsers, without issue:
1. Chrome
2. Safari

---

## Device Testing / Responsive Testing

The site was tested throughout the developement process to ensure that it is fully responsive using chrome development tools.  Each page of the site was checked at each of the break points to ensure that the design and layout looked good.  I also tested the site at points between the usual breakpoints and discovered that after 576px and prior to 768px, the three featured images did not display well on the review_details, food_details and cocktail_details pages.  I therefore changed my code to ensure that only two images are displayed until the 768px breakpoint is reached.

Testing was also performed on the following devices to ensure that the site was fully responsive:
1. Samsung Galaxy Flip mobile phone.
2. Samsung Galaxy Tab A7.
3. Standard Laptop.
4. Widescreen monitor.

---

## Bugs

Testing was performed throughout the development process, and I tried to fix bugs as soon as I observed them.  The following bugs were fixed during the development process:

1. The sticky footer was hiding content on the page,  I resolved this by adding a height for the footer of 60px and padding to the bottom of the body of 60px.
2. At one point i realised that there was no Previous button appearing on the second page of Restaurant Reviews.  This was because I had forgotton to add it.  I had added it to the Food Recipes and Cocktail Recipes pages but left it off the Restaurant Reviews, but it was quickly and easily resolved.
3. Although I had set unapproved comments to be greyed out, I did not feel this was obvious, so I changed the parameter used from 'faded' to 'fw-light' and the greyed out comments were more obviously greyed out.
4. I had an extended 'Log In' link at the bottom of food recipes and cocktail recipes.  This was due to a spacing error in my code which I fixed.
5. In addition to the manual testing that I performed above, i also asked a couple of potential site users to perform A/B testing.  At the time, I had styled most of my buttons (including the edit buttons for comments) with a grey colour.  This uncovered an issue whereby one of the users thought the button was greyed out, and therefore disabled.  I changed the style of the buttons as a result to avoid future confusion.

---

## Validation:

### HTML Validation:

- [Full HTML Validation Report](documentation/validation/html_validation.pdf)

- No errors or warnings were found when passing through the official [W3C](https://validator.w3.org/) validator, except for errors resulting from the use of Django Summernote.

### CSS Validation:

- [Full CSS Validation Report](documentation/validation/css_validation.png)

- No errors or warnings were found when passing through the official [W3C (Jigsaw)](https://jigsaw.w3.org/css-validator/) validator.

### JS Validation:

- [Full JS Validation Report](documentation/validation/js_validation.png)

- No errors or warning messages were found when passing through the official [JSHint](https://www.jshint.com/) validator, except for an error related to the use of Bootstrap.

### Python Validation:

- [Full Python Validation Report](documentation/validation/python_validation.pdf)

- No errors were found when the code was passed through the [CI Python Linter](https://pep8ci.herokuapp.com/).  This checking was done manually by copying python code and pasting it into the validator.

---

## Lighthouse Reports

### Home Page

![Lighthouse Report - Home Page](documentation/lighthouse_reports/Home_Page.png)

### About Page

![Lighthouse Report - About Page](documentation/lighthouse_reports/About_Page.png)

### Food Recipes Page

![Lighthouse Report - Food Recipes Page](documentation/lighthouse_reports/Food_Recipes_Page.png)

### Cocktail Recipes Page

![Lighthouse Report - Cocktail Recipes Page](documentation/lighthouse_reports/Cocktail_Recipes_Page.png)

### Review Details Page

![Lighthouse Report - Review Details Page](documentation/lighthouse_reports/Review_Details_Page.png)

### Review Food Details Page

![Lighthouse Report - Food Details Page](documentation/lighthouse_reports/Food_Details_Page.png)

### Review Cocktail Details Page

![Lighthouse Report - Cocktail Details Page](documentation/lighthouse_reports/Cocktail_Details_Page.png)

### Sign Up Page

![Lighthouse Report - Sign Up Page](documentation/lighthouse_reports/SignUp_Page.png)

### Sign In Page

![Lighthouse Report - Sign In Page](documentation/lighthouse_reports/SignIn_Page.png)

### Sign Out Page

![Lighthouse Report - Sign Out Page](documentation/lighthouse_reports/SignOut_Page.png)

---