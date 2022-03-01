from django.shortcuts import render
from django.http import HttpResponse

# Create your views herdef hi(request):
def hi(request):
    return render(request,'demoapp/hi.html')
