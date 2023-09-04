# Sumit has created this file - views.py
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    # get the text from textarea
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    # Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'Remove Punctuations', 'analyzed_text': analyzed}

        djtext = analyzed


    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'All letters in uppercase', 'analyzed_text': analyzed}

        djtext = analyzed

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char

        params = {'purpose': 'New Line remover', 'analyzed_text': analyzed}

        djtext = analyzed

    if extraspaceremover == "on":
        analyzed = ""
        for i, char in enumerate(djtext):
            if not(djtext[i] == " " and djtext[i+1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Extra Space remover', 'analyzed_text': analyzed}

        djtext = analyzed

    if charcount == "on":
        analyzed = ""
        count = 0
        for char in djtext:
            count = count + 1
            analyzed = str(count)

        params = {'purpose': 'Count of total character ', 'analyzed_text': analyzed}

    if removepunc != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover != "on" and charcount != "on":
        return HttpResponse("Error")

    return render(request, 'analyze.html', params)




# def capfirst(request):
#     return HttpResponse("Capitalize First")
#
#
# def spaceremove(request):
#     return HttpResponse("Space Remove")
#
#
# def charcount(request):
#     return HttpResponse("Char Count")




