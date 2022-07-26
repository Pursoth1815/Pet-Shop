from django.urls import path
from . import views

urlpatterns = [
    # URL Path name, views file FUNCTION name, addition parameter name
    path('', views.home, name="home"),
    path('register', views.register, name="register"),
    path('login', views.loginpage, name="login"),
    path('logout', views.logoutpage, name="logout"),
    path('collections', views.collections, name="collections"),
    path('collections/<str:name>', views.collectionsview, name="collections"),
    path('collections/<str:cname>/<str:pname>',
         views.product_details, name="product_details"),
    path('vendor', views.vender, name="vendor"),
    path('profile', views.profile, name="profile"),
    path('contact', views.contact, name="contact")
]
