from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def HOME(request):
    print('home')
    return HttpResponse('HOME')