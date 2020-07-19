"""Mycoffeeshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib.auth.models import User
from django.contrib import admin
from django.urls import path, include
# from one import settings
from . import settings

from coffee.views import fn , fn1 , fn2 , fn3 , fn4 , adminlogout , seeadmin , seecustom , customdetails , customorderdetails , adminlogin , adminlog , user , reg , log , item , temp , tempH , edit , editing , delete
from coffee.views import addtocart,cart,removecart,logout,homelogin,yourcart,placedorder,neworder,bill,myorder,cancelorder,myprofile,customedit,customedited


urlpatterns = [
    path('admin/', admin.site.urls),

    path('t1', temp),
    path('t', tempH),
    path('h', fn),
    path('r', fn1),
    path('l', fn2),

    path('o', fn3),
 #admin adding and login
    path('adadm', fn4),
    path('us', user),
    path('adminlogin', adminlogin),
    path('adminlog', adminlog),
    path('adminlogout',adminlogout),

# view admins and view customers
    path('sadmin', seeadmin),
    path('seecustom', seecustom),
    path('cdetails/<i>',customdetails),
    path('cdetails/corderdetails/<i>',customorderdetails),

# adding to database table
    path('db', reg),
    path('log', log),
    path('item', item),

    path('edt/<int:i>', edit),
    path('edt/editing/<int:m>', editing),
    path('dlt/<int:id>', delete),

    path('cart/<int:i>',addtocart),
    path('cartc',cart),
    path('remove/<id>',removecart),

    path('yourcart',yourcart),
    path('placed',placedorder),

    path('logout',logout),
    path('homelogin',homelogin),


    path('neworder',neworder),
    path('bill/<id>',bill),

    path('myorder',myorder),
    path('cancelorder/<id>',cancelorder),

    path('myprofile',myprofile),
    path('customedit',customedit),
    path('customedited',customedited),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
