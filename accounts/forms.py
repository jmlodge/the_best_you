from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User


class UserRegistrationForm(UserCreationForm):
    MONTH_ABBREVIATIONS = [
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'June',
        'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'
    ]
    MONTH_CHOICES = list(enumerate(MONTH_ABBREVIATIONS, 1))
    YEAR_CHOICES = [(i, i) for i in range(2015, 2036)]

    credit_card_number = forms.CharField(label='Credit card number')
    cvv = forms.CharField(label='Security code (CVV)')
    expiry_month = forms.ChoiceField(label="Month", choices=MONTH_CHOICES)
    expiry_year = forms.ChoiceField(label="Year", choices=YEAR_CHOICES)
    stripe_id = forms.CharField(widget=forms.HiddenInput, required=False)
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label='Please confirm your Password',
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'stripe_id')

    def clean_password2(self):
        pw1 = self.cleaned_data.get('password1')
        pw2 = self.cleaned_data.get('password2')

        if pw1 and pw2 and pw1 != pw2:
            message = "Your Passwords do not match!"
            raise ValidationError(message)


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
