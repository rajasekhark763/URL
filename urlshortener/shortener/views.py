from django.shortcuts import render
from shortener.models import Url
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy
# Create your views here.

class UrlListView(ListView):
    model=Url
# Create your views here.
class UrlDetailView(DetailView):
    model=Url

class UrlCreateView(CreateView):
    model=Url
    fields=('main_url','new_url')

class UrlUpdateView(UpdateView):
    model=Url
    fields=('main_url','new_url')

class UrlDeleteView(DeleteView):
    model=Url
    success_url=reverse_lazy('urls')
