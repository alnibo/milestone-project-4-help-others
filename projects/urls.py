from django.conf.urls import url
from .views import all_projects, view_category, add_project, project_details, edit_project, delete_project

urlpatterns = [
    url(r'^add_project/$', add_project, name='add_project'),
    url(r'^$', all_projects, name='projects'),
    url(r'(?P<category>[\w|\W]+)/$', view_category, name='category'),
    url(r"^(?P<pk>\d+)$", project_details, name='project_details'),
    url(r"^edit/(?P<pk>\d+)$", edit_project, name='edit_project'),
    url(r"^delete/(?P<pk>\d+)$", delete_project, name='delete_project'),
]
