from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def register(request) -> HttpResponse:
    form = UserCreationForm()
    return render(request, "users/register.html", { 'form': form })