from django import forms


class PhotoForm(forms.Form):
    email = forms.EmailField()