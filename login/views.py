from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from results.models import certificate

# Create your views here.

def mylogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            if user.is_staff:
                login(request, user)
                return redirect('home')
            else:
                return HttpResponse('You are not authorized to access this page.')
        return HttpResponse('Server down')
    return render(request, 'mylogin/mylogin.html')
    
def home(request):
    certificates = certificate.objects.all()
    context = {
        'certificates':certificates,
    }
    return render(request, 'home.html', context)