from quote import search
from django.http import HttpResponse

def index(request):
    return HttpResponse("Home")

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

def removepunc(request):
    return HttpResponse("Remove Punc")
    
def capfirst(request):
    return HttpResponse("Cap First")

def newlineremove(request):
    return HttpResponse("New Line Remove")

def spaceremove(request):
    return HttpResponse("Space Remove")

def charcount(request):
    return HttpResponse("Character Count")