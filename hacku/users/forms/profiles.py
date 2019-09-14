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


    expertise_percentage = forms.CharField(
        max_length=100,
        label='Porcentaje de dominio del tema',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    english_content = forms.BooleanField(
        label='Habilitar contenido en inglés',
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-control'
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


    
