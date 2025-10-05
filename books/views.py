from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
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

# Book details
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    reviews = book.reviews.all()
    form = None
    
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.user = request.user
                review.book = book
                review.save()
                messages.success(request, 'Your review has been posted!')
                return redirect('book_detail', pk=book.pk)
        else:
            form = ReviewForm()

    context = {
        'book': book,
        'reviews': reviews,
        'form': form,
        'average_rating': book.average_rating(),
    }
    return render(request, 'books/book_detail.html', context)

# User registrations
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto-login after registration
            messages.success(request, 'Registration successful!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserRegistrationForm()
    return render(request, 'auth/register.html', {'form': form})

# User login

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()  
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'auth/login.html', {'form': form})

# User logout
@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully!')
    return redirect('home')
        
