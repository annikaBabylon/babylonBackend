from django import forms
from .models import Discount

class DiscountForm(forms.ModelForm):
    class Meta:
        model = Discount
        fields = [
            'title',
            'content',
            'percentage',
            'cover_image'
        ]