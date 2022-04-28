from django import forms
from calc.models import OldTractor


class OldTracktorForm(forms.ModelForm):

    class Meta:
        model = OldTractor
        fields = '__all__'