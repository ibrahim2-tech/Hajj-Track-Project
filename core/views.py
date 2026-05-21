from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import HajjService, PilgrimProfile, Booking

def register_view(request):
    if request.method == "POST":
        user = User.objects.create_user(
            username=request.POST.get('username'),
            email=request.POST.get('email'),
            password=request.POST.get('password')
        )
        PilgrimProfile.objects.create(
            user=user,
            nationality=request.POST.get('nationality'),
            identity_type=request.POST.get('identity_type'),
            identity_number=request.POST.get('identity_number'),
            gender=request.POST.get('gender')
        )
        return redirect('login')
    return render(request, 'core/register.html')

def login_view(request):
    if request.method == "POST":
        user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
        if user:
            login(request, user)
            return redirect('services_list')
    return render(request, 'core/login.html')

@login_required
def services_list(request):
    return render(request, 'core/services_list.html', {'services': HajjService.objects.all()})

@login_required
def service_detail(request, service_id):
    service = get_object_or_404(HajjService, id=service_id)
    
    if request.method == "POST":
        Booking.objects.create(pilgrim=request.user, service=service)
        return redirect('detail', service_id=service_id) 
    
    bookings = service.booking_set.select_related('pilgrim__pilgrimprofile').all()
    
    context = {
        'service': service, 
        'bookings': bookings
    }
    return render(request, 'core/service_detail.html', context)

@login_required
def add_service(request):
    if request.method == "POST":

        title = request.POST.get('title')
        category = request.POST.get('category')
        camp_location = request.POST.get('camp_location')
        description = request.POST.get('description')
        cost = request.POST.get('cost')
        
        HajjService.objects.create(
            title=title, 
            category=category, 
            camp_location=camp_location, 
            description=description, 
            cost=cost
        )
        return redirect('services_list')
        
    return render(request, 'core/add_service.html')

@login_required
def update_service(request, service_id):
    service = get_object_or_404(HajjService, id=service_id)
    
    if request.method == "POST":
        service.title = request.POST.get('title')
        service.category = request.POST.get('category')
        service.camp_location = request.POST.get('camp_location')
        service.description = request.POST.get('description')
        service.cost = request.POST.get('cost')
        service.save() 
        return redirect('services_list')
        
    return render(request, 'core/update_service.html', {'service': service})
@login_required
def delete_service(request, service_id):
    service = get_object_or_404(HajjService, id=service_id)
    service.delete()
    return redirect('services_list')

def logout_view(request):
    logout(request)
    return redirect('login')
