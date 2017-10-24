from django.shortcuts import get_object_or_404, render
from .forms import NameForm
from .models import PunWord
from django.http import HttpResponseRedirect


def get_word(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # word = form.cleaned_data['word']
            return HttpResponseRedirect('/puns/result/')
    else:
        form = NameForm()

    return render(request, 'puns/index.html', {'form': form})


# def result(request):
#     context = {'word': word}
#     return render(request, 'puns/result.html', context)