from django import forms
from nutrition.models import Nutrients


class NutrientsForm(forms.ModelForm):

    class Meta:
        model = Nutrients
        fields = ('name', 'energy_kJ', 'energy_kcal', 'protein', 'carbs', 'fat', 'sugar', 'fiber', 'amount', 'meal')

