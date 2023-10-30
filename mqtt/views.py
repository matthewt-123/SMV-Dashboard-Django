from django.shortcuts import render
from .helper import run
# Create your views here.

topics = ['test', 'test2', 'etc']
run(topics)
def index(request):
    #todo: build dashboard here
    pass

