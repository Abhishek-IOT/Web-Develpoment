from django.http import HttpResponse
def index(request):
    return HttpResponse('''"<h1>My name is Abhishek</h1><a href="https://www.youtube.com/"> Code With Abhishek </a>''')

def Make(request):
    return HttpResponse("Make")
