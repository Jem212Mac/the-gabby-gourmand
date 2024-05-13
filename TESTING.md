# Testing

## Manual Testing

### User Story Testing

User story testing was performed throughout site development, for each new feature, before it was merged into the master file.

User Story [#8](https://github.com/Jem212Mac/the-gabby-gourmand/issues/8) and User Story [#9](https://github.com/Jem212Mac/the-gabby-gourmand/issues/9).

| Test Case ID | Test Objective (based on Acceptance Criteria)                                                                                  | Test Steps                                                                                                                                                           | Expected Results                                            | Status |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- | ------ |
| 1            | Check that a logged in site admin can create a new restaurant review in django admin.                                          | Log in to django admin function with site admin credentials & click to add a review.  Add review detail and save.                                                    | Review is saved and visible in django admin.                | Passed |
| 2            | Check that a logged in site admin can create a new food recipe in django admin.                                                | Log in to django admin function with site admin credentials & click to add a recipe.  Add recipe detail with type = 0 and save.                                      | Review is saved and visible in django admin.                | Passed |
| 3            | Check that a logged in site admin can create a new cocktail recipe in django admin.                                            | Log in to django admin function with site admin credentials & click to add a recipe.  Add recipe detail with type = 1 and save.                                      | Review is saved and visible in django admin.                | Passed |
| 4            | Check that a logged in site admin can read and update a review in django admin.                                                | Log in to django admin function with site admin credentials & click on a review to view it.  Make changes to the review and save.                                    | Updated review is saved and visible in django admin.        | Passed |
| 5            | Check that a logged in site admin can read and update a food recipe in django admin.                                           | Log in to django admin function with site admin credentials & click on a food recipe to view it.  Make changes to the recipe and save.                               | Updated recipe is saved and visible in django admin.        | Passed |
| 6            | Check that a logged in site admin can read and update a cocktail recipe in django admin.                                       | Log in to django admin function with site admin credentials & click on a cocktail recipe to view it.  Make changes to the recipe and save.                           | Updated recipe is saved and visible in django admin.        | Passed |
| 7            | Check that a logged in site admin can delete a review post.                                                                    | Log in to django admin function with site admin credentials & click on a review to view it.  Click on delete.                                                        | Review is deleted and is no longer visible in django admin. | Passed |
| 8            | Check that a logged in site admin can delete a food recipe post.                                                               | Log in to django admin function with site admin credentials & click on a food recipe to view it.  Click on delete.                                                   | Recipe is deleted and is no longer visible in django admin. | Passed |
| 9            | Check that a logged in site admin can delete a cocktail recipe post.                                                           | Log in to django admin function with site admin credentials & click on a cocktail recipe to view it.  Click on delete.                                               | Recipe is deleted and is no longer visible in django admin. | Passed |
| 10           | Check that a logged in site admin can create a draft restaurant review in django admin.                                        | Log in to django admin function with site admin credentials & click to add a review.  Add review detail and save as a draft (do not tick published).                 | Recipe is saved as a draft.                                 | Passed |
| 11           | Check that a logged in site admin can create a draft food recipe in django admin.                                              | Log in to django admin function with site admin credentials & click to add a recipe.  Add recipe detail (with type = 0) and save as a draft (do not tick published). | Recipe is saved as a draft.                                 | Passed |
| 12           | Check that a logged in site admin can create a draft cocktail recipe in django admin.                                          | Log in to django admin function with site admin credentials & click to add a recipe.  Add recipe detail (with type = 1) and save as a draft (do not tick published). | Recipe is saved as a draft.                                 | Passed |
| 13           | Check that a logged in site admin can reopen a draft restaurant review, update it, and save it as published with django admin. | Log in to django admin function with site admin credentials & click on a draft review to view it.  Update the review detail, tick published, and save.               | Review is saved as published.                               | Passed |
| 14           | Check that a logged in site admin can reopen a draft food recipe, update it, and save it as published with django admin.       | Log in to django admin function with site admin credentials & click on a draft food recipe to view it.  Update the recipe detail, tick published, and save.          | Recipe is saved as published.                               | Passed |
| 15           | Check that a logged in site admin can reopen a draft cocktail recipe, update it, and save it as published with django admin.   | Log in to django admin function with site admin credentials & click on a draft cocktail recipe to view it.  Update the recipe detail, tick published, and save.      | Recipe is saved as published.                               | Passed |

User Story [#2](https://github.com/Jem212Mac/the-gabby-gourmand/issues/2).

| Test Case ID | Test Objective (based on Acceptance Criteria)                                                   | Test Steps                                                                         | Expected Results            | Status |
| ------------ | ----------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | --------------------------- | ------ |
| 16           | Check that when a user clicks on a restaurant review, a detailed view of the post is displayed. | From the home page, click on a restaurant review title or image.                   | Review detail is displayed. | Passed |
| 17           | Check that when a user clicks on a food recipe, a detailed view of the post is displayed.       | Navigate to the food recipes page.  Click on a food recipe title or image.         | Recipe detail is displayed. | Passed |
| 18           | Check that when a user clicks on a cocktail recipe, a detailed view of the post is displayed.   | Navigate to the cocktail recipes page.  Click on a cocktail recipe title or image. | Recipe detail is displayed. | Passed |

---

## Bugs

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