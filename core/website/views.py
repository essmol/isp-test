from django.shortcuts import render,redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    FormView,
    CreateView
)






class IndexView(TemplateView):
    template_name = 'website/index.html'


class ContactView(TemplateView):
    template_name = 'website/contact.html'



class AboutView(TemplateView):
    template_name = 'website/about.html'  

class PakegeView(TemplateView):
    template_name = 'website/package.html' 


class BlogView(TemplateView):
    template_name = 'blog/blog.html' 


class FeaturesView(TemplateView):
    template_name = 'website/featuers.html'             