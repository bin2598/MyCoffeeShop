from django.db import models

class Register(models.Model):
    Name = models.CharField(max_length=10)
    Email = models.CharField(max_length=50)
    Gender = models.CharField(max_length=5)
    DOB = models.DateField()
    MobileNo = models.IntegerField()
    Username = models.CharField(max_length=10)
    Password = models.CharField(max_length=20)
    # order = models.ForeignKey(Order,on_delete=models.CASCADE)

class Login(models.Model):
    reg = models.ForeignKey(Register,on_delete=models.CASCADE)
    Username = models.CharField(max_length=20)
    Password = models.CharField(max_length=20)

class Item(models.Model):
    Item_Name = models.CharField(max_length=20)
    Price = models.IntegerField(default=0)
    Image = models.ImageField(upload_to='photos')        # ivide 'upload_to = ' nte avashyam illa

class Order(models.Model):
    reg = models.ForeignKey(Register,on_delete=models.CASCADE)
    item = models.ForeignKey(Item,on_delete=models.CASCADE)
    Quantity = models.IntegerField(default=0)
    Total_Price = models.IntegerField()
    Date = models.DateField()
    Time = models.TimeField()
    status = models.IntegerField(default=0)
