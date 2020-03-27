from django import forms
from FineSystemapp.models import Apply_Fine
from FineSystemapp.models import RULEs


class New_3FineApply(forms.ModelForm):
    class Meta():
        model = Apply_Fine
        fields = '__all__'


class New_1Rules_Add(forms.ModelForm):
    class Meta():
        model = RULEs
        fields = '__all__'

