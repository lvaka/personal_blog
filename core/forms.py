"""Core Forms."""
from django import forms


class EmailForm(forms.Form):
    """
    Form for contact page.

        name - char field
        email - char field
        subject - char field
        message - char field
    """

    name = forms.CharField()
    subject = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
