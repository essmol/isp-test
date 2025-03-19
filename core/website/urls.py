from django.urls import path
from . import views

app_name = "website"

urlpatterns = [
    
    path("", views.IndexView.as_view(), name="index"),
    path("contact/", views.ContactView.as_view(), name="contact"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("package", views.PakegeView.as_view(), name="package"),
    path("posts/", views.BlogView.as_view(), name="blog"),
    path("featuers/", views.FeaturesView.as_view(), name="featuers"),
               
               
               
               
               ]
