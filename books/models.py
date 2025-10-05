from django.db import models
import os
from django.contrib.auth.models import User
# Create your models here.

# save files according to instance name
def book_cover_directory_name(instance, filename):
    return os.path.join('Books/media', instance.title, filename)

# 1. Category
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
    
# 2. Books
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='books') # one to many. One category can have many books
    cover_image = models.ImageField(upload_to=book_cover_directory_name, blank=True, null=True) 
    description = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True) 

    class Meta:
        ordering = ['title']

    def __str__(self):
        return f"{self.title} by {self.author}"

    def average_rating(self):
        reviews = self.reviews.all()
        if not reviews.exists():
            return 0
        return round(sum([review.rating for review in reviews]) / reviews.count(), 1)

# 3. Review
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    comment = models.TextField()
    rating = models.PositiveIntegerField(default=0)  # rating from 1 to 5 (optional)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Review by {self.user.username} on {self.book.title}"
