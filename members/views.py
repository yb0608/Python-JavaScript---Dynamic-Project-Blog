from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import RegisterFrom
# Create your views here.

class RegisterView (generic.CreateView):
    form_class = RegisterFrom
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')