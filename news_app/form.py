from django import forms
from news_app.models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'text'] 
        widgets = {
            'name': forms.TextInput(attrs={'class': 'contact__name', 'placeholder': 'Name'}),
            'email': forms.EmailInput(attrs={'class': 'contact__email', 'placeholder': 'Email'}),
            'subject': forms.TextInput(attrs={'class': 'contact__subject', 'placeholder': 'Subject'}),
            'text': forms.Textarea(attrs={'class': 'contact__text', 'placeholder': 'Type your message'}),
        }