from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Product(models.Model):
    name= models.CharField(max_length=200)
    bio = models.TextField()
    price = models.IntegerField()
    img = models.ImageField(upload_to='product/')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.name



