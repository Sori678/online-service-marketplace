from django.shortcuts import render, get_object_or_404
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

def service_detail(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    return render(request, 'marketplace/service_detail.html', {'service': service})

def edit_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    
    if service.provider != request.user:
        return redirect('service_list') 
    
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('service_detail', service_id=service.id)
    else:
        form = ServiceForm(instance=service)
        
    return render(request, 'marketplace/service_form.html', {
        'form': form,
        'edit_mode': True,
        'service': service
    })