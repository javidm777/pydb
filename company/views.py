from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse
from company.models import Company, Product


# Create your views here.
def company_list(request):
    companies = Company.objects.all()
    content = "\n".join([f"name: {company.name}, Country: {company.country}" for company in companies])
    return HttpResponse(content)


def company_details(request, pk):
    queryset = Company.objects.filter(pk=pk)
    if queryset.exists():
        company_det = queryset.first()
        return HttpResponse(f'title: {company_det}')
    return HttpResponse('404')


def product_company(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except:
        return HttpResponse ('404')
    # companies = Company.objects.filter(product=product)
    companies = product.company.all()


    content = "\n".join(
        [f"name: {company.name}, Country: {company.country}" for company in
         companies])
    return HttpResponse(content)
