from django.urls import path
from . import views
urlpatterns=[
    path('',views.ff_login),
    path('shop_home',views.shop_home),
    path('logout',views.ff_logout),    
    path('register',views.register), 
    path('carousel',views.carousel),
    path('banner',views.banner2),
    path('addpro',views.addpro),
    path('addbrand',views.brand),
    path('addcategory',views.addcat),
    path('sizes',views.sizes),
    path('viewproduct',views.viewprd),
    path('updates/<pid>',views.updateproduct),
    path('updatesize/<pid>',views.updatesize),
    # user,
    path('user_home',views.user_home),
    path('aboutus',views.aboutus),
    path('contactus',views.contactus),
    path('mens',views.mens),
    path('women',views.womens),
    path('kids',views.kids),
    path('buy',views.buy),
    
]