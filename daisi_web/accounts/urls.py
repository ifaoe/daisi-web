from django.conf.urls import url
from daisi_web.accounts import views

urlpatterns = [
    url(r"^dropdown/login/$", views.login_dropdown, name="account_dropdown_login"),
    url(r"^dropdown/logout/$", views.logout_dropdown, name="account_dropdown_logout"),
    # url(r"^admin/$", views.login_dropdown, name="account_admin"),
    # url(r"^admin/?P<user>.+/$", views.login_dropdown, name="account_admin_user"),
]