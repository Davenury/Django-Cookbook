# Django Cookbook

## Table of contents
* [Why](#why)
* [Introduction](#introduction)
* [Technologies](#technologies)
* [Usage](#usage)
* [Database schema](#database)
* [Content of Repository](#content)

### Why
This project was prepared to Python classes at college with [piotrpolec](https://github.com/piotrpolec).

### Introduction
This cookbook allows you to add your own recipes and search for them in the website. Besides it allows you to search every recipe with some ingredient.

### Technologies
* Python (Django) - backend
* PostgreSQL - database
* HTML, CSS, JS - frontend

### Usage
* Download this project
* Install reqiurements.txt 
```
pip install reqiurements.txt
```
* You also have to have PostgreSQL database installed.
* Find file settings.py (in directory recipe) and change database login and password to your own database.
* When everything is ready, go to directory with this app (there will be a ```manage.py``` file) and run following command:
```
python manage.py runserver
```
* Site will be deployed on your local host and you'll get information about port from command line / terminal.

### Database
![Database schema](https://i.imgur.com/R5N9sjv.png)

### Content
This repository contents:
* ```recipe``` directory - files generated by Django
* ```recipes``` directory with:
  * ```migrations``` directory - migrations of database
  * ```static``` directory - all CSS and static files (like icon of website)
  * ```templates``` with its subdirectories - HTML files that generates views
  * ```admin.py``` - file generating admin view
  * ```apps.py``` - file generated by Django
  * ```help_classes.py``` - other classes that are used in application
  * ```help_functions.py``` - other functions that are used in application
  * ```models.py``` - models of app that makes database
  * ```tests.py``` - file generated by Django
  * ```urls.py``` - file generated by Django - routing of application
  * ```views.py``` - file generating views in application
* ```manage.py``` - file generated by Django
* ```requirements.txt``` - file with all modules that are needed in project
