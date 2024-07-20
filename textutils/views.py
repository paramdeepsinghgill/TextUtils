# I have created this file - Paramdeep
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')
    #Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations','analyzed_text':analyzed}
        djtext = analyzed
    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'Changed to Uppercase','analyzed_text':analyzed}
        djtext = analyzed
        #Analyze the text
        # return render(request, 'analyze.html', params)
    if(extraspaceremover=="on"):
        analyzed = ""
        for index,char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose':'Removed NewLines','analyzed_text':analyzed}
        djtext = analyzed
        #Analyze the text
        # return render(request, 'analyze.html', params)
    if(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose':'Removed NewLines','analyzed_text':analyzed}
        djtext = analyzed
        #Analyze the text
        # return render(request, 'analyze.html', params)
    if(charcount=="on"):
        i = 0
        for char in djtext:
            if not(char == " "):
                i+=1
        i = str(i)
        analyzed = "The number of characters in the string is: " + i + "."
        params = {'purpose':'Counted characters','analyzed_text':analyzed}
        #Analyze the text
    if (removepunc!="on" and newlineremover!="on" and extraspaceremover!="on" and fullcaps!="on" and charcount!="on"):
        return HttpResponse("please select any operation and try again")
    return render(request, 'analyze.html', params)
def aboutus(request):
    return render(request,'about us.html')
def contactus(request):
    return render(request,'contact us.html')
# def newlineremove(request):
#     return HttpResponse("newline remove first")
# def capfirst(request):
#     return HttpResponse("capitalize first")
# def spaceremove(request):
#     return HttpResponse("space remover <a href='/'>back</a>")
# def charcount(request):
#     return HttpResponse("charcount ")