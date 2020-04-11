from django.shortcuts import render, redirect, reverse


def view_cart(request):
    """A view that renders the cart contents page"""
    return render(request, "cart.html")


def add_to_cart(request, id):
    """
    Add an donation amount in Euro of the
    specified project to the cart
    """
    amount = int(request.POST.get('amount'))

    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + amount
    else:
        cart[id] = cart.get(id, amount)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def adjust_cart(request, id):
    """
    Adjust the donation amount in Euro
    of the specified project
    """
    amount = int(request.POST.get('amount'))
    cart = request.session.get('cart', {})

    if amount > 0:
        cart[id] = amount
    else:
        cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, id):
    """
    Remove a project from the cart.
    """
    cart = request.session.get('cart', {})
    cart.pop(id)
    request.session['cart'] = cart
    return redirect('view_cart')
