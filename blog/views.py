from django.shortcuts import render

from blog.models import Product, Category, About


# Create your views here.
# 👉----------------------Pages--------------------------------------👈

def index(request):
    carousel = Product.objects.filter(tag_type='carousel')
    product = Product.objects.filter(tag_type='product')
    about = About.objects.all()[0]
    context = {
        'carousel': carousel,
        'product': product,
        'about': about
    }


    return render(request,'page/index.html', context=context)


def about(request):
    about = About.objects.all()[0]
    context = {
        'about': about
    }
    return render(request,'page/about.html', context=context)


def client(request):
    return render(request,'page/client.html', context={})


def contact(request):
    return render(request,'page/contact.html', context={})


def products(request):
    product = Product.objects.filter(tag_type='product')
    context = {
        'product': product,
    }
    return render(request,'page/products.html', context=context)


# 👉----------------------Pages end--------------------------------------👈

# 👉----------------------detaillar--------------------------------------👈

def detail(request, id):
    product = Product.objects.get(id=id)
    context = {
        'x': product
    }
    return render(request,'detail/detail.html', context=context)


# 👉----------------------detaillar end--------------------------------------👈

