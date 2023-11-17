from django import forms
from .models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["name", "address"]

    def clean_name(self):
        data = self.cleaned_data["name"]
        if len(data) < 3 or len(data) > 32:
            raise forms.ValidationError("Name length should be between 3 and 32")
        return data

    def clean_address(self):
        data = self.cleaned_data["address"]
        if len(data) < 3 or len(data) > 100:
            raise forms.ValidationError("Address length should be between 3 and 100")
        return data
