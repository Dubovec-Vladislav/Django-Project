from django import forms
from .models import Comment, ReplyComment, User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["name", "comment", ]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "comment": forms.Textarea(attrs={"class": "form-control", "rows": 5}),
        }


class ReplyCommentForm(forms.ModelForm):
    class Meta:
        model = ReplyComment
        fields = ["name", "comment", ]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "comment": forms.Textarea(attrs={"class": "form-control", "rows": 5}),
        }


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='User Name', widget=forms.TextInput(
        attrs={"class": "form-control"}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={"class": "form-control"}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
        attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ("username", "password1", "password2")


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='User Name', widget=forms.TextInput(
        attrs={"class": "form-control"}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={"class": "form-control"}))
