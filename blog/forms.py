from django import forms
from .models import Comment, ReplyComment


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
