from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from . models import*
from django.contrib import messages

# Create your views here.
def shop_home(req):
    if 'shop' in req.session:
        data=Product.objects.all()
        return render(req,'shop/shophome.html',{'products':data})
    else:
        return redirect(login)

def login(req):
    if 'shop' in req.session:
        return redirect(shop_home)
    if 'user' in req.session:
        return redirect(user_home)
    if req.method=='POST':
        uname=req.POST['uname']
        password=req.POST['password']
        data=authenticate(username=uname,password=password)
        if data:
            login(req,data)
            if data.is_superuser:
                req.session['shop']=uname
                return redirect(shop_home)
            else:
                req.session['user']=uname
                return redirect(user_home)
        else:
            messages.info(req, " ")
            return redirect(login)
    else:
        return render(req,'Login.html')


# --------------------user-------------------

def user_home(req):
    return render(req,'user/user_home.html')

def register(req):
    return render(req,'user/register.html')