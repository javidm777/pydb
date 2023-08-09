from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def company_list(request):
    return HttpResponse('Company list page')


def company_archive(request, year=None, month=None):
    if month is not None:
        return HttpResponse(f'Company Archive for {year} and {month}')
    if year is not None:
        return HttpResponse(f'Company Archive for {year}')
