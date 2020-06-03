from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    title = forms.CharField()
    description = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "desc-area",
            "rows": 10,
            "cols": 10
        }
    ))
    price = forms.DecimalField()
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if "SHE" in title:
            return title
        else:
            raise forms.ValidationError("This is not a valid title")



class RawProductForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "desc-area",
            "rows": 10,
            "cols": 10
        }
    ))
    price = forms.DecimalField()