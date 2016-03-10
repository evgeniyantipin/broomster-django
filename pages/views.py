from django.shortcuts import render, redirect
from .forms import QuoteForm


def index(request):
    return render(request, 'index.html')


def quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            redirect('')

    else:
        form = QuoteForm()
        return render(request, 'quote.html', {'form': form})


