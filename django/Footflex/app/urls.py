from django.urls import path
from . import views
urlpatterns=[
    path('',views.login),
    path('shophome',views.shop_home),
    path('register',views.register),
]