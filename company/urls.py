from django.urls import path, re_path
from company.views import company_list, company_details, product_company

urlpatterns = [
    path('list/', company_list),
    path('detail/<int:pk>/', company_details),
    path('archive/product/<int:pk>/', product_company)

]