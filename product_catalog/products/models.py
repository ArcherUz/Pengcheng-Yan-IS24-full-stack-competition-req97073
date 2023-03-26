from django.db import models
import jsonfield

# Create your models here.

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255)
    product_ownerName = models.CharField(max_length=64)
    developer = jsonfield.JSONField()
    scrum_masterName = models.CharField(max_length=64)
    start_data = models.DateField()
    methodology = models.CharField(max_length=64)


    def __str__(self):
        return self.product_name