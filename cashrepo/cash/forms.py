from models import Card
from django import forms

class CardForm(forms.ModelForm):
    number = forms.CharField(
            label=('number'),
            widget=forms.TextInput(attrs={
                # 'class':'jqxmaskedinput',
                'id': 'defaultKeypad',
                'placeholder':'**** **** **** ****',
                'maxlength':16,
                'style':'width:250px; height:40px; font-size:20px;'}))
    class Meta:
        model = Card
        fields = ['number']

class PinForm(forms.ModelForm):
    pin = forms.CharField(label=('pin'), widget=forms.PasswordInput)
    class Meta:
        model = Card
        fields = ['pin']
