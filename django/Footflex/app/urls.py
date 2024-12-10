from django.urls import path
from . import views
urlpatterns=[
    path('',views.ff_login),
    path('shop_home',views.shop_home),
    path('logout',views.ff_logout),    
    path('register',views.register), 
    path('carousel',views.carousel),
    path('addpro',views.addpro),
    path('addbrand',views.brand),
    # user,
    path('user_home',views.user_home),
    path('aboutus',views.aboutus),
    path('contactus',views.contactus),
]