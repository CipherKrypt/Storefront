from django.shortcuts import render
from django.http import HttpResponse

'''Returns a Hello User or name of the user if specified'''
def say_hello(request):
    return render(request, 'base.html', {'name': 'Joe'})

