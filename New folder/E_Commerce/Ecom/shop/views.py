from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request,'Shop/index.html')
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