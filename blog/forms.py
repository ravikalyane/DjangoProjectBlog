from django import forms
from .models import Comment, Message


class CommentForm(forms.ModelForm):
    name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    message = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': 'Message'}))

    class Meta:
        model = Comment
        exclude = ['post', 'approved_comment']
        fields = '__all__'


class MessageForm(forms.ModelForm):
    name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    message = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': 'Message'}))

    class Meta:
        model = Message
        fields = '__all__'
