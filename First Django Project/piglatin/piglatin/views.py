from django.http import HttpResponse
from django.shortcuts import render

def Hello(request):
    return render(request, 'home.html')

def translate(request):
    return HttpResponse("You are on the translate page")