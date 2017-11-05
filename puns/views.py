from django.shortcuts import get_object_or_404, render
from .forms import NameForm
from .models import PunWord
from .pun import *
from django.http import HttpResponseRedirect
import random


def get_word(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            word = form.cleaned_data['word']
            return HttpResponseRedirect('/res_%s/' % word)
    else:
        form = NameForm()

    return render(request, 'puns/index.html', {'form': form})


def result(request, input_word):
    words = list(PunWord.objects.all())
    new_words = [word.word for word in words]
    output = (pun(new_words, input_word.lower()))
    form = NameForm()
    context = {'input_word': input_word, 'form': form, 'new_words': new_words,'output': output[:6]}
    return render(request, 'puns/result.html', context)