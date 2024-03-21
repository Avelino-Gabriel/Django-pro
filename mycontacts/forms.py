from django import forms
from .models import Contact

class AddForm(forms.Form):
    
    class Meta:
        model = Contact
        fields = ('img','name', 'relation', 'phone', 'email',)