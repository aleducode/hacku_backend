"""Profile forms."""

# Django
from django import forms

# Models
from hacku.users.models import (
    PreferenceContentProfile,
    ContentArea,
    ContentType
    )


class PreferenceContentProfileForm(forms.ModelForm):
    """Preference Content Profile."""

    # TODO: Change to multiple radio buttons
    content_type = forms.ModelMultipleChoiceField(
        label='Content Type',
        queryset=ContentType.objects.all(),
        widget=forms.SelectMultiple(
            attrs={
                'class': 'form-control',
            }
        )
    )

    area = forms.ModelMultipleChoiceField(
        label=' Area Content',
        queryset=ContentArea.objects.all(),
        widget=forms.SelectMultiple(
            attrs={
                'class': 'form-control',
            }
        )
    )

    class Meta:
        """Meta class."""
        model = PreferenceContentProfile
        fields = '__all__'


    
