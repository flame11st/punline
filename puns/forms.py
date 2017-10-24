from django import forms


class NameForm(forms.Form):
    word = forms.CharField(label='Enter the word', max_length=100)