from django import forms
from .models import Article
from django.contrib.auth import authenticate

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'topic', 'youtube_url', 'image']


class AuthenticationForm(forms.Form):
    username = forms.CharField(max_length=254)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        if username and password:
            self.user = authenticate(username=username, password=password)
            if self.user is None:
                raise forms.ValidationError("Incorrect username/password")
        return cleaned_data