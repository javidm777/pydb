from django.urls import path
from . import views

urlpatterns = [
    path('salam', views.form_view),
    # دیگر مسیرها را اضافه کنید
]
