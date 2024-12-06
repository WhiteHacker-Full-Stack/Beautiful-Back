from django.contrib import admin

from blog.models import Product, Category, About

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(About)
