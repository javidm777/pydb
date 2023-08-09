from django.urls import path, re_path
from company.views import company_list, company_archive

urlpatterns = [
    path('list/', company_list),
    re_path('archive/(?P<year>[0-9]{4})', company_archive),
    re_path('archive/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/', company_archive),



]