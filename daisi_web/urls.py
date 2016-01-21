"""daisi_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin


from daisi_web.exports import views as export_views
from daisi_web.exports.views import ExportRunning, process_export
from daisi_web.plain.views import IndexView
from daisi_web.status_projects.views import ProjectData, session_progress, project_progress
from daisi_web.image_api.views import get_image

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^accounts/', include('daisi_web.accounts.urls')),
    # url(r'^accounts/', include('daisi_web.image_api.urls')),
    url(r'^status/$', ProjectData.as_view(), name='status'),
    url(r'^status/sessions/(?P<session>[0-9]{4}-[0-9]{2}-[0-9]{2}-.+)/$', session_progress, name='session_progress'),
    url(r'^status/projects/(?P<project>[0-9]{4}-[0-9]{2}-[0-9]{2}-.+)/$', project_progress, name='project_progress'),
    url(r'^export/$', export_views.get_export_data, name='exports'),
    url(r'^export/running/(?P<session>[0-9]{4}-[0-9]{2}-[0-9]{2}-.+)/(?P<export>.+)/(?P<filetype>.+)/$',
        ExportRunning.as_view(), name='export_running'),
    url(r'^export/data/(?P<session>[0-9]{4}-[0-9]{2}-[0-9]{2}-.+)/(?P<export>.+)/(?P<filetype>.+)/$',
        process_export, name='export_data'),
    url(r'^api/get_sessions/', export_views.get_sessions, name='get_projects'),
    # url(r'^api/(?P<session>[0-9]{4}-[0-9]{2}-[0-9]{2}-.+)/(?P<cam>.+)/(?P<img>.+)/(?P<utm_x>.+)/(?P<utm_y>.+)/(?P<width>.+)/(?P<height>.+)/$', get_image, name='get_image'),
]