from django import forms

class Login(forms.Form):
    email = forms.CharField(label='Email de acesso', max_length=100, widget=forms.TextInput(attrs={'class':'rounded border px-2'}))
    password = forms.CharField(label='Senha de acesso', max_length=100, widget=forms.PasswordInput(attrs={'class':'rounded border px-2'}))
    