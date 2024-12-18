from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from . models import*
from django.contrib import messages
from django.contrib.auth.models import User
import os

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
                    file=data1.pic1.url
                    file=file.split('/')[-1]
                    os.remove('media/'+file)
                    data.delete()
                    data1.pic1=image1
                if image2:
                    file=data1.pic2.url
                    file=file.split('/')[-1]
                    os.remove('media/'+file)
                    data.delete()
                    data1.pic2=image2
                if image3:
                    file=data1.pic3.url
                    file=file.split('/')[-1]
                    os.remove('media/'+file)
                    data.delete()
                    data1.pic3=image3
                data1.save()

            return redirect(shop_home)
        else:
            return render(req,'shop/carousels.html')
    else:
        return render(ff_login)
def banner2(req):
    if 'shop' in req.session:
        if req.method == 'POST':
            image1 = req.FILES.get('img1')
            image2 = req.FILES.get('img2')
            name = req.POST.get('name')  
            discrp = req.POST.get('dis')
            data = Banner2.objects.all()
            id = [i.pk for i in data]
            
            if not data:
                data = Banner2.objects.create(pic1=image1, pic2=image2, b_name=name, b_dis=discrp)
                data.save()
            else:
                data1 = Banner2.objects.get(pk=id[0])
                
                if image1:
                    file = data1.pic1.url
                    file = file.split('/')[-1]
                    os.remove('media/' + file)
                    data1.pic1 = image1

                if image2:
                    file = data1.pic2.url
                    file = file.split('/')[-1]
                    os.remove('media/' + file)
                    data1.pic2 = image2  

                data1.b_name = name  
                data1.b_dis = discrp 

                data1.save() 

            return redirect(banner2)
        else:
            return render(req, 'shop/banner2.html')


    
def brand(req):
    if 'shop' in req.session:
        if req.method=='POST':
            b_name=req.POST['brandname']
            b_name=b_name.lower()
            try:
                brd=Brand.objects.get(name=b_name)
            except:
                data=Brand.objects.create(name=b_name)
                data.save()
            return redirect(brand)
        brands=Brand.objects.all()
        return render(req,'shop/brand.html',{'brands':brands})
    else:
        return render(ff_login)
    
def addcat(req):
    if 'shop' in req.session:
        if req.method=='POST':
            cat_name=req.POST['catname']
            cat_name=cat_name.lower()
            try:
                cr=Category.objects.get(c_name=cat_name)
            except:
                data=Category.objects.create(c_name=cat_name)
                data.save()
            return redirect(addcat)
        category=Category.objects.all()
        return render(req,'shop/category.html',{'category':category})
    else:
        return render(ff_login)



def addpro(req):
    if 'shop' in req.session: 
        if req.method=='POST':
            pid=req.POST['pid']
            name=req.POST['name']
            dis=req.POST['dis']
            price=req.POST['price']
            offer_price=req.POST['offer_price']
            color=req.POST['color']
            image=req.FILES['img']
            brands=req.POST['brand']
            category=req.POST['category']
            cat=Category.objects.get(pk=category)
            brd=Brand.objects.get(pk=brands)
            data=Product.objects.create(pid=pid,name=name,dis=dis,price=price,offer_price=offer_price,color=color,img=image,category=cat,brand=brd)
            data.save()
            return redirect(sizes)
        else:
            brands=Brand.objects.all()
            category=Category.objects.all()
            return render(req,'shop/addpro.html',{'brands':brands,'category':category})                                                                                             #not completed
    else:
        return render(ff_login)

def sizes(req):
    if 'shop' in req.session:
        if req.method=='POST':
            products=req.POST['p_name']
            size=req.POST['size']
            stock=req.POST['stock']
            prd=Product.objects.get(pk=products)
            data=Size.objects.create(product=prd,size=size,stock=stock)
            data.save()
            return redirect(addpro)
        else:
            productss=Product.objects.all()
        return render(req,'shop/size.html',{'products':productss})
    else:
        return render(ff_login)
    
def viewprd(req):
    if 'shop' in req.session:
        pro=Product.objects.all()
        # brd=Brand.objects.get()
        return render(req,'shop/viewproduct.html',{'products':pro})
    else:
        return render(ff_login)
    

