from django.forms import forms

from account.models import Profile


class ProfileForm(forms.Form):
    class Meta:
        model = Profile
        fields = ['user.username','name','surname', 'birth_date', 'bio']

