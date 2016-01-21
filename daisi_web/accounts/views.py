from django.shortcuts import render
from allauth.account.views import LoginView, LogoutView, SignupView


# Create your views here.


class LoginDropDownView(LoginView):
    template_name = "account/dropdown/login.html"

login_dropdown = LoginDropDownView.as_view()


class LogoutDropDownView(LogoutView):
    template_name = "account/dropdown/logout.html"

logout_dropdown = LogoutDropDownView.as_view()

# class SignUpFullView(SignupView):
#     form_class = SignupFullForm