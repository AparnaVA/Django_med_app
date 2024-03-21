from django import forms
from .models import medicine
class ProductForm(forms.ModelForm):
    class Meta:
        model = medicine
        fields = ['id','name','description','price']
