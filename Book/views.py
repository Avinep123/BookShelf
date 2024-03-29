from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import DetailView
from .models import Book 
from django.contrib.auth import logout 
from django.db.models import Q
from .models import Book
from .forms import BookFilterForm



class BookDetailViewWithSimilarBooks(DetailView):
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        
        similar_books = Book.objects.filter(
            Q(authors=self.object.authors) | Q(categories=self.object.categories)
        ).exclude(id=self.object.id).distinct()[:10]

        context['similar_books'] = similar_books
        return context


def new_arrival(request):
    arrival_books = Book.objects.order_by('-publication_date')[:20]  
    context = {'arrival_books': arrival_books}
    return render(request, 'arrival.html', context)


def featured_books(request):
    featured_books = Book.objects.filter(featured=True)
    return render(request, 'featured_books.html', {'featured_books': featured_books})

def search_books(request):
    search_query = request.GET.get('search_query', '')
    found_books = Book.objects.filter(title__icontains=search_query)

    context = {'found_books': found_books, 'search_query': search_query}
    return render(request, 'search_results.html', context)


def custom_logout(request):
    logout(request)
    return redirect('home') 
  

def browse_books(request):
    books = Book.objects.all()
    form = BookFilterForm(request.GET)

    if form.is_valid():
        author = form.cleaned_data['author']
        category = form.cleaned_data['category']

        if author:
            books = books.filter(authors=author)

        if category:
            books = books.filter(categories=category)

    context = {'books': books, 'form': form}
    return render(request, 'browse.html', context)
