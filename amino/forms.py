from django import forms
from .models import Input
from .models import Amino

class InputForm(forms.ModelForm):
    class Meta:
        model = Input
        fields = [
            'input_string'
        ]


class DataForm(forms.ModelForm):
    class Meta:
        model = Amino
        fields = [
            'amino_name',
            'three_letter_symbol',
        ]