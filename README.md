# Bangazon API


## To Run This App

1. Clone the repo.

**If you have not set up a virtual environment, do this stuff the first time you want to run this app:**

2. From the command line cd into the project directory
3. Run the following command: ```python -m venv bangazonvenv```
  * Note: the gitignore will automatically exclude any directory ending with "venv".
4. CD into the bangazonvenv directory
5. Run the following command: ```. Scripts/activate``` (might be different for Mac users)
  * You will know the virtual environment is running when the command prompt is preceded with ```(bangazonvenv)```
6. CD into the project root directory (should be a sibling of the bangazonvenv directory)
7. Run the following command: ```pip install django djangorestframework```
8. Run the following command: ```python manage.py runserver```
9. Open a web browser and navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

**If you've already installed Django, etc. inside your virtual environment**

2. From the command line, cd into your bangazonvenv directory
3. Run the following command: ```. Scripts/activate``` (might be different for Mac users)
4. CD into the root directory (wherever the manage.py file is located).
5. Type ```python manage.py runserver``` into the command line.
6. Open a web browser and navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## To Reset the Database

(These instructions are unfinished right now)

1. Open the database in DB Browser.
1. 