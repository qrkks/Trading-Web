from django import forms
from .models import Inquiry

class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        exclude = ['source_webpage', 'source_ip', 'country_from_ip']
