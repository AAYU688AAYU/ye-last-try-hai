from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password')
    
    return render(request, 'login.html')

@login_required
def dashboard_view(request):
    context = {
        'user': request.user,
        'diagnoses': request.user.diagnoses.all()
    }
    return render(request, 'dashboard.html', context)

def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('login')