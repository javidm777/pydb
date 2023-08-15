from django import forms
from django.contrib.auth.forms import AuthenticationForm


class WordpressDownloadForm(forms.Form):
    website = forms.CharField(label='Website URL')
    wp_username = forms.CharField(label='Wordpress Username')
    wp_password = forms.CharField(label='Wordpress Password',
                                  widget=forms.PasswordInput)


class CustomLoginForm(AuthenticationForm):
    # اگر نیاز به اضافه کردن فیلدهای دلخواه دارید، اینجا اضافه کنید.
    pass