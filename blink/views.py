from django.shortcuts import render,redirect
from django.http import HttpResponse

import time
import RPi.GPIO as GPIO

# Create your views here.

def main(request):
	return render(request,'blink/blink.html')
def on(request):
	
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(17,GPIO.OUT)
	GPIO.output(17,True)	
	return HttpResponse(status=204)

def off(request):
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(17,GPIO.OUT)
	GPIO.output(17,False)
	return HttpResponse(status=204)
def blnk(request):
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(17,GPIO.OUT)
	while True:		
		GPIO.output(17,GPIO.HIGH)
		time.sleep(1)
		GPIO.output(17,GPIO.LOW)
		time.sleep(1)
	return HttpResponse(status=204)
def stp(request):
	GPIO.cleanup()
	return HttpResponse(status=204)
def test(request):
	return render(request,'blink/test1.html')
