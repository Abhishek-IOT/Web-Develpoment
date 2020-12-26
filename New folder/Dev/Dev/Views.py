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
    upper=request.GET.get('upper','off')
    print(removepunc)
    print(djtext)
    anl=""
    punct="""{}.()\<>"""
    if removepunc=='on':
        for char in djtext:
            if char not in punct:
                anl=anl+char
        params={'purpose':'Remove Punctuations','analyzetext':anl}
        return render(request, "analyze.html", params)
    elif upper == 'on':
        temp=""
        for char1 in djtext:
            temp = temp + char1.upper()
        params = {'purpose': 'To Upper Case', 'analyzetext': temp}
        return render(request,"analyze.html",params)
    # elif removepunc=='on' and upper=='on':
    #     for char in djtext:
    #         if char not in punct:
    #             anl = anl + char
    #     temp = ""
    #     for char1 in anl:
    #         temp = temp + char1.upper()
    #     params={'purpose':"Both the things done",'analyzetext':temp}
    #     return render(request, "analyze.html", params)