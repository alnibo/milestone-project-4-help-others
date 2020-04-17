from django.conf.urls import url
from .views import all_projects, view_category, add_project

urlpatterns = [
    url(r'^$', all_projects, name='projects'),
    url(r'(?P<category>\w+)/$', view_category, name='category'),
    url(r'^add_project/$', add_project, name='add_project'),
]
