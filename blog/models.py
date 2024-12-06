from django.db import models

# Create your models here.

# 👉____________________________dinamik modellar____________________________👈
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Product(models.Model):
    tag = [
        ('carousel', 'Carousel'),
        ('product', 'Product'),
    ]
    name= models.CharField(max_length=200)
    bio = models.TextField()
    price = models.IntegerField()
    img = models.ImageField(upload_to='product/')
    tag_type = models.CharField(choices=tag, max_length=10)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class About(models.Model):
        title = models.CharField(max_length=200)
        text = models.TextField()
        img = models.ImageField(upload_to='about/')

        def __str__(self):
            return self.title


# 👉____________________________dinamik modellar end____________________________👈





