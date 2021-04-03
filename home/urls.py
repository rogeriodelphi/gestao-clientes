from django.urls import path
from .views import home, my_logout
from django.views.generic.base import TemplateView


urlpatterns = [
    path('', home, name='home'),
    path('logout/', my_logout, name='logout'),
    path('home2/', TemplateView.as_View(), name='home2'),
]