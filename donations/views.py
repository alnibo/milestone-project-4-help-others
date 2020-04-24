from django.shortcuts import render
from checkout.models import Order
from donations.models import Donations


def donation_history(request):
    """ view that displays the donation history"""

    donator = None
    if request.user.is_authenticated():
        donator = Order.objects.filter(request.user).first()
    
    donations = []
    if donator:
        donations = Donations.objects.filter(donator=user)
    
    return render(request, "donation_history.html", {"donations": donations})
