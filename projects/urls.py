from django.conf.urls import url, include
from .views import all_projects, view_category

urlpatterns = [
    url(r'^$', all_projects, name='projects'),
    url(r'(?P<category>\w+)/$', view_category, name='category'),
]
