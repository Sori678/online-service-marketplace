from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Q
from .models import Service
from .forms import ServiceForm


def service_list(request):
    """
    Display a list of all services, including search filtering.
    """
    services = Service.objects.all()
    query = request.GET.get('q')
    if query:
        services = services.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )

    return render(
        request,
        'marketplace/services.html',
        {'services': services, 'query': query}
    )


@login_required
def create_service(request):
    """
    Handle the creation of a new service listing.
    """
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
    """
    Display details for a single service.
    """
    service = get_object_or_404(Service, id=service_id)
    return render(
        request,
        'marketplace/service_detail.html',
        {'service': service}
    )


@login_required
def edit_service(request, service_id):
    """
    Handle editing of an existing service listing.
    """
    service = get_object_or_404(Service, id=service_id)

    if service.provider != request.user:
        messages.error(request, 'You do not have permission to edit this.')
        return redirect('service_list')

    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES, instance=service)
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


@login_required
def delete_service(request, service_id):
    """
    Handle service deletion with confirmation.
    """
    service = get_object_or_404(Service, id=service_id)

    if service.provider != request.user:
        messages.error(request, 'You do not have permission to delete this.')
        return redirect('service_list')

    if request.method == 'POST':
        service.delete()
        messages.warning(request, 'The service has been removed.')
        return redirect('service_list')

    return render(
        request,
        'marketplace/service_confirm_delete.html',
        {'service': service}
    )


@login_required
def my_services(request):
    """
    Display a private dashboard for the logged-in user's services.
    """
    user_services = Service.objects.filter(
        provider=request.user
    ).order_by('-created_on')
    total_value = user_services.aggregate(Sum('price'))['price__sum'] or 0

    return render(request, 'marketplace/my_services.html', {
        'services': user_services,
        'total_value': total_value
    })