from django import forms
from .models import PhoneModel

class PhoneModelForm(forms.ModelForm):
    class Meta:
        model = PhoneModel
        fields = "__all__"