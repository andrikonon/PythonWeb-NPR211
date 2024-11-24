from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

def homepage(request):
    # return HttpResponse("Головна сторінка")
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')

class RobotsTxtView(TemplateView):
    template_name = 'robots.txt'