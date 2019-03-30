from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="HOME"),
    path('about-us/',views.about,name="ABOUT"),    
    path('contact/',views.contact,name="CONTACT"),
]
