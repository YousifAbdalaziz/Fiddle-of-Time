from django.shortcuts import render, HttpResponse
from .models import Book
from django.db.models import Q

# Create your views here.
def index(request):
   books = Book.objects.all
   return render(request, 'base.html', {'books': books})

def search(request):
    
    s = request.GET.get('search')
    books = Book.objects.filter(Q(title__startswith = s))
    return render(request, 'result.html', {'books': books})