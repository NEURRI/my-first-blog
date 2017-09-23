from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    # forms안에 ModelForm을 받아오겠다는 표현. 상속 개념
    class Meta:
        model = Post
        fields = ('title', 'text',)
