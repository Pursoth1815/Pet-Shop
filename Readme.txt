Make an new project in Python

Step : 1

// pip install pipenv

Step : 2

// pipenv shell { pipfile will be created }

Step : 3

// pip install django 
{ 
    Incase of Error check the environment 
    // By pipenv --venv
    and select the path and run 
}

Step : 4

// django-admin startproject NewBie . { To create an new project }

Step : 5

// select the new python interpretor By 
{
    view -> command pallet -> select python interpretor
    -> select current path
}

Step : 6

// python manage.py runserver 
{ 
    to run the project & check wheather it open django server or not 
    // to stop server use command (Ctrl + C)
    // to change port python manage.py runserver 8001
    // By default sqlLite will be installed 
}

Step : 7

// pip install mysqlclient
{
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'newbie',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'root',
        'PORT': '8889',
    }
}

// change the DATABASES settings
and run the server by using step 6
}

Step : 8

******   // shop -> APP_NAME   *********

// python manage.py startapp shop
{
    Ther will be an new folder in the project 
    
    INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'shop'
]

//change the INSTALLED_APPS settings by add name of that folder
}

Step : 9

{
    create an urls.py file in shop folder

    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),
]

change main urls.py by adding include and our new path urls.py 

}

Step : 10

// create and new folder named templates and again 
create another one shop and add an index.html file


*******************     Main    **************************

Step : 11  // 

// In our app name 'shop' folder open views.py and urls.py

VIEWS.PY

from django.urls import path
from . import views
urlpatterns = [
    path('home', views.home, name="home")
]

// create an variable urlpatterns and add path of home FUNCTION urls 

URLS.py


from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "shop/index.html")

// create an FUNCTION home and render index.html 
// Incase of another page ex login, register add seprate FUNCTION and addd urls to render it

// Incase of adding the css files or other img files

Add static file in tha app folder ( not in other templates folders )

add the static root in settings.py file

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]

and check the 
    'django.contrib.staticfiles', file is presint in installed apps or not

Step : 12

// Add

MEDIA_URL = '/images/'
MEDIA_ROOT = BASE_DIR/'static' in settings.py and add folder 
in your BASE_DIR named static