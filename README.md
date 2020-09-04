# ShowYourself - Blog app
![Home Page 1](screenshots/screenshot1.png)
## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
## General info
This projects lets an User to create his own Blog. User after creating an account gains ability to create and publish their own posts and also visit other Bloggers profiles.
Each Blogger can set profile his own profile picture and a bio.
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
$ git clone https://github.com/MattFrankowski/blog.git
```
Then move to the project directory and activate a Virtual Enviroment:
```
$ myvenv\Scripts\activate
```
Next, navigate project1/website directory and in command line type:
```
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```
Open browser and go to adress http://127.0.0.1:8000/

Website is now running!