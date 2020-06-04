from django.shortcuts import *
from django.http import *
from django.views.decorators.csrf import csrf_exempt
import time, sys
import requests
import time, sys
import requests
#from ubidots import ApiClient
#import Adafruit_DHT
#sensor = Adafruit_DHT.DHT11
#import RPi.GPIO as GPIO
from time import sleep
#GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(17, GPIO.OUT)  # led1
#GPIO.setup(27, GPIO.OUT)  # led2
#GPIO.setup(22, GPIO.OUT)  # led3
#GPIO.setup(18, GPIO.OUT)  # led4
#pin = 23  # dht11 sensor
#from time import sleep
@csrf_exempt
def switch1(request):
    data =int( request.GET['d'])
    print(data)
    return HttpResponse('success')
#    if data.content == 1:
 #       GPIO.output(17, 1)
  #  elif data.content == 2:
   #     GPIO.output(17, 0)
    #elif data.content == 3:
     #   GPIO.output(27, 0)
#    elif data.content == 4:
 #       GPIO.output(27, 0)
  #  elif data.content == 5:
   #     GPIO.output(22, 1)
    #elif data.content == 6:
     #   GPIO.output(22, 0)


def website(request):
    return render(request,'index.html')
def temperature(request):
      #      humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
       #     print (temperature)
        #    return HttpResponse(temperature)
   b=1

def humidity(request):
  #  humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
   # print(humidity)
    #return HttpResponse(humidity)
  c=1

