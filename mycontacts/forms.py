from django import forms
from .models import Contact

class AddForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = ('foto', 'name', 'relation', 'phone', 'email',)
        