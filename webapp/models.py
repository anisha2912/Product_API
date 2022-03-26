from pyexpat import model
from django.db import models

class Products (models.Model):
    product_id=models.IntegerField()
    product_name=models.CharField(max_length=100)
    product_price=models.CharField(max_length=100)
    product_size=models.CharField(max_length=100)
    product_colour=models.CharField(max_length=100)
    product_description=models.CharField(max_length=200)

    def __str__(self):
        return self.product_name
