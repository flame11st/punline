import os,sys,codecs
sys.path.append(os.path.join(os.path.abspath('..'), 'www'))
from django.core.management import setup_environ
setup_environ(settings)
import django.models

from puns.models import PunWordEn,PunWordRu
file = open('wordsEn.txt','r')
line = file.readlines()
for l in line:
	PunWordEn(word = l).save()
file.close()