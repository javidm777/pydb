from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def catalogue_list(request):
    return HttpResponse('Hi catalogue list page')
