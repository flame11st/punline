from django import forms


class NameForm(forms.Form):
    word = forms.CharField(label='', max_length=100)