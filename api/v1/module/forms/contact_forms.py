from django import forms
from contact.models import Contact

# Creating a ModelForm
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"