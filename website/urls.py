
from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('contact.html', views.contact, name="contact"),
]
