from django.shortcuts import render
from django.http import HttpResponse
from shop.models import Product
from math import ceil
# Create your views here.

def index(request):
    # products= Product.objects.all()
    allprods = []
    catprods = Product.objects.values('category','id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category = cat)
        n= len(prod)
        nSlides= n//4 + ceil((n/4)-(n//4))
        allprods.append([prod,range(1,nSlides),nSlides])
    # allProds=[[products, range(1, len(products)), nSlides],[products, range(1, len(products)), nSlides]]
    params={'allProds':allprods}
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