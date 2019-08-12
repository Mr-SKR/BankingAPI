from django import forms


class SignUpForm(forms.Form):
    user_id = forms.CharField(label='User ID')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
