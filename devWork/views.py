from quote import search
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # Solution 1
    # return render(request, 'index.html')

    # Solution 2
    mydictionary = {'name': 'Yash Kumar Sonune', 'git': 'https://github.com/yashsf08'}
    return render(request, 'index.html', mydictionary)

def quote(request):
    return HttpResponse("<h1>" + search('family', limit=1)[0]['quote'] + "</h1>")

def navigator(request):
    return HttpResponse("""
       <h1><a href="http://www.youtube.com/watch">Youtube</a></h1> 
       <h1><a href="https://www.facebook.com/">Facebook</a></h1> 
       <h1><a href="https://www.instagram.com/">Instagram</a></h1> 
       <h1><a href="https://www.reddit.com/">Reddit</a></h1> 
       <h1><a href="https://www.quora.com">Quora</a></h1> 
    """)

def analyze(request):
    djtext = request.GET.get('myarea', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    analyzed_text = "" 
    if removepunc != 'off':
        punctuations = """!"#$%&'()*+,-./:;?@[\]^_`{|}~"""
        for word in djtext:
            if word not in punctuations:
                analyzed_text += word
        
    params = {
        'purpose': "Removing Punctuations",
        'analyzed_text': analyzed_text,
    }

    return render(request, 'analyze.html', params)
    
def capfirst(request):
    return HttpResponse("Cap First")

def newlineremove(request):
    return HttpResponse("New Line Remove")

def spaceremove(request):
    return HttpResponse("Space Remove")

def charcount(request):
    return HttpResponse("Character Count")