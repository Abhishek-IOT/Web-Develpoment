from django.http import HttpResponse
def index(request):
    return HttpResponse('''"<h1>My name is Abhishek</h1><a href="https://www.youtube.com/"> Code With Abhishek </a>''')

def Make(request):
    """Just for making a Pipeline
    //  http://127.0.0.1:8000/Make=This will open a Page with just Make
    """
    return HttpResponse("Make<a href='/'>back</a>")
