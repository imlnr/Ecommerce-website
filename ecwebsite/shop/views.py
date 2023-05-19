from django.shortcuts import render
from django.http import HttpResponse
from shop.models import Product
from math import ceil
# Create your views here.

def index(request):
    products= Product.objects.all()
    n= len(products)
    nSlides= n//4 + ceil((n/4)-(n//4))
    allProds=[[products, range(1, len(products)), nSlides],[products, range(1, len(products)), nSlides]]
    params={'allProds':allProds }
    return render(request,"shop/index.html", params)

def about(request):
    return render(request, 'shop/about.html')
def contact(request):
    return HttpResponse('this is contact page')
def tracker(request):
    return HttpResponse('this is a tracker')
def productview(request):
    return HttpResponse('this is the view of your product')
def search(request):
    return HttpResponse('this is your search')
def contact(request):
    return HttpResponse('this is contact page')
def checkout(request):
    return HttpResponse('this is checkout')
def temp(request):
    return render(request, 'shop/temp.html')