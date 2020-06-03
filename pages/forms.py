from django import forms

from .models import Contact

class ContactForm(forms.ModelForm):
    name = forms.CharField(label="", widget=forms.TextInput(
        attrs={
            "id":"name",
            "class": "form-input",
            "autocomplete":"off",
            "placeholder":"Name",
            "size": "40"
        }
    ))
    email= forms.EmailField(label="", widget=forms.EmailInput(
        attrs={
            "id":"email",
            "class":"form-input",
            "autocomplete":"off",
            "placeholder":"Email",
            "size": "40"
        }
    ))
    message = forms.CharField(label="", widget=forms.Textarea(
        attrs={
            "id": "msg-area",
            "class":"form-input",
            'autocomplete':'off',
            "placeholder":"Message",
            "rows": "5",
            "cols": "42"
        }
    ))
    class Meta:
        model = Contact
        fields = [
            'name',
            'email',
            'message'
        ]