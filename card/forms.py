from .models import Profile
from django import forms


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput)
    rep_password = forms.CharField(label='repeat password', widget=forms.PasswordInput)

    class Meta:
        model = Profile
        fields = ['username', 'first_name', 'last_name', 'email', 'sex']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['rep_password']:
            raise forms.ValidationError('Passwords mismatch')
        return cd['rep_password']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

