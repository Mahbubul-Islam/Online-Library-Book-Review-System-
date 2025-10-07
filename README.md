# 📚 Online Library - Book Review System

[![Django](https://img.shields.io/badge/Django-5.2.1-green.svg)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-4.0-38B2AC.svg)](https://tailwindcss.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A modern, responsive Django web application for browsing books, viewing details, and writing reviews. Built with Django and styled with Tailwind CSS.

## 📋 Table of Contents

- [Features](#-features)
- [Demo](#-demo)
- [Technology Stack](#-technology-stack)
- [Getting Started](#-getting-started)
- [Usage Guide](#-usage-guide)
- [Project Structure](#️-project-structure)
- [Database Models](#-database-models)
- [Key Features Highlights](#-key-features-highlights)
- [Design Features](#-design-features)
- [Security Note](#-security-note)
- [Contributing](#-contributing)
- [Support](#️-support)
- [Future Enhancements](#-future-enhancements)
- [License](#-license)

## ✨ Features

### 1. User Authentication

- ✅ User Registration (sign up for a new account)
- ✅ Login / Logout functionality
- ✅ Only registered users can write reviews

### 2. Book Management (Admin Only)

- ✅ Admin can add new books via Django Admin Panel
- ✅ Book information includes:
  - Title
  - Author
  - Category
  - Cover Image (optional)
  - Description

### 3. Book Browsing (All Users)

- ✅ Browse and view a list of all books
- ✅ Each book has a Details Page showing:
  - Title, Author, Category
  - Cover image
  - Description
  - Average rating
  - All reviews

### 4. Reviews (User Feature)

- ✅ Registered users can comment/review books
- ✅ Users can rate books (1-5 stars)
- ✅ All reviews are visible under the respective book
- ✅ Average rating displayed on book cards and detail pages

### 5. Extra Features

- ✅ **Search**: Search books by title or author
- ✅ **Category Filter**: Filter books by category
- ✅ **Pagination**: 6 books per page in 3x2 grid layout
- ✅ **Responsive Design**: Mobile-friendly interface with Tailwind CSS
- ✅ **Star Ratings**: Visual star ratings for reviews
- ✅ **Optimized Book Cover Display**: Book covers shown with proper aspect ratio

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git (for cloning the repository)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Mahbubul-Islam/Online-Library-Book-Review-System-.git
   cd Online-Library-Book-Review-System-
   ```

2. **Create a virtual environment (recommended):**

   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install required packages:**

   ```bash
   pip install django pillow crispy-tailwind
   ```

4. **Apply database migrations:**

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (Admin account):**

   ```bash
   python manage.py createsuperuser
   ```

   Follow the prompts to create an admin account.

6. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

7. **Access the application:**

   - **Main Site:** <http://127.0.0.1:8000/>
   - **Admin Panel:** <http://127.0.0.1:8000/admin/>

## 📖 Usage Guide

### For Admin Users

1. **Login to Admin Panel:**

   - Go to <http://127.0.0.1:8000/admin/>
   - Use your superuser credentials

2. **Add Categories:**

   - Click on "Categories" → "Add Category"
   - Enter category name (e.g., Fiction, Non-Fiction, Science, etc.)
   - Click "Save"

3. **Add Books:**
   - Click on "Books" → "Add Book"
   - Fill in the book details:
     - Title
     - Author
     - Select a Category
     - Upload Cover Image (optional)
     - Write Description
   - Click "Save"

### For Regular Users

1. **Register an Account:**

   - Click "Register" in the navigation
   - Fill in username, email, and password
   - Click "Create Account"

2. **Browse Books:**

   - View books in a beautiful 3x2 grid layout (6 books per page)
   - Navigate through pages using pagination controls
   - Use the search box to find books by title or author
   - Filter books by category using the dropdown
   - Clear filters to view all books

3. **View Book Details:**

   - Click on any book card to view full details
   - See the book's description, author, category, and ratings
   - Read existing reviews

4. **Write Reviews:**
   - Login to your account
   - Navigate to a book's detail page
   - Select a rating (1-5 stars)
   - Write your review
   - Click "Submit Review"

## 🗂️ Project Structure

```plaintext
online_library/
├── books/                      # Main app
│   ├── migrations/            # Database migrations
│   ├── templates/             # HTML templates
│   │   ├── base.html         # Base template with navbar
│   │   ├── books/
│   │   │   ├── home.html     # Book listing page
│   │   │   └── book_detail.html  # Book detail page
│   │   └── auth/
│   │       ├── login.html    # Login page
│   │       └── register.html # Registration page
│   ├── models.py              # Database models
│   ├── views.py               # View functions
│   ├── forms.py               # Form classes
│   ├── urls.py                # App URL patterns
│   └── admin.py               # Admin configuration
├── online_library/            # Project settings
│   ├── settings.py           # Django settings
│   ├── urls.py               # Main URL configuration
│   └── wsgi.py
├── static/                    # Static files (CSS, JS, images)
├── media/                     # User-uploaded files (book covers)
├── db.sqlite3                # SQLite database
└── manage.py                 # Django management script
```

## 🎨 Technology Stack

- **Backend**: Django 5.2.1
- **Database**: SQLite
- **Frontend**: Tailwind CSS 4 (via CDN)
- **Icons**: Font Awesome 6.4.0
- **Image Handling**: Pillow
- **Forms**: django-crispy-forms with crispy-tailwind
- **Authentication**: Django built-in authentication system

## � Database Models

### Category

```python
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
```

**Fields:**

- `name`: Category name (unique)

### Book

```python
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    cover_image = models.ImageField(upload_to='Books/covers/', blank=True, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
```

**Fields:**

- `title`: Book title
- `author`: Author name
- `category`: Foreign key to Category
- `cover_image`: Optional image upload
- `description`: Text description
- `created_at`: Auto-generated timestamp

### Review

```python
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
```

**Fields:**

- `user`: Foreign key to User
- `book`: Foreign key to Book
- `comment`: Review text
- `rating`: Integer (1-5 stars)
- `created_at`: Auto-generated timestamp

## 🔒 Security Note

⚠️ **Important**: This project uses Django's default `SECRET_KEY` which is visible in the code. For production deployment:

1. Generate a new secret key
2. Store it in environment variables
3. Never commit it to version control
4. Set `DEBUG = False`
5. Configure `ALLOWED_HOSTS` properly

## 📄 License

This project is created for educational purposes as part of a Django full-stack course.

## ✨ Key Features Highlights

### Pagination System

- **Grid Layout**: 3 columns × 2 rows = 6 books per page
- **Responsive**: Adjusts to 2 columns on tablets, 1 column on mobile
- **Navigation**: Previous/Next buttons with page numbers
- **Page Info**: Shows current page and total pages

### Book Display

- **Optimized Cover Images**: Using `object-contain` to show full cover without cropping
- **Hover Effects**: Cards lift on hover with smooth transitions
- **Fallback Design**: Beautiful gradient placeholder for books without covers
- **Star Rating Display**: Visual representation of average ratings

### User Experience

- **Messages System**: Success/error notifications for user actions
- **Mobile Menu**: Responsive navigation for mobile devices
- **Clean UI**: Modern, professional design with consistent color scheme
- **Fast Search**: Real-time search and filtering capabilities

## 🎨 Design Features

### Color Scheme

- **Primary Dark**: #1b3c53
- **Primary**: #234c6a
- **Secondary**: #456882
- **Accent**: #d2c1b6
- **Background**: #f8f5f2

### Layout

- **Desktop**: 3-column grid for books
- **Tablet**: 2-column grid
- **Mobile**: 1-column stack
- **Fixed Height**: 320px (h-80) for book covers

## 🙋‍♂️ Support

If you encounter any issues:

1. Make sure all migrations are applied: `python manage.py migrate`
2. Check if the server is running: `python manage.py runserver`
3. Verify all dependencies are installed
4. Check the terminal for error messages
5. Clear browser cache if styles don't update
6. For login issues, ensure you've logged out from admin panel

**Found a bug?** [Open an issue](https://github.com/Mahbubul-Islam/Online-Library-Book-Review-System-/issues)

## 🚀 Future Enhancements

Potential features for future development:

- [ ] User profiles with reading history
- [ ] Book wishlist functionality
- [ ] Advanced search with multiple filters
- [ ] Book recommendations based on ratings
- [ ] Export reviews to PDF
- [ ] Social sharing of reviews
- [ ] Email notifications for new books
- [ ] REST API for mobile app integration
- [ ] Multiple language support

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Mahbubul Islam**

- GitHub: [@Mahbubul-Islam](https://github.com/Mahbubul-Islam)
- Repository: [Online-Library-Book-Review-System-](https://github.com/Mahbubul-Islam/Online-Library-Book-Review-System-)

## 🙏 Acknowledgments

- Built as part of a Django Full Stack Course
- Styled with [Tailwind CSS](https://tailwindcss.com/)
- Icons from [Font Awesome](https://fontawesome.com/)
- Powered by [Django](https://www.djangoproject.com/)

---

<div align="center">

**⭐ Star this repository if you find it helpful! ⭐**

Made with ❤️ using Django and Tailwind CSS

</div>
