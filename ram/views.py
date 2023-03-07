from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def mejari(request):
    return HttpResponse('<marquee>hello</marquee>')