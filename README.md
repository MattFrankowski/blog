# ShowYourself - Blog app
![Home Page 1](screenshots/main_page.gif)
## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
## General info
This projects lets an User create his own blog.\
Project features:
* User authentication system ([Login](#login), [Register](#register), [Password Change](#password-change)).
* Page restrictions for not logged Users -  using Django decorators.
* Blogger has ability to Create, Edit and Delete his posts. - CRUD functionality.
* Blogger create form, ability to set a profile photo.
* Search Blogger by given name.
* Website is fully responsible.
## Technologies
Project is created with:
* Python 3.8
* Django 3.1
* HTML
* CSS
* Bootstrap 4
## Setup
To run this project locally clone this repository:
```
$ git clone https://github.com/MattFrankowski/show_yourself.git
```
Then move to the project directory and activate a Virtual Enviroment:
```
$ myvenv\Scripts\activate
```
Next, navigate to show_yourself/website directory and in command line type:
```
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```
Open browser and go to adress http://127.0.0.1:8000/

Website is now running!

## Login
![Login](screenshots/login.png)

## Register
![Register](screenshots/register.png)

## Password change
When project is run locally emails for password resseting are sent to *sent_emails* directory as .txt file
