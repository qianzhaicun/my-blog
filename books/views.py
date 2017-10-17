from django.shortcuts import render

# Create your views here.
def search_form(request):
    return render(request, 'books/search_form.html')
    
from django.http import HttpResponse
from books.models import Book
# ...
def search(request):
    error = False
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        if not q:
            error = True
        books = Book.objects.filter(title__icontains=q)
        buttonName = ""
        if "Search" in request.GET: 
            buttonName = "Search"
        else:
            buttonName = "Search2"
        return render(request,'books/search_results.html',
            {'books':books,'query':q,'buttonName':buttonName})
    
    return render(request, 'books/search_form.html',
                      {'error': error})  