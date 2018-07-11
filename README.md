# Blog

## This is a Django powered blog website. This is just for demo purpose and is not for production purpose. I have included the SECRET_KEY in setting.py so that you can test it without creating django project from scratch.

## This django project also featured google and facebook Oauth2 authentication. You need to have google auth app id and auth secret key to test the login with google+, and to login with facebook you need to have facebook app id and auth secret key. You can check official website for google Oauth2 and facebook Oauth2 for more details. Many online guides are also there.

## A local database sqlite is there, which comes with python package. You can use any database you want. Just change it in setting.py in blogweb directory. You can get setup instruction from django official doucumentation.
 
## Installation guide
### Requirements
1 Django 2.0
2 Python 3
3 social-auth-app-django
Installation instruction is there in respective official websites. social-auth-app-django can be install using pip install.

## Installation steps
* Clone or download the git respository in your local drive.
* In the setting.py change the google and facebook auth id and secret key.
* Open the directory containing the project where there is manage.py file.
* Execute the command python manage.py migrate
* Execute the command python manage.py runserver. It will start local server at 8000 port number.
* Then open the given url http://localhost:8000 in browser to play with it.

## Other options
* Same project can be done using  django-rest-framework and other front end libraries like reactjs.