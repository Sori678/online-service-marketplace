from django.shortcuts import render
from .models import Service
# Create your views here.

def service_list(request):
    services = Service.objects.all()
    return render(request, 'marketplace/services.html', {'services': services})