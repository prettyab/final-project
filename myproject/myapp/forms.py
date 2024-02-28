from .models import SalaryPrediction
from django import forms
class SalaryPredictionForm(forms.ModelForm):
    class Meta:
        model = SalaryPrediction
        fields = ['YearsExperience']