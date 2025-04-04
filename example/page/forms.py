from django import forms


class ExampleForm(forms.Form):
    email = forms.CharField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
