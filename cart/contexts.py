from django.shortcuts import get_object_or_404
from projects.models import Project


def cart_contents(request):
    """
    Ensures that the cart contents are available
    on any web page within the web app
    """
    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    project_count = 0

    for id, amount in cart.items():
        project = get_object_or_404(Project, pk=id)
        total += amount
        project_count += 1
        cart_items.append({'id': id, 'amount': amount,
                           'project': project})

    return {'cart_items': cart_items, 'total': total,
            'project_count': project_count}
