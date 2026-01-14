from django.shortcuts import render
from .models import Service
from django.shortcuts import redirect
from .forms import ServiceForm
# Create your views here.

def service_list(request):
    services = Service.objects.all()
    return render(request, 'marketplace/services.html', {'services': services})

def create_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            service = form.save(commit=False)
            service.provider = request.user  
            service.save()
            return redirect('service_list')
    else:
        form = ServiceForm()
    return render(request, 'marketplace/service_form.html', {'form': form})