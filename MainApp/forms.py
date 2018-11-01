from django import forms
from .models import Member_dbdm

class PostForm(forms.ModelForm):
    class Meta:
        model = Member_dbdm
        fields = ('user_id', 'user_pw', 'user_name', 'user_address', 'phone', 'email')