from django.db import models

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    number = models.CharField(max_length=128) 
    title = models.CharField(max_length=128)
    amount = models.CharField(max_length=128)


    def __str__(self):
        return self.title