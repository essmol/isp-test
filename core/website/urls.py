from django.urls import path
from . import views

app_name = "website"

urlpatterns = [
    
    path("", views.IndexView.as_view(), name="index"),
    path("", views.ContactView.as_view(), name="contact"),
    path("", views.AboutView.as_view(), name="about"),
    path("", views.PakegeView.as_view(), name="package"),
    path("", views.BlogView.as_view(), name="blog"),
    path("", views.FeaturesView.as_view(), name="featuers"),
               
               
               
               
               ]
