from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def quote(request):
    return render(request, 'quote.html')
