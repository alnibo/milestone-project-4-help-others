[![Build Status](https://travis-ci.org/alnibo/milestone-project-4-help-others.svg?branch=master)](https://travis-ci.org/alnibo/milestone-project-4-help-others)

# Help others

Stream Four Project - Full Stack Frameworks with Django Milestone - Code Institute

![Image of Help Others Homepage](https://github.com/alnibo/milestone-project-4-help-others/blob/master/Other/help-others.jpg)

This website connects private donors with foundations, initiatives and nonprofits in many countries all over the world. We help nonprofits access funding and support by sharing their projects with our community. There are many projects in over 8 categories, to which users can donate to.

## Table of Contents

1. [Demo](#demo)
2. [UX](#ux)
3. [Database](#database)
4. [Features](#features)
5. [Technologies Used](#technologies-used)
6. [Testing](#testing)
7. [Deployment](#deployment)
8. [Credits](#credits)

## Demo

Check out the deployed website [here](https://help-others.herokuapp.com/).

## UX

To create a sleek look and a homogeneous experience for the user I used the colors grey, white and black consistently throughout the project. For a little bit of color I styled certain buttons in orange and the delete/remove buttons in red.

In order to create an easy and intuitive user experience I designed the website in a way where it is simple for the user to use.

### Target Audience

The website targets anyone who is interested in donating to a good cause. Projects supporting education, health care, human services and many more are availabe. User can browse through the website and read about the different projects before selecting them and paying via credit card. Additionally this website offers the possibility for users, like small and medium sized nonprofit organisations, to add their own donation projects, in order to share them with the community and enhance chances of funding.

### User Stories

As a user I expect/would like/need:

1. to view clear information about the site's purpose.

2. to create an account in order to make donations to my favorite projects.

3. to change my password.

4. to view existing projects in order to find some that I decide to donate to.

5. to have a search function to look for specific projects/initiatives.

6. to have the projects sorted in different categories in order to look for projects that are supporting a specific cause.

7. to view a more detailed view of each project.

8. to add projects in order to share them with others and enable them to donate money.

9. to edit the projects that I have added.

10. to delete the projects that I have added.

11. that no other user is able to edit and delete the projects that I added.

12. to have a profile page where I can see my user details and all the projects that I have added.

13. to select how much I want to donate for a project and add it to the cart.

14. to be able to view the selection that I have added to the cart and amend the amount I want to donate.

15. to donate money to the selected projects via a credit card.

16. to see my donation history.

### Wireframes

In the planing process using [Balsamiq](https://balsamiq.cloud/) [these wireframes](https://github.com/alnibo/milestone-project-4-help-others/tree/master/Other/Wireframes) were created in order to design the layout for this project for mobile, medium and desktop views.

## Database



## Features

### Existing Features

#### Page Structure

- **Navbar:** Using Bootstrap, the navbar is fixed at the top and collapses on medium and small devices. It is then accessible through a button that enables a dropdown menu. On the left side the navbar contains the website's name and the links to 'Home', 'Projects' and 'Categories', which opens a dropdown menu with the different project categories. These links on the left side are always visible. If the user is logged in the the right side of the navbar contains a personalized link to the user's profile page, 'Logout', 'Cart' and a number that will display the amount of projects that have already been added to the cart. If the user is not logged in, the right side of the navbar will only display 'Register' and 'Login' buttons.

- **Footer:** The footer contains a GitHub linke and an educational disclaimer.

#### Forms

- **Register form:** the register form enables users to create an account in order to make donations. The input fields are email address, username and two password fields (the password needs to be repeated to confirm).

- **Login form:** the login form enables existing user to login, make donations, add, edit and delete their projects and see their donation history.

- **Add project form:** this form enables users to add their own projects that they want to share with other users.

- **Edit project form:** this form enables users to edit and update their own projects.

- **Order/Contact and Payment form:** these forms are used during the checkout and enable the user to input his/her personal contact information as well as credit card details in order to complete the donation.

- **Search bars:** enables user to search for specific projects.

#### Buttons

- **Read More button:** in order to view more details about the projects.

- **Add button:** when entering an amount, by clicking on 'Add' the user is able to add the project to the cart.

- **Amend button:** when changing the amount of a project in the cart the user can update the cart by pressing on 'Amend'.

- **Cart delete button:** if wrongfully added to the cart a user can click the red delete button to remove the project from the cart.

- **Checkout button:** when satisfied with selected project a user can click on 'Checkout' in order to enter his/her payment details.

- **Submit Payment button:** after having entered the neccessary contact and payment information by clicking 'Submit Payment' the user is finishing the donation process.

- **Edit and Delete buttons:** for each project a user has added when clicking on the edit and update the projects. The delete button enables the user to fully delete the project from the database.

- **Cancel buttons:** enables the user to cancel when adding or editing a project.

- **See donation history button:** enables the user to see the projects he/she has previously donated to.

- **Change password button:** enables the user to change the password.

- **Back to top button:** enables the user to jump back to the top. This feature is escpecially helpful when many projects have been added. I added `scroll-behavior: smooth;` to ensure a smooth scrolling behavior, which however does not work in Internet Explorer and Safari.

#### Other

- **Search bars:** the search bars help the user quckly finding certain projects.

- **Messages:** after certain actions (e.g. submiting forms) the user is given a status update in form of an alert message that pops up on the top of the page and vanishes again after 3 seconds.

### Features Left to Implement

- **Thousand Separators for money amounts:** Initially I included `USE_THOUSAND_SEPARATOR = TRUE`because I wanted to have the Euro amount displayed with a thousand separator. However, this also added a thousand separator on the year (in Payment form and on the 'Donation History' page). This is why I concluded not to use it. I tried other solutions, but these changed the numbers into strings, which didn't work for me. Fixing this is something I would like to work on for the future.

- **Reset Password:** As mentioned in the [testing section](#testing) the reset password feature doesn't seem to be working. I tried all kinds of solutions but none of them worked for me. This is also something that needs to be figured out in the future.

- **Pagination:** Once more and more projects will be added in the future it would make sense to include a pagination feature.

- **Search Bar:** I would also like the user to be able to not only search for a project's name but also enabling the user searching the project's descriptions.

## Technologies Used

1. HTML - this standard markup language was used for the structure and layout of this website

2. CSS - to describe the style of the HTML document

3. JavaScript - to enable interactive features in my website, such as e.g. the 'back to the top' button and the alert messages

4. [Python](https://www.python.org/) - the core language of this website

5. [Django](https://www.djangoproject.com/) - a core python web framework

6. [jQuery](https://jquery.com/) - used to initialize message elements.

7. [Bootstrap](https://getbootstrap.com/) - a front-end component library to build a responsive website. With Bootstraps grid system the layout of this website was created. Other Bootstrap features used for this website are buttons, forms, navbar, footer, badge

8. [Font Awesome](https://fontawesome.com/v4.7.0/) - icons for better readability and styling

9. [Github](https://github.com/) - used for development version control using Git

10. [Heroku](https://heroku.com) - this cloud platform was used to run the deployed application

11. [Travis](https://travis-ci.org/) - used to build and test the code

12. [Gitpod](https://www.gitpod.io/) - this online IDE was used for the development of this application

13. [Balsamiq](https://balsamiq.cloud/) - this web-based mockup tool was used to visualize the layout and design of the website

## Testing

### Code Validation

#### HTML

The [W3C CSS Validation Service](https://validator.w3.org/) was used to validate HTML code.

The error "bad value `search` for attribute `type` on element `button`" was shown, so I removed it.

Another error was shown that "the value of the `for` attribute of the `label` element must be the id of a non-hidden form control". So, for the project pages I added `{{ project.id }}` as the value of the `for`attribute of the `label`element and as the `id` of the form control. For the cart page I added `{{ item.id }}` instead.

No errors remained.

#### CSS

The [W3C Markup Validation Service](https://jigsaw.w3.org/css-validator/) was used to validate CSS code. Several errors and warnings were shown. But these were regarding Bootstrap and were disregarded.

Otherwise no errors nor warnings were shown.

#### JavaScript

[JSHint](https://jshint.com/) was used to validate JavaScript.

The validator revealed that a `;` was missing in line 24 and that mybutton was undefined. Upon fixing that the validator was still showing that there is one undefined variable `$`. This warning was ignored as I think JSHint does not have access to external libraries, such as jQuery.

Additionally it said that the function `topFunction` is unused. But I ignored this as JSHint doesn't have access to my `html` code, where the function `topFunction`is triggered with `onclick="topFunction()"`.

No other errors were shown.

#### Python

All other functionalities were manually tested.

### Features testing

Throughout the development of this website all features were manually tested. The following table gives an overview of how the features were tested and lists resolved and remaining bugs.

| Page | Feature | Tests | Bugs |
| :---: | :---: | --- | --- |
| Base/general | Navbar | - test if navbar shows 'Home', 'What We Do', 'Projects', 'Categories' on the left and 'Register', 'Login' and cart buttons on the right when user is not authenticated <br> - test if navbar shows 'Home', 'What We Do', 'Projects', 'Categories' on the left and profile, 'Logout' and cart buttons on the right when user is authenticated.<br> - test if all navbar buttons redirect to the correct page <br> - test if 'Categories' dropdown button works, when clicked the dropdown options should appear, when clicking again or anywhere else the options should hide again <br> - test if badge appears with correct number display when projects are added to the cart <br> - test if buttons corresponding to the current page are highlighted in black font-color instead of grey <br> - test if navbar collapses on smaller devices and if dropdown button works | No bugs |
| | Footer | - test if GitHub link works and redirects user to the GitHub repository when clicking the button <br> - test if page opens in a new tab | No bugs |
| | Back to Top Button | - test if button appears when scrolling down <br> - test when clicking if page gets scrolled back to the top | No bugs |
| Index/Home | Search Bar | - test if search bar function works and displays the correct projects according to the search input | No bugs |
| | What We Do Button | - test if button redirects to the 'What We Do' page | No bugs |
| Register | Register Form | - test if validation errors get displayed when entering an existing email or an existing username, when leaving a field blank or when password 1 and password 2 don't match <br> - test if user can register when providing the correct data and gets redirected to the index/home page <br> -  check if user information is correctly added to the database | No bugs |
| | Link to Login | - test if link redirects to the login page | No bugs |
| | Already authenticated | - test if authenticated user manually enters the registration url in the browser if redirected to index/home page | No bugs |
| Login | Login Form | - test if validation errors get displayed when entering a non existing username, wrong password or leaving a field empty <br> - test if user can login when providing the correct data and gets redirected to the index/home page | No bugs |
| | Link to Register | - test if link redirects to the register page | No bugs |
| | Already authenticated | - test if authenticated user manually enters the registration url in the browser if redirected to index/home page | No bugs |
| What We Do | View all Projects Button | - test if button redirects to the projects page and displays all projects | No bugs |
| | How It Works | - test if pictures change opacity when mouse hovering over them | No bugs |
| Projects | Search Bar | - test if search bar function works and displays the correct projects according to the search input | No bugs |
| | Picture and Project Name | - test if project picture and project name are clickable and redirect to the project details page when clicked | No bugs |
| | Description | - test if project description is truncated | No bugs |
| | Add to Cart Button | - test if adding to cart functionality works when adding an amount in the input field and clicking the 'Add' button | No bugs |
| | Read More Button | - test if button redirects to the project details page | No bugs |
| Profile | See donation history Button | - test if button redirects to donation history | No bugs |
| | Change Password | - test if button redirects to the password reset page | No bugs |
| | Picture and Project Name | - test if project picture and project name are clickable and redirect to the project details page when clicked | No bugs |
| | Description | - test if project description is truncated | No bugs |
| | Add to Cart Button | - test if adding to cart functionality works when adding an amount in the input field and clicking the 'Add' button | No bugs |
| | Read More Button | - test if button redirects to the project details page | No bugs |
| | Add Project Button | - test if button redirects to the 'Add Project' page | No bugs |
| | Back to Homepage Button | - test if button redirects to the index/home page | No bugs |
| Add Project | Category Dropdown Field | - test if dropdown selection menu works | No bugs |
| | Choose file Button | - test if button opens a pop up window where an image can be selected to upload | No bugs |
| | Add Project Button | - test if button submits the form and adds the project with the correct data to the database | No bugs |
| | Cancel Button | - test if button cancel the input and redirects back to the profile page | No bugs |
| Project Details | Description | - check if entire description is visible | No bugs |
| | Add to Cart Button | - test if adding to cart functionality works when adding an amount in the input field and clicking the 'Add' button | No bugs |
| | Edit Button | - test if button is only visible when current user is the created of this project <br> - test if button redirects to the 'Edit' page of the correct project and displayes the projects details | No bugs |
| | Delete Button | - test if button is only visible when current user is the created of this project <br> - test if button opens the delete modal, asking the user if really to delete the project | No bugs |
| | Delete Modal | - test if 'Yes' button deletes project from the database and redirects to the projects page <br> - test if modal closes when clicking the 'No' button, the 'X' button on the top right or anywhere outside of the modal | Initially when deleting a project that had already been added to the cart the site would crash. Including an if statement `if pk in cart:` checking if the project is in the cart and informing the user about this solved this problem |
| Edit Project | Form | - test if form is already displaying current information about the project in the form fields | Initially it was an empty form, this was solved by passing in an initial argument for each of the form fields in form of a dictionary like this `edit_project_form = AddProjectForm(initial={'name': project.name, 'category':project.category, ... })` |
| | Category Dropdown Field | - test if dropdown selection menu works | No bugs |
| | Choose file Button | - test if button opens a pop up window where an image can be selected to upload | No bugs |
| | Confirm Changes Button | - test if button submits the edit form and correctly updates the project's information in the database | - Initially a when submitting the edit form instead of updating the current project a new project was added, by setting each field to data coming back from the form `project.name = edit_project_form.cleaned_data.get('name')` and saving it `project.save()` made it work so that it would update the existing project <br> - Another problem was that the if the user decides to keep the same image and doesn't select a new image he/she was prompted to select an image. This was solved by adding `if edit_project_form.cleaned_data.get('image'): project.image = edit_project_form.cleaned_data.get('image')` |
| | Edit Functionality | - test when manually adding the id of the project after the url ../projects/edit/ if possible to access the edit page | Initially this was possible, but solved adding this if statement `if not user == project.added_by:`, telling the user that he/she doesn't have permission to edit this project and redirecting him/her back to the project details page |
| | Cancel Button | - test if button redirects back to the correct project details page and doesn't update the project's information | No bugs |
| Donation History | Total Amount | - check if total amount is correct | Initially total amount was summing up all donations from every user of the database, this was solved by adding `filter(order__user=request.user)` to only include projects that were added by the current user |
| Cart | Picture and Project Name | - test if project picture and project name are clickable and redirect to the project details page when clicked | No bugs |
| | Amend Amount | - test if updating to cart item functionality works when changing the amount in the input field and clicking the 'Amend' button | No bugs |
| | Delete Button | - test if button removes the project from the cart | No bugs |
| | Empty Card | - test when no item in cart that text informing that cart is empty, as well as 'All Projects' and 'Back to Homepage' buttons are displayed | No bugs |
| | All Projects Button | - test if button redirects to projects page | No bugs |
| | Back to Homepage Button | - test if button redirects to index/home page | No bugs |
| | Checkout Button | - test if button redirects to checkout page | No bugs |
| | Total Amount | - test if total amount is correctly displayed | No bugs |
| Checkout | Payment Form | - test if validation errors get displayed when when leaving a field blank | No bugs |
| | Total Amount | - test if total amount is correctly displayed | No bugs |
| | Submit Payment Button | - test if button submits payment, redirects to projects page and no items are left in cart | No bugs |
| Password Reset | Resest password Button | - test when entering email address if button redirects to reset passwort done and if email is sent | Initially when clicking the 'Reset password' button the site would loud for a long time and then display an error `Network is unreachable` <br> <br> After having been in contact with tutor support I tried following Google Account set up: <br> - turn off 2-Factor Authentication <br> - turn on Less Secure Apps <br> - turn on DisplayUnlockCaptcha <br> <br> As this didn't work I tried another solution: <br> - turn off Less Secure Apps <br> - turn on 2-Factor Authentication <br> - click on app passwords <br> - set up your new app password <br> - put it in env/config vars instead of the normal email password <br> even though the redirect to the password reset done page now works there is still no email sent |
| 404 Error Page | All Projects Button | - test if button redirects to projects page | No bugs |
| | Back to Homepage Button | - test if button redirects to index/home page | No bugs |

### Responsiveness testing

Ensuring its responsiveness this website was tested across different mobile, tablet and desktop devices using Chrome developer tools. In a second step it was then tested across the most common internet browsers (Safari, Chrome, Internet Explorer, and Firefox), making sure it is compatible. For a detailed overview, please see this excel file [here](https://github.com/alnibo/milestone-project-4-help-others/blob/master/Other/Testing-resp-comp%20MS4.pdf).

### User stories testing

#### User story 1
- The user is welcomed on the 'index' page providing the user some initial information about the aim of this website to help others and some informative stats. The 'What We Do' page provides more detailed information about the site's purpose and gives clear information on how it actually works.

#### User story 2
- Each user is able to create their own account by clicking on 'Register' and filling out the register form. In order to register the user needs to input a new username that has not been used yet, an email address and enter a password. The password needs to be repeated in order to confirm. Once registered the user is redirected back to the home page.

#### User story 3
- There are two ways for the user to change the password. When loogged in the user can click the 'Change Password' button on the profile page and then entering his/her email address. If the user has forgotten the account password and is not able to login anymore, he/she can click the link 'Reset Password' on the login page in order to reset the password.

#### User story 4
- By clicking on the 'Projects' button in the navbar the user is able to view all projects that are currently open for donations.

#### User story 5
- The user is able to search for specific projects using the search bar on the home page and the projects pages.

#### User story 6
- If the user is interested in a specific cause (e.g. the environment), he/she can click the button 'Categories' in the navbar, which opens a dropdown menu with all existing causes. The user can then choose one of the categories and have projects to that category displayed.

#### User story 7
- By clicking the 'Read More' button of a project the user is able to get more information about a specific project, such as seeing the whole description of the project as well as who has added the project to the website.

#### User story 8
- Nonprofits and other organisations are able to add their projects to the site by clicking the 'Add Project' button on the profile page and filling out the 'Add Project' form. The user is prompted to enter the project's name, choose a category, give a detailed description about the project and upload an image.

#### User story 9
- In the details view of a project the user that has created this project is able to see and click the 'Edit' button in order to edit the project. He/she can change the project's information in the 'Edit Project' form and click on 'Confirm Changes'.

#### User story 10
- In the details view of a project the user that has created this project is able to see and click the 'Delete' button in order to delete the project from the database. A modal will pop up where the user is asked if he/she is really sure. Upon clicking 'Yes' the project is deleted.

#### User story 11
- If viewing the details of a project that another user has added, the edit and delete button is not visible. When entering the id of projects that other users have added in the url after .../projects/edit/ the user is informed that he/she doesn't have the permission to edit this project.

#### User story 12
- By clicking the profile button on the top right the user is able to see his/her profile page. On the top of the page the user can see the account details (username and email). Below that all projects the user has added to the website are displayed.

#### User story 13
- On the project pages a user can enter an amount between 5 and 99999 € in the form element for each project. By clicking the 'Add' button it gets added to the cart.

#### User story 14
- By clicking on the cart symbol to the far right of the navbar the user is able to see the cart with all the added projects. By changing the amount and clicking the 'Amend' button the cart gets updated.

#### User story 15
- When satisfied with the selection the user can click the 'Checkout' button, which brings him/her to the Checkout page. After entering all the required contact and payment information and clicking on 'Submit Payment' a message informs the user about the successfull donation.

#### User story 16
- After clicking the 'See donation history' button on the profile page, a user is able to see his/her donation history. All projects a user has donated to are displayed included the donated amount. On the bottom of the page to totally donated amount is shown.

## Deployment

### GitHub

I was developing the app using Gitpod. In order to keep records of the different versions during the development phase git version control was used.

Starting this project the Code Institute [GitHub Full Template](https://github.com/Code-Institute-Org/gitpod-full-template) was used. Having had the Gitpod extension installed for Chrome the template was opened in Gitpod.

The following commands were taken to save the various changes in the local repository:

- `$ git add 'filename'` to add the updated files to the staging area
- `$ git commit -m "..."` to commit the changes
- `$ git push -u origin master` to push all committed changes to the remote repository on GitHub.

### Heroku

This app is hosted using Heroku.

Following steps were taken to deploy my project:

1. Create app

    - On the Heroku website I created a new app.
    - In the heroku dashboard of my application under the 'Settings' tab I clicked on 'Reveal Config Vars', where I have set the following config vars:
    
    key | value 
    --- | ---
    AWS_ACCESS_KEY_ID | <your_key>
    AWS_SECRET_ACCESS_KEY_ID | <your_key>
    DATABASE_URL | <your_ostgres_database_url>
    DISABLE_COLLECTSTATIC | 1
    EMAIL_ADDRESS | <your_email_address>
    EMAIL_PASSWORD | <your_email_password>
    SECRET_KEY | <your_secret_key>
    STRIPE_PUBLISHABLE | <your_stripe_pk>
    STRIPE_SECRET | <your_strip_sk>

2. Login to the Heroku account in Gitpod

    - To log in to Heroku I used this command `$ heroku login -i` and entered my account details.

3. Git repository

    - following command can be used for the initial commit: `$ git commit -m "Initial Commit"`
    - and then `$ heroku git:remote -a 'app_name'` to set up the remote repository
    - In case the repository has not been created the following commands should be used:

        ```
        $ cd 'directory-name'/
        $ git init
        $ heroku git:remote -a 'app-name''
        ```

4. Connect application to remote database

    - On the Heroku website under Resources tab, under Add-ons search for "Heroku Postgres" and set up the Postgres database 
    - type `pip3 install dj_database_url` in your terminal (this allows us to connect to a database_URL)
    - then `pip3 install psycopg2` (allows us to connect to Postgres databases)

    in settings.py:

    - import dj_database_url
    - add `DATABASES = {'default': dj_database_url.parse("link to database")}`
    - type `python3 manage.py migrate` in the terminal to migrate all existing migrations to the postgres database
    - then `heroku config:set DISABLE_COLLECTSTATIC=1``
    - We need to install Gunicorn, which is required to connect to Heroku:  `pip3 install gunicorn`

5. Requirements.txt

    - For Heroku to run the app we need to create a file with all the dependencies: 'requirements.txt'
    - This file is created by using the following code: `$ pip3 freeze--local > requirements.txt`

6. Procfile

    - Heroku additionally needs Procfile, which tells Heroku how to run the project.
    - In order to create Profile use this command in the terminal: `$ echo web: web: gunicorn django_help.wsgi:application > Procfile`
    - Then run `$ heroku ps:scale web=1` to start web processes

7. Deployment

    - Similary to GitHub, changes are added and committed
    - With `$ git push heroku master` the committed code can be pushed to Heroku.

    - Alternatively, what I did, was on the Heroku website under the tab 'Deploy' select GitHub and type in your project's repository to link it to Heroku. Then further down enable Automatic Deploys, which then deploys your code to Heroku everytime you push you code to GitHub.
    

### AWS

These are the steps were taken to configure the external server Amazon AWS S3:

1. Creating bucket granting it public access
2. In properties we activate static website hosting
3. Under permissions we add the following CORS Configuration:

    ```
    <CORSConfiguration>
        <CORSRule>
            <AllowedOrigin>*</AllowedOrigin>
            <AllowedMethod>GET</AllowedMethod>
            <MaxAgeSeconds>3000</MaxAgeSeconds>
            <AllowedHeader>Authorization</AllowedHeader>
        </CORSRule>
    </CORSConfiguration>
    ```
    
4. And under Bucket Policy following code was added and the specific ARN was inserted into "Ressource":

    ```
    {
        "Version":"2012-10-17",
        "Statement":[{
            "Sid":"PublicReadGetObject",
            "Effect":"Allow",
            "Principal": "*",
            "Action":["s3:GetObject"],
            "Resource":["arn:aws:s3:::example-bucket/*"
            ]
        }
        ]
    }
    ```

5. Went to IAM (Identity and Access Management where we can manage who can access our AMazon AWS services) and created a group
6. Created a policy, where we choose S3 Full Access, in Resource added the specific ARN and added the ARN again with '/*' at the end
7. Attached created policy to group
8. Createed a user, enable Programmatic access and gave group permission
9. Downloaded csv file with access keys
10. Installed following packages, which allow us to connect Django to S3 and add 'storages to the app in settings.py

    ```
    pip3 install django-storages
    pip3 install boto3
    ```

11. Added the AWS S3 bucket details in the setting.py file:

    ```
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2100 22:00:00 GMT',
        'CacheControl': 'max-age=94608000'
    }
    AWS_STORAGE_BUCKET_NAME = '<bucket-name>'
    AWS_S3_REGION_NAME = '<region>'
    AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
    AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
    ```

12. Created a custom_storages.py file to set classes to route to the location for static and media files
13. Finally, I pushed the static files to S3 by typing: `python3 manage.py collectstatic`


### Instructions on how to run this project locally

1. Make sure you have an IDE and the following must be installed:

    - [PIP](https://pip.pypa.io/en/stable/installing/#upgrading-pip) (will be already installed if you are using Python 3.4 or above)
    - [Python 3](https://www.python.org/downloads/)
    - [Git](https://www.atlassian.com/git/tutorials/install-git)
    - [Django](https://www.djangoproject.com/)

2. Go to https://github.com/alnibo/milestone-project-4-help-others. There you can either download a copy of the repository by clicking on "Download ZIP" on the top right of the page or if you have Git installed you can clone the repository with the following command:

    ```
    git clone https://github.com/alnibo/milestone-project-4-help-others.git
    ```

3. In your local IDE you need to create two files, one called `env.py` and the other one `.gitignore`

4. Your `env.py` file should contain a SECRET_KEY,

5. Make sure that your `.gitignore` file contains `env.py` so that your environment variables won't get pushed to your remote repository.

6. Then run the following command and open port in preview or in a new browser tab:

    ```
    python3 manage.py runserver
    ```

## Credits

### Content

I found inspiration about donation categories from [this website](https://www.donasity.com/campaign/index/campaigncategorylist).

### Media

The pictures were taken from the online image libraries [Pexels](https://www.pexels.com) and [Unsplash](https://unsplash.com).

### Acknowledgements

The foundation of this project was the E-Commerce Mini Project from Code Institute. The initial code and concepts were taken from there and then extended and customized for this website.

The code for the back to top button was taken from [here](https://www.w3schools.com/howto/howto_js_scroll_to_top.asp).

To create the environment variables I followed [hese instructions](https://code-institute-room.slack.com/archives/CP07TN38Q/p1576743936008200) of Anna Greaves, a Tutor from Code Institute.

The code for smooth scrolling was seen [here](https://www.w3schools.com/howto/howto_css_smooth_scroll.asp#section1).

In order to display capital letters for a names from the database inside a django template I found [this stackoverflow example](https://stackoverflow.com/posts/14268364/edit).

I used the code from [here](https://stackoverflow.com/questions/26798623/how-to-return-the-result-on-same-page-in-django) to stay on the same page in Django.

In order to display something else when empty I used [this code](https://stackoverflow.com/questions/17435233/django-template-check-for-empty-query-set).

To set up the error pages I got information from [here](https://stackoverflow.com/questions/17662928/django-creating-a-custom-500-404-error-page).

In order to get the total sum of donations I used [this stackoverflow example](https://stackoverflow.com/questions/8616343/django-calculate-the-sum-of-the-column-values-through-query).

To have active navbar links I found a solution form [here](https://stackoverflow.com/questions/25044370/make-clicked-tab-active-in-bootstrap).

Last but not least, I would like to thank my mentor Aaron Sinnott for his help and everyone from tutur support and Student Care for their help and guidance throughout this project. 

Also the biggest thank you goes out to my girlfriend who accepted and was ok with me sitting for long ours in front of the computer and supported me every step along the way.

### This project was created for educational purposes only.