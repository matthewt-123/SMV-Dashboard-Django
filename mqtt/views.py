from django.shortcuts import render
from .helper import run
import threading

# Create your views here.

#SET TOPICS HERE
topics = ['test', 'test2', 'etc']

#subscribes to above topics and stores them to database
def index(request):
    #todo: build dashboard here
    pass
thread = threading.Thread(target=run, name="MQTT_Subscribe", args=[topics])
thread.start()