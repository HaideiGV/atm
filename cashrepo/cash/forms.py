from models import Card
from django import forms

class CardForm(forms.ModelForm):
    number = forms.CharField(
            label=('number'),
            widget=forms.TextInput(attrs={
                'class':'card_mask',
                'id': 'defaultKeypad',
                'placeholder':'**** **** **** ****',
                'maxlength':16}))
    class Meta:
        model = Card
        fields = ['number']

class PinForm(forms.ModelForm):
    pin = forms.CharField(label=('pin'), widget=forms.PasswordInput)
    class Meta:
        model = Card
        fields = ['pin']
