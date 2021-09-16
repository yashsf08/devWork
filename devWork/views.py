from quote import search
from django.http import HttpResponse

def index(request):
    return HttpResponse("This is my response")

def about(request):
    return HttpResponse("This is my about page")

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

