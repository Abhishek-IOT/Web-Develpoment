from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    print(request.GET.get('text','default'))
    return render(request,"Insert.html")


def Make(request):
    """Just for making a Pipeline
    //  http://127.0.0.1:8000/Make=This will open a Page with just Make
    """
    return HttpResponse("Make<a href='/'>back</a>")

def analyze(request):
    djtext=request.GET.get('text','default')
    removepunc = request.GET.get('removepunc', 'off')
    print(removepunc)
    print(djtext)
    return render(request,"analyze.html")