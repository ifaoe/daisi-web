from django.conf.urls import url
from daisi_web.options.views import options, switch_database, OptionView

urlpatterns = [
    url(r'^options/$', options, name='options'),
    # url(r'^options/$', OptionView.as_view(), name='options'),
    url(r'^database/(?P<database>.+)/$', switch_database, name='options_database'),
]