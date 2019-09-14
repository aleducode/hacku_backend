"""Profile forms."""

# Django
from django import forms

# Models
from hacku.users.models import (
    PreferenceContentProfile,
)
from hacku.contents.models import (
    ContentArea,
    ContentType
    )


class PreferenceContentProfileForm(forms.ModelForm):
    """Preference Content Profile."""

    # TODO: Change to multiple radio buttons
    content_type = forms.ModelMultipleChoiceField(
        label='Tipo de contenido',
        queryset=ContentType.objects.all(),
        widget=forms.SelectMultiple(
            attrs={
                'class': 'form-control',
            }
        )
    )

    area = forms.ModelMultipleChoiceField(
        label='Área del contenido',
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
        fields = ('content_type',
                  'user',
                  'area',
                  'hour',
                  'english_content',
                  'expertise_percentage'
                  )


    
