from django.shortcuts import render, get_object_or_404
from .models import Service
from django.shortcuts import redirect
from .forms import ServiceForm
from django.contrib import messages
from django.db.models import Sum
# Create your views here.

def service_list(request):
    services = Service.objects.all()
    query = request.GET.get('q')
    if query:
        services = services.filter(title__icontains=query) | services.filter(description__icontains=query)
    
    return render(request, 'marketplace/services.html', {'services': services, 'query': query})

def create_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            service = form.save(commit=False)
            service.provider = request.user  
            service.save()
            messages.success(request, 'The service was created successfully!')
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
            messages.success(request, 'The service has been updated!')
            return redirect('service_detail', service_id=service.id)
    else:
        form = ServiceForm(instance=service)
        
    return render(request, 'marketplace/service_form.html', {
        'form': form,
        'edit_mode': True,
        'service': service
    })

def delete_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    
    if service.provider != request.user:
        return redirect('service_list')
    
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES, instance=service)
        service.delete()
        messages.warning(request, 'The service has been permanently removed.')
        return redirect('service_list')
        
    return render(request, 'marketplace/service_confirm_delete.html', {'service': service})
def my_services(request):
    user_services = Service.objects.filter(provider=request.user).order_by('-created_on')
    total_value = user_services.aggregate(Sum('price'))['price__sum'] or 0
    return render(request, 'marketplace/my_services.html', {
        'services': user_services,
        'total_value': total_value
    })