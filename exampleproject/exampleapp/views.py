from django.shortcuts import render

from django.http import HttpResponse

def index(request):
  return HttpResponse("Hi! This is the main view of my CI/CD example app!")
