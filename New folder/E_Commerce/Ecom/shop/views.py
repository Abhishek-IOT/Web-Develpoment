from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil
# Create your views here.
def index(request):
    product=Product.objects.all()
    print(product)
    n=len(product)
    nslide=n//4+ceil((n/4)-(n//4))
    params = {'no_of_sildes':nslide,'range':range(1,nslide),'product': product}
    return render(request,'Shop/index.html',params)
def about(request):
    return render(request,'Shop/about.html')
def Tracker(request):
    pass
def Search(request):
    pass
def prodview(request):
    pass
def check(request):
    pass
def Contact(request):
    pass