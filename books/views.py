from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Book, Category, Review
from .forms import UserRegistrationForm, UserLoginForm, ReviewForm

# Create your views here.
# Book list

def home(request):
    query = request.GET.get('q','')
    category_id = request.GET.get('category')
    
    books = Book.objects.all()
    
    # Search by title or author
    if query:
        books = books.filter(Q(title__icontains=query)|Q(author__icontains=query))
    
    # Filter by category
    if category_id:
        if str(category_id).isdigit():
            books = books.filter(category__id=category_id)
        else:
            books = books.filter(category__name__iexact=category_id)
    
    categories = Category.objects.all()

    context = {
        'books': books,
        'categories': categories,
        'query': query,
        'selected_category': category_id,
    }
    return render(request, 'books/home.html', context)


