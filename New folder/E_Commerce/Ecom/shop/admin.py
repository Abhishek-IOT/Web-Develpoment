from django.contrib import admin
#TO create a admin we will use python manage.py createsuperuser
# Register your models here.
from . models import  Product
admin.site.register(Product)