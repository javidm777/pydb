from django.contrib.auth.views import LoginView
from django.urls import path
from counter import views
from counter.forms import CustomLoginForm
from counter.views import download_wordpress

urlpatterns = [
    # ...
    path('download-wordpress/', download_wordpress, name='download_wordpress'),
    path('counter/', views.counter_page, name='counter_page'),
    path('login/', LoginView.as_view(template_name='counter/login.html',
                                     authentication_form=CustomLoginForm),
         name='login'),

]
