from django.conf.urls import url
from daisi_web.image_api.views import get_image

urlpatterns = [
# url(r'^api/get_sessions/', export_views.get_sessions, name='get_projects'),
    url(r'^api/(?P<session>[0-9]{4}-[0-9]{2}-[0-9]{2}-.+)/(?P<cam>.+)/(?P<img>.+)/(?P<utm_x>.+)/(?P<utm_y>.+)/(?P<width>.+)/(?P<height>.+)/$', get_image, name='get_image'),
]