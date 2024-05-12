from django import forms
from .models import CollaborateRequest


class CollaborateForm(forms.ModelForm):
    """
    Form for users to request collaboration
    """
    class Meta:
        model = CollaborateRequest
        fields = ('name', 'email', 'message')
