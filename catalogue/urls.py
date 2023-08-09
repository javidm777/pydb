from django.urls import path
from catalogue.views import catalogue_list

urlpatterns = [
    path('list/', catalogue_list),
]
