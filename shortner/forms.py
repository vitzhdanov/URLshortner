from django import forms
from shortner.models import Url


class UrlForm(forms.Form):
    model = Url
    long_url = forms.CharField(max_length=999, min_length=5)

