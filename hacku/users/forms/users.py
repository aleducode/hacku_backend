"""User forms."""

# Django
from django import forms

# Models
from hacku.users.models import User
from hacku.utils.models import COUNTRY_CODES


class SignUpForm(forms.Form):
    """Sign up form."""

    first_name = forms.CharField(
        min_length=2,
        max_length=50,
        label='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'First Name'
                }
        )
    )

    last_name = forms.CharField(
        min_length=2,
        max_length=50,
        label='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Last Name'
            }
        )
    )

    username = forms.CharField(
        min_length=4,
        max_length=50,
        label='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Nickname'
            }
        )
    )
    phone_prefix = forms.CharField(
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'placeholder': 'Prefix phone'

            },
            choices=COUNTRY_CODES
        )
    )
    phone_number = forms.CharField(
        min_length=2,
        max_length=50,
        label='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Phone Number'
            }
        )
    )

    email = forms.CharField(
        min_length=6,
        max_length=70,
        label='',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email'
                }
        )
    )

    password = forms.CharField(
        min_length=7,
        max_length=20,
        label='',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password'
                }
        )
    )

    password_confirmation = forms.CharField(
        min_length=7,
        max_length=20,
        label='',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password Confirmation'
                }
        )
    )

    def clean_username(self):
        """Username must be unique."""
        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exists()
        if username_taken:
            raise forms.ValidationError('Username is already in use.')
        return username

    def clean_email(self):
        """Email must be unique."""
        email = self.cleaned_data['email']
        email_taken = User.objects.filter(email=email).exists()
        if email_taken:
            raise forms.ValidationError('Email is already in use.')
        return email

    def clean_phone_number(self):
        """Clean phone number."""
        phone_prefix = self.cleaned_data['phone_prefix']
        phone = self.cleaned_data['phone_number']
        return '{}{}'.format(phone_prefix, phone)

    def clean(self):
        """Verify password confirmation match."""
        data = super().clean()
        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Password do not match')
        return data

    def save(self):
        """Create user data."""
        data = self.cleaned_data
        data.pop('password_confirmation')
        data.pop('phone_prefix')
        user = User.objects.create_user(**data)
        return user
