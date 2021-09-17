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
    # Initializing Variables
    djtext = request.POST.get('myarea', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcounter = request.POST.get('charcounter', 'off')
    params = dict()
    params['purpose'] = ""
    if removepunc == 'on':
        punctuations = """!"#$%&'()*+,-./:;?@[\]^_`{|}~"""
        analyzed_text = "" 
        for word in djtext:
            if word not in punctuations:
                analyzed_text += word
        djtext = analyzed_text 
        params['purpose'] = "* Removing Punctuations *"

    if fullcaps == 'on':
        djtext = djtext.upper()
        params['purpose'] += "* UpperCase *"

    if newlineremover == 'on':
        analyzed_text = ""
        for word in djtext:
            if word != "\r" and word != "\n":
                analyzed_text += word

        djtext = analyzed_text
        params['purpose'] += "* New Line Remove *"

    if extraspaceremover == 'on':
        analyzed_text = ""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index + 1] == " ":
                pass
            else: 
                analyzed_text += char

        djtext = analyzed_text
        params['purpose'] += "* Extra Space Remove *"
        
    if charcounter == 'on':
        params['counter'] = len(djtext)
        params['purpose'] += "* Character Count *"

    params['analyzed_text'] = djtext
    return render(request, 'analyze.html', params)