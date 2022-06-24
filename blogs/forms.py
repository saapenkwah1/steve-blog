from django import forms
from .models import BlogPost

class NewBlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title','text',]
        label = {'title': '', 'text':''}
        widget = {'text': forms.Textarea(attrs={'cols': 100})}

# class BlogPostForm(forms.ModelForm):
#     class Meta:
#         model = BlogPost
#         fields = ['text']
#         label = {'text': ''}
#         widget = {'text': forms.Textarea(attrs= {'cols': 100 })}


    
