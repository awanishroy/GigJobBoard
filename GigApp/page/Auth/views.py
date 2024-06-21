# GigApp/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            if user.is_active:
                login(request, user)
                messages.success(request, 'Logged in successfully.')
                return redirect('home')  # Redirect to admin home page after login
            else:
                return render(request, 'admin/auth/login.html', {'error_message': 'Invalid User'})
        else:
            return render(request, 'admin/auth/login.html', {'error_message': 'Invalid User'})
    
    return render(request, 'admin/auth/login.html')

@login_required
def custom_logout(request):
    logout(request)
    messages.info(request, 'Logged out successfully.')
    return redirect('admin.home')  # Redirect to custom login page after logout