from django import forms
from .models import Organization


class CreateOrUpdateOrganization(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['ORG_name', 'ORG_brief']
