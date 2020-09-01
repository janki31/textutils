from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'index.html')

def analyze(request):
    dtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    extraspaceremove = request.POST.get('extraspaceremove', 'off')
    charctercount = request.POST.get('charctercount', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    puncutations='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''


    if removepunc == "on":
        analyzed = ""
        for ch in dtext:
            if ch not in puncutations:
                analyzed=analyzed+ch

        params={'anayzed_text':analyzed}
        dtext=analyzed

    if(fullcaps== "on"):
        analyzed = ""

        for ch in dtext:
            analyzed=analyzed+ch.upper()

        params = {'anayzed_text': analyzed}
        dtext = analyzed

    if(extraspaceremove == "on"):
        analyzed=""

        for index,ch in enumerate(dtext):
            if not(dtext[index] ==" "):
                analyzed=analyzed+ch

        params = {'anayzed_text': analyzed}
        dtext = analyzed

    if(charctercount == "on"):
        analyzed = ""
        count=0
        for ch in dtext:
            if (ch !=' ' and ch.isdigit()!=True):
                count=count+1
                analyzed=analyzed+ch
        analyzed=analyzed+" "+str(count)
        params = {'anayzed_text': analyzed}
        dtext = analyzed

    if (newlineremover == "on"):
        analyzed = ""
        for ch in dtext:
            if ch !='\n' and ch !='\r':
                analyzed = analyzed + ch

        params = {'anayzed_text': analyzed}

    if(removepunc!="on" and fullcaps!="on" and extraspaceremove!="on"
            and newlineremover!="on" and charctercount!="on"):
        return HttpResponse("<h1>Please select any operation...</h1>")

    return render(request, 'analyze.html', params)
def aboutus(request):
    return render(request,'aboutus.html')


