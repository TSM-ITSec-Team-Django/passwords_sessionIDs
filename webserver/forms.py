from django import forms


class Login(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password')


class Register(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password')
