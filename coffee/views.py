from django.shortcuts import render,redirect
from django.contrib.auth.models import auth,User
from django.contrib.auth import authenticate
from django.http import HttpResponse
from .models import Register,Login,Item,Order

import datetime,time

# Create your views here.#



#
# ---------------------------    A D M I N   A C T I V I T Y     ----------------------------#
# -------------------------------------------------------------------------------------------#
def fn3(request):
    a = Item.objects.all()
    return render(request, 'owner.html', {'table': a})

def fn4(request):
    return render(request,'addadmin.html')

def adminlogin(request):
    return render(request,'adminlogin.html')
def adminlog(request):
    user = request.POST.get('username')
    psw = request.POST.get('psw')
    # print(psw)
    use = authenticate(request, username=user, password=psw)
    # print(use)          #  o/p -> jubin      ie, 'username'  it is like session creation
    # print(use.email)    #  o/p -> jubin@j.bn
    if use is not None:
        auth.login(request, use)
        return redirect(fn3)
    else:
        msg = 'Incorrect admin username or password'
        return render(request,'adminlogin.html', {'m':msg})

def adminlogout(request):
    auth.logout(request)
    return redirect(adminlogin)


def seeadmin(request):
    admin = 'Admin'
    email = 'Email'
    a = Item.objects.all()
    u = User.objects.all()
    return render(request, 'owner.html', {'table': a, 'u': u,'admin':admin,'email':email})

def seecustom(request):
    s = Register.objects.all()
    return render(request,'custom.html',{'s1':s})
def customdetails(request,i):
    r = Register.objects.filter(id=i)
    return render(request,'customdetails.html', {'R':r})
def customorderdetails(request,i):
    # r = Register.objects.get(id=i)  o/p -> also correct
    o = Order.objects.filter(reg=i,status=1).order_by('Date').reverse()
    for i in o:
        name = i.reg.Name
        return render(request,'customorderdetails.html', {'o':o, 'name':name})
    else:
        return HttpResponse("<h1 align='center' style='padding:300px; color:yellow;background-color:grey;'>No Orders !!!</h1>")

#---------------------------------------------------------#

def edit(request,i):
    # print(i)
    d = Item.objects.get(id=i)
    return render(request,'edit.html',{'d':d})
def editing(request,m):
    if request.method == 'POST':
        name = request.POST.get('item')
        price = request.POST.get('price')
        img = request.FILES.get('img')
        # print(m)
        d = Item.objects.get(id=m)
        d.Item_Name = name
        d.Price = price
        d.Image = img
        d.save()      #  ith most needed  ..Enkile save aakooo.
    return redirect(fn3)

def delete(request,id):
    d = Item.objects.get(id=id)
    # return HttpResponse('<script>alert("Helloooooo")</script>')
    d.delete()
    return redirect(fn3)

def neworder(request):
    #d = datetime.datetime.now()       # o/p -> 2020-03-20 17:54:00.705259
    d = datetime.datetime.now().date() # o/p ->  2020-03-20
    # print(d.date())                  # o/p ->  2020-03-20
    # print(d.time())                  # o/p -> 17:56:20.848692
    o = Order.objects.filter(Date=d).order_by('Time')

    order = Order.objects.all().order_by('Date').reverse
    return render(request,'neworder.html',{'o':o, 'order':order, 'd':d})

def bill(request,id):
    o = Order.objects.get(id=id)
    return render(request,'bill.html',{'o':o})

#-------------------------------------------------------------------------------------------#



