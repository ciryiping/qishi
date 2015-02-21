from django import forms
from mysite.blog.models import BlogPost
from bootstrap_markdown.widgets import MarkdownEditor

# Create your models here.

class BlogPostForm(forms.ModelForm):
    FORM_NAME = "AddPostForm"
    body = forms.CharField(widget=MarkdownEditor(
        attrs={'id': 'body'}))
    class Meta:
        model = BlogPost
 
