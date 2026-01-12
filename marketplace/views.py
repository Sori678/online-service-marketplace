from django.shortcuts import render
from django.views import Service
# Create your views here.
from django.shortcuts import render
from .models import Service

def service_list(request):
    services = Service.objects.all()
    return render(request, 'marketplace/services.html', {'services': services})