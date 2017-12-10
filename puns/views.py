from django.shortcuts import get_object_or_404, render
from .forms import NameForm
from .models import PunWordEn,PunWordRu
from .pun import *
from django.http import HttpResponseRedirect
import re
from django.http import HttpResponse
from django.views import *


def get_word(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            word = form.cleaned_data['word']
            comb = 'y'if form.cleaned_data['comb'] else 'n'
            handler404 = 'puns.views.error_res'
            try:
                return HttpResponseRedirect( '/res_%s_%s/'% (comb, word) )
            except django.views.defaults.page_not_found():
                return HttpResponseRedirect('/res_n_q/')
    else:
        form = NameForm()

    return render(request, 'puns/index.html', {'form': form})


def error_res(request):
    return HttpResponse("error")

def result_en(request, input_word, comb):
    pattern = r"[1-9]"
    error = False
    combi_pun = comb == 'y'
    if re.search( pattern, input_word ): error = True

    words = list(PunWordEn.objects.all()) if not combi_pun else list(PunWordRu.objects.all())
    new_words = [word.word for word in words]
    output = (pun(new_words, input_word.lower(), combi_pun))
    form = NameForm()
    context = {'input_word': input_word, 'form': form, 'new_words': new_words,
               'input_word_check': input_word.lower(), 'output': output[:6],'error':error,
               'comb': comb,'combi_pun':combi_pun}
    return render(request, 'puns/result.html', context)


def result_ru(request, input_word, comb):
    pattern = r"[1-9]"
    error = False
    combi_pun = comb == 'y'
    if re.search( pattern, input_word ): error = True

    words = list(PunWordRu.objects.all()) if not combi_pun else list(PunWordEn.objects.all())
    new_words = [word.word for word in words]
    output = (pun(new_words, input_word.lower(),combi_pun))
    form = NameForm()
    context = {'input_word': input_word, 'form': form, 'new_words': new_words,
               'input_word_check': input_word.lower(), 'output': output[:6],'error':error,
               'comb':comb,'combi_pun': combi_pun}
    return render(request, 'puns/result.html', context)