def updateproduct(req,cid):
    if req.method == 'POST':
        pid = req.POST['pid']
        name = req.POST['name']
        dis = req.POST['dis']
        price = req.POST['price']
        offer_price = req.POST['offer_price']
        color = req.POST['color']
        image = req.FILES.get('img')
        brands = req.POST['brand']
        category = req.POST['category']

        cat = Category.objects.get(pk=category)
        brd = Brand.objects.get(pk=brands)

        if image:
            Product.objects.filter(pk=cid).update(
                pid=pid, name=name, dis=dis, price=price, 
                offer_price=offer_price, color=color, img=image, 
                category=cat, brand=brd
            )
            data = Product.objects.get(pk=cid)
            data.img = image
            data.save()
        else:
            Product.objects.filter(pk=cid).update(
                pid=pid, name=name, dis=dis, price=price, 
                offer_price=offer_price, color=color, 
                category=cat, brand=brd
            )

        return redirect(viewprd)

    else:
        try:
            data = Product.objects.get(pk=cid)
            brands = Brand.objects.all()
            categories = Category.objects.all()
            size=Size.objects.filter(product=data)
            print (size)
            return render(req, 'shop/update.html', {'data': data, 'brands': brands, 'categories': categories,'sizes':size})
        except:
            return redirect(viewprd)

def updatesize(req,sid):
        if req.method=='POST':
            size=req.POST['size']
            stock=req.POST['stock']
            siz=Size.objects.get(pk=sid)
            siz.size=size
            siz.stock=stock
            siz.save()
            return redirect('updateproduct',cid=siz.product.pk)
        else:
            productss=Product.objects.get(pk=sid)
        return render(req,'shop/size.html',{'products':productss})


# --------------------user-------------------

def user_home(req):
    if 'user'in req.session:
        banner=Banner.objects.all()[:1]
        products=Product.objects.all()[::-1][:5]
        banner2=Banner2.objects.all()
        return render(req,'user/user_home.html',{'banners':banner,'products':products,'pbanner':banner2})
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
    
def mens(req):
    if 'user'in req.session:
        data=Category.objects.get(c_name='mens')
        menz=Product.objects.filter(category=data)
        return render(req,'user/mens.html',{'products':menz})
    else:
        return redirect(ff_login)
    
def womens(req):
    if 'user'in req.session:
        data=Category.objects.get(c_name='womens')
        womenz=Product.objects.filter(category=data)
        return render(req,'user/womens.html',{'products':womenz})
    else:
        return redirect(ff_login)    
def kids(req):
    if 'user'in req.session:
        data=Category.objects.get(c_name='kids')
        kidz=Product.objects.filter(category=data)
        return render(req,'user/kids.html',{'products':kidz})
    else:
        return redirect(ff_login)    
def details(req,pid):
    data=Product.objects.get(pk=pid)
    siz=Size.objects.filter(product=data)
    select_size=req.session.get('size')
    print(select_size)
    return render(req,'user/details.html',{'products':data,'sizes':siz,'selected_size':select_size})

def selectsize(req,sid):
    siz=Size.objects.get(pk=sid)
    req.session['size']=siz.pk
    return redirect('details',pid=siz.product.pk)
    
def allproducts(req):
    data=Product.objects.all()
    return render(req,'user/allproducts.html',{'products':data})

def view_cart(req):
    user=User.objects.get(username=req.session['user'])
    data=Cart.objects.filter(user=user)
    return render(req,'user/cart.html',{'cart':data})

def add_to_cart(req, pid):
    product = Product.objects.get(pk=pid)
    user = User.objects.get(username=req.session['user'])
    sizes = Size.objects.get(size=req.session['size'])

    try:
        cart = Cart.objects.get(product=product, user=user)
        cart.qty += 1
        cart.save()
    except Cart.DoesNotExist:
        Cart.objects.create(product=product, user=user, size=sizes,qty=1)

    return redirect('view_cart')






def aboutus(req):
    return render(req,'user/aboutus.html')

def contactus(req):
    return render(req,'user/contactus.html')

    
