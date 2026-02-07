from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

# Create your views here.

def mylogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            if user.is_staff:
                login(request, user)
                return HttpResponse('welcome to certificate')
            else:
                return HttpResponse('You are not authorized to access this page.')
        return HttpResponse('Server down')
    return render(request, 'mylogin/mylogin.html')