from django import forms
from allauth.account.adapter import get_adapter
from django.utils.translation import ugettext_lazy as _

class SignupForm(forms.Form):
    first_name = forms.CharField(
            max_length=30, label=_('First Name'), widget=forms.TextInput(attrs={'placeholder': _('First Name')}))
    last_name = forms.CharField(
            max_length=30, label=_('Last Name'), widget=forms.TextInput(attrs={'placeholder': _('Last Name')}))

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        # placeholder for username
        # user.username = ""

        # DAISI Username daisi-xxx
        i = 1
        add_num = 2
        while True:
            try:
                if i < len(user.last_name):
                    user.username = get_adapter().clean_username(
                            'daisi-' + user.first_name[0] + user.last_name[0] + user.last_name[i]).lower()
                else:
                    user.username = get_adapter().clean_username(
                            'daisi-' + user.first_name[0] + user.last_name[:2] + str(add_num)).lower()
            except forms.ValidationError:
                if i < len(user.last_name):
                    i += 1
                else:
                    add_num += 1
            else:
                break

        # Full user name
        # i = 1
        # unique_user = True
        # while True:
        #     try:
        #         if unique_user:
        #             user.username = get_adapter().clean_username(user.first_name[0] + user.last_name).lower()
        #         else:
        #             user.username = get_adapter().clean_username(user.first_name[0] + user.last_name + str(i)).lower()
        #     except forms.ValidationError:
        #         unique_user = False
        #         i += 1
        #         continue
        #     break
        user.save()

