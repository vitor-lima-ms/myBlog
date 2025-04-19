from django import forms

from publication.models import Publication, Comment

class CreatePublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ['title', 'subtitle', 'category', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'subtitle': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subtitle'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 40}),
        }
        labels = {
            'title': 'Title',
            'subtitle': 'Subtitle',
            'category': 'Category',
            'content': 'Content',
        }

class SearchPublicationForm(forms.Form):
    query = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'by Title'}))
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 40}),
        }
        labels = {
            'content': 'Leave a comment!',
        }