#_______________________   D A T A B A S E   I N S E R T I O N   ___________________________#
#--------------------------------------------------------------------------------------------#
def user(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        uname = request.POST.get('uname')
        psw = request.POST.get('psw')
        u = User.objects.all()
        for i in u:
            if i.username == uname:
                msg = "This username already exists, Try another"
                return render(request,'addadmin.html',{'m':msg})

        us = User.objects.create_user(username=uname,password=psw,email=email)
        us.first_name = fname
        us.last_name = lname
        us.save()

        # l = Login()
        # l.Username = uname
        # l.Password = psw
        # l.reg = 'null'
        # l.save()
    return redirect(fn3)



def reg(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    gen = request.POST.get('gender')
    dob = request.POST.get('dob')
    mob = request.POST.get('mobile')
    uname = request.POST.get('username')
    pwd = request.POST.get('password')

    rev = Register.objects.all()
    for i in rev:
        if (i.Email == email):
            msg = "Already registered email. Try another one"
            return render(request, 'register.html', {'m1': msg})
        elif (i.MobileNo == mob):
            msg = "Already registered Mobile Number. Try another one"
            return render(request, 'register.html', {'m2': msg})
        elif (i.Username == uname):
            msg = "Username taken before. Take another username"
            return render(request, 'register.html', {'m3': msg})

    reg = Register()
    reg.Name = name
    reg.Email = email
    reg.Gender = gen
    reg.DOB = dob
    reg.MobileNo = mob
    reg.Username = uname
    reg.Password = pwd
    reg.save()

    log = Login()
    log.reg = reg
    log.Username = uname
    log.Password = pwd
    log.save()
    msg = name+' you successfully registered. Please Login'
    print(msg)
    # return HttpResponse(name+".. You Successfully uploaded your details")
    return render(request,'login.html',{'msg':msg})

def log(request):
    if request.method == 'POST':
        user = request.POST.get('username')
        pwd = request.POST.get('password')
        d = Login.objects.filter(Username=user,Password=pwd)
        # e = Login.objects.get(Username=user,Password=pwd)
        # e1 = e.reg
        # print(d.Username)  ->error
        # print(d)   #o/p ->  <QuerySet [<Login: Login object (1)>]>
        # for i in d:
        #    print(i.reg)     # o/p -> Register object (1)
        #print(i.Username)  #  o/p -> bibin
        # print(e1)    # o/p -> Register object (1)

        #print(e1.Email)   # o/p -> nnb@h.com
        # for i in e:
            # print(i) - o/p -> error
        # d4 = Login.objects.all()
        # print(d4) -> o/p  = <QuerySet [<Login: Login object (1)>, <Login: Login object (2)>, <Login: Login object (3)>]>

        # d1 = e1.Name
        d2 = "Hi  "
        tab = Item.objects.all()
        if d.exists():
            for i in d:
                request.session['userid'] = i.id
            # request.session['regid'] = e1
            usersession = request.session.get('userid')
            # u = Register.objects.get(id=usersession)
            # # for i in u:
            # print(u.Email)   #  o/p ->  bibinbabyanthony@gmail.com

            return redirect(homelogin)
            #return HttpResponse("Hello "+user)
        else:
            m = "Incorrect password or Username"
            m1 = {'l':m}
            return render(request,'login.html',m1)




def item(request):
    item = request.POST.get('item')
    price = request.POST.get('price')
    img = request.FILES.get('img')

    i = Item()
    i.Item_Name = item
    i.Price = price
    i.Image = img
    i.save()
    return redirect(fn3)
    # return render(request,'owner.html')



#--------------------   HH OO MM EE   ----------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------#

def fn(request):
    s = request.session.get('userid')
    if s!=None:
        return redirect(homelogin)
    name = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    tab = Item.objects.all()
    return render(request,'home.html',{'tab':tab, 'na':name})

def homelogin(request):

    name = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    tab = Item.objects.all()
    usersession = request.session.get('userid')
    l = Login.objects.get(id=usersession)
    o = Order.objects.filter(reg=l.reg,status=0)
    cartcount= len(o)
    # print(l.reg.Name)      #  o/p ->  bibin
    return render(request,'homelogin.html',{'tab':tab, 'na':name, 'd3':l.reg.Name, 'count':cartcount})

def fn1(request):
    return render(request,'register.html')
def fn2(request):
    return render(request,'login.html')
def logout(request):
    del request.session['userid']
    return redirect(fn)

#--------------------------------------------------------------------------------------------------------#



#------------------         CART  &  ORDERING          --------------  #
#______________________________________________________________________#
def addtocart(request,i):
    # print(type(i))      # o/p -> <class 'int'>
    sessn = request.session.get('userid')
    # print(sessn)
    if sessn != None:

        i = Item.objects.get(id=i)
        qnty = request.POST.get("qnty")
        # q = int(qnty)
        # print(qnty)    # o/p ->  2  -- but it is string
        d = datetime.datetime.now()
        date = d.date()        # print(d)  - o/p -> 2020-05-08
        time = d.time()     # print(time)  - o/p -> 19:43:54.975873
        print(time)
        # date = d.strftime('%Y-%m-%d')
        # time = d.strftime("%X")
        # print(date)     #  o/p  ->  2020-03-08
        # print(time)     #  o/p  ->  16:30:15
        # print(type(qnty))   # o/p -> <class 'str'>

        q = int(qnty)     #  print(type(qnty)) = o/p -> <class 'int'>
        total = i.Price * q
        # print(total)


        l = Login.objects.get(id = sessn)
        print(l.reg)
        # l1 = l.reg
        # print(l1)      # o/p ->  Register object (1)         very important
        # r = Register.objects.get(id = )
        # print(l.id)
        # print(i)    #  o/p  ->  Item Object (1)
        o = Order()
        o.item = i
        o.reg = l.reg
        o.Quantity = qnty
        o.Total_Price = total
        o.Date = date
        o.Time = time
        o.save()

        return redirect(homelogin)

    else:
        return redirect(fn2)

def cart(request):

    d = datetime.datetime.now()
    sess = request.session.get('userid')
    l = Login.objects.get(id=sess)
    # print(l.reg.id)     #  o/p ->  1
    cart = Order.objects.filter(reg=l.reg.id,status=0)
    # print(cart)   #  o/p ->  <QuerySet [<Order: Order object (66)>, <Order: Order object (67)>]>
    if cart.exists():
        g = 0
        for i in cart:
            g = g + i.Total_Price
        return render(request,'cart.html',{'cart':cart, 'g':g})
    else:
        return HttpResponse("<h1 align='center' style='padding:300px; color:yellow;background-color:grey;'>Ohh.. Your 'CART' is empty . Please order something</h1>")


def removecart(request,id):
    order = Order.objects.get(id=id)
    # delete(request,order)     #  o/p ->  error
    order.delete()
    return redirect(cart)

def yourcart(request):
    d = datetime.datetime.now()
    sess = request.session.get('userid')
    l = Login.objects.get(id=sess)
    o = Order.objects.filter(reg=l.reg, status=0)
    g = 0
    for i in o:
        g = g+i.Total_Price
    return render(request,'yourcart.html',{'o':o, 'g':g})

def placedorder(request):
    sess = request.session.get('userid')
    l = Login.objects.get(id=sess)
    o = Order.objects.filter(reg=l.reg)
    for i in o:
        i.status = 1
        i.save()

    return render(request, 'placed.html',{'l':l})

#=========================================================#


def myprofile(request):
    sess = request.session.get('userid')
    l = Login.objects.get(id=sess)
    r = Register.objects.get(id=sess)
    return render(request,'myprofile.html',{'l':l})
def customedit(request):
    sess = request.session.get('userid')
    l = Login.objects.get(id=sess)

    d = l.reg.DOB.strftime("%Y-%m-%d")    #  <- important  'KANDU PIDITHAM'
    print(d)
    r = Register.objects.get(id=sess)
    return render(request,'customedit.html',{'l':l,'d':d})
def customedited(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        mobile = request.POST.get('mobile')
        username = request.POST.get('user')
        psw = request.POST.get('psw')

        sess = request.session.get('userid')
        l = Login.objects.get(id=sess)
        l.reg.Name = name
        l.reg.Email = email
        l.reg.DOB = dob
        l.reg.Gender = gender
        l.reg.MobileNo = mobile
        l.reg.Username = username
        l.reg.Password = psw
        l.reg.save()
        return redirect(myprofile)

def myorder(request):
    sess = request.session.get('userid')
    l = Login.objects.get(id=sess)
    d = datetime.datetime.now()
    o = Order.objects.filter(Date=d,reg=l.reg,status=1)
    ord = Order.objects.filter(reg=l.reg,status=1)
    return render(request,'myorder.html',{'o':o, 'ord':ord})
def cancelorder(request,id):
    o = Order.objects.get(id=id)
    o.delete()
    return redirect(myorder)


#----------------------------------------------------------------------------#


def temp(request):
    ttab = Item.objects.all()
    for i in ttab:
        print(i)
    ttab1 = {'ttab' : ttab}
    d = datetime.datetime.now()
    # t = time.ctime()
    n = request.POST.get('n')
    name = request.POST.get('name')
    print(name)
    print(type(n))
    return render(request, 'temp.html',{'ttab' : ttab,'d':d.strftime('%x'),'t':d.strftime("%X")})
def tempH(request):
    return render(request,'temp.html')
