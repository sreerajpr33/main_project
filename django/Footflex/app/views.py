from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from . models import*
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def shop_home(req):
    if 'shop' in req.session:
        data=Product.objects.all()
        return render(req,'shop/shophome.html',{'Products':data})
    else:
        return redirect(ff_login)

def ff_login(req):
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
            return redirect(ff_login)
    else:
        return render(req,'Login.html')
    
def ff_logout(req):
    if 'shop' in req.session or 'user' in req.session:
        logout(req)
        req.session.flush()
        return redirect(ff_login)
    else:
        return redirect(ff_login)
    
def carousel(req):
    if 'shop' in req.session:
        if req.method=='POST':
            image1=req.FILES.get('img1')
            image2=req.FILES.get('img2')
            image3=req.FILES.get('img3')
            data=Banner.objects.all()
            id=[ i.pk for i in data ]
            # print(id[0])
            if not(data):
                data=Banner.objects.create(pic1=image1,pic2=image2,pic3=image3)
                data.save()
            else :
                data1=Banner.objects.get(pk=id[0])
                if image1:
                    data1.pic1=image1
                if image2:
                    data1.pic2=image2
                if image3:
                    data1.pic3=image3
                data1.save()
            return redirect(shop_home)
        else:
            return render(req,'shop/carousels.html')
    else:
        return render(ff_login)
    
def brand(req):
    if 'shop' in req.session:
        return render(req,'shop/brand.html')
    else:
        return render(ff_login)
def addpro(req):
    if 'shop' in req.session: 
        return render(req,'shop/addpro.html')                  #not completed
    else:
        return render(ff_login)
    




# --------------------user-------------------

def user_home(req):
    if 'user'in req.session:
        banner=Banner.objects.all()[::-1][:1]
        print(banner)
        return render(req,'user/user_home.html',{'banners':banner})
    else:
        return redirect(ff_login)
def register(req):
    if req.method=='POST':
        uname=req.POST['uname']
        email=req.POST['email']
        pswd=req.POST['pswd']
        try:
            data=User.objects.create_user(first_name=uname,email=email,username=email,password=pswd)
            data.save()
        except:
            messages.info(req, "already in use")
            return redirect(register)
        return redirect(ff_login)
    else:
        return render(req,'user/register.html')
    
