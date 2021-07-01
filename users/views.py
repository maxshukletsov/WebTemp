from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import UserManager, User
from django.views.generic import DetailView, ListView


# Create your views here.
class SignUp(generic.CreateView):
    form_class = UserManager
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class AccountformListView(ListView):  # представление в виде списка
    model = User  # модель для представления

class AccountformDetailView(DetailView):
    model = User