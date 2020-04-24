from django.conf.urls import url
from .views import index, about_us

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r"^about_us/", about_us, name="about_us")
]
