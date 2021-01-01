from django.db import models

# Create your models here.
class Product(models.Model):
    prod_id=models.AutoField
    prod_name=models.CharField(max_length=50)
    desc=models.CharField(max_length=300)
    pub_date=models.DateField()
