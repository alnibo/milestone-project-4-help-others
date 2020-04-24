from django.conf.urls import url
from .views import donation_history

urlpatterns = [
    url(r"^history/", donation_history, name=donation_history),
]