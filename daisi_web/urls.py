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
from daisi_web.status_projects.views import ProjectData, SessionProgress, ProjectProgress
from daisi_web.exports import views as ExportViews
from daisi_web.plain.views import IndexView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^status/$', ProjectData.as_view(), name='status'),
    url(r'^status/sessions/(?P<session>[0-9]{4}-[0-9]{2}-[0-9]{2}-.+)/$', SessionProgress, name='session_progress'),
    url(r'^status/projects/(?P<project>[0-9]{4}-[0-9]{2}-[0-9]{2}-.+)/$', ProjectProgress, name='project_progress'),
    url(r'^export/$', ExportViews.ExportView.as_view(), name='exports'),
    url(r'^api/get_sessions/', ExportViews.get_sessions, name='get_projects'),
]
