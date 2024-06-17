
from django import forms # type: ignore
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'product_id', 'title', 'user_id', 'first_name', 'last_name',
            'customer_need', 'state', 'city', 'email', 'phone', 'message'
        ]
