# views.py in your cart app

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from Book.models import Book  # Import your Book model

@login_required
def add_to_cart(request, book_id):
    # Handle adding a book to the cart
    try:
        book = Book.objects.get(pk=book_id)

        # Create or update the cart in the session
        cart = request.session.get('cart', {})
        cart_item = cart.get(book_id, {'quantity': 0})
        cart_item['quantity'] += 1
        cart_item['book'] = {
            'id': book.id,
            'title': book.title,
            'price': book.price,
            'thumbnail': book.thumbnail,
            'upload': book.upload.url if book.upload else '',
        }
        cart[book_id] = cart_item

        request.session['cart'] = cart
        return JsonResponse({'success': True})
    except Book.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Book not found'}, status=404)




@login_required
def view_cart(request):
    # Display the user's cart
    cart = request.session.get('cart', {})
    cart_items = cart.values()

    total_price = sum(item['quantity'] * item['book']['price'] for item in cart_items)
    
    for item in cart_items:
        item['subtotal'] = item['quantity'] * item['book']['price']

    return render(request, 'addtocart.html', {'cart_items': cart_items, 'total_price': total_price})

@login_required
def remove_from_cart(request, book_id):
    cart = request.session.get('cart', {})
    if str(book_id) in cart:
        del cart[str(book_id)]
        request.session['cart'] = cart

    return redirect('view_cart')

@login_required
def update_quantity(request, book_id):
    cart = request.session.get('cart', {})
    if str(book_id) in cart:
        quantity = int(request.POST.get('quantity', 1))
        cart[str(book_id)]['quantity'] = quantity
        request.session['cart'] = cart

    return JsonResponse({'success': True})
