from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def display(request):
    s1='<h1>Hello World</h1>'
    s2='<h1>Good Evening</h1>'
    s3='<h1>ITVEDANT</h1>'
    
    return HttpResponse(s1+s2+s3)