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
    path('updates/<cid>',views.updateproduct,name='updateproduct'),
    path('updatesize/<sid>',views.updatesize),
    # user,
    path('user_home',views.user_home),
    path('aboutus',views.aboutus),
    path('contactus',views.contactus),
    path('mens',views.mens),
    path('women',views.womens),
    path('kids',views.kids),
    path('allproducts',views.allproducts),
    path('buy/<pid>',views.details,name='details'),
    path('view_cart',views.view_cart,name='viewcart'),
    path('addcart/<pid>',views.add_to_cart),
    path('select_size/<sid>',views.selectsize),

    
    
]