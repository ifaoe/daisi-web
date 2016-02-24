from django.conf.urls import url
from daisi_web.status_projects.views import ProjectData, session_progress, project_progress

urlpatterns = [
    url(r'^status/$', ProjectData.as_view(), name='status'),
    url(r'^status/sessions/(?P<session>[0-9]{4}-[0-9]{2}-[0-9]{2}-.+)/$', session_progress, name='session_progress'),
    url(r'^status/projects/(?P<project>[0-9]{4}-[0-9]{2}-[0-9]{2}-.+)/$', project_progress, name='project_progress'),
]