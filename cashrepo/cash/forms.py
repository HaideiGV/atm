from models import Card
from django import forms

class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['number']

class PinForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['pin']