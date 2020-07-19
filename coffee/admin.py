from django.contrib import admin
from .models import Register,Login,Item,Order
# Register your models here.
admin.site.register(Register)
admin.site.register(Login)
admin.site.register(Item)
admin.site.register(Order)