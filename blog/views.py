from django.shortcuts import render

from blog.models import Product, Category


# Create your views here.
# 👉----------------------Pages--------------------------------------👈

def index(request):
    # categoryName = Category.objects.get(name = "carousel")
    # carousel = Product.objects.filter(category= categoryName)
    products = Product.objects.all()
    context = {
        'p': products,
    }


    return render(request,'page/index.html', context=context)


def about(request):
    return render(request,'page/about.html', context={})


def client(request):
    return render(request,'page/client.html', context={})


def contact(request):
    return render(request,'page/contact.html', context={})


def products(request):
    return render(request,'page/products.html', context={})


# 👉----------------------Pages end--------------------------------------👈

# 👉----------------------detaillar--------------------------------------👈

def detail(request, id):
    product = Product.objects.get(id=id)
    context = {
        'x': product
    }
    return render(request,'detail/detail.html', context=context)


# 👉----------------------detaillar end--------------------------------------👈

