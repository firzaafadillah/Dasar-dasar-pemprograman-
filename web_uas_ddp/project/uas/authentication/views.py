from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegisterForms, LoginForms
from django.contrib.auth import logout

# Create your views here.
def register_view(request):
    if request.method == 'POST':
        forms = RegisterForms(request.POST)
        if forms.is_valid():
            forms.save()
            username = forms.cleaned_data.get('username')
            password = forms.cleaned_data.get('password1') 
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('login')
    else:
        forms = RegisterForms()
    return render(request, 'account/register.html', {'forms' : forms})
        
def login_view(request):
    if request.method == 'POST':
        forms = LoginForms(data=request.POST)
        if forms.is_valid():
            user = forms.get_user()
            login(request, user)
            return render(request, 'user/dashboard.html')
    else:
        forms = LoginForms() 
    return render(request, 'account/login.html', {'forms' : forms})

def logout_view(request):
    logout(request)
    return redirect('dashboard')

def dashboard_view(request):
    return render(request, 'user/dashboard.html')

# authentication/views.py

def beranda_view(request): # Nama fungsi sudah diganti
    if request.user.is_authenticated:
        return render(request, 'user/dashboard.html')
    else:
        return render(request, 'user/dashboard.html')
    
def berhitung_view(request):
    # Pastikan file html ini ada di templates/account/berhitung.html
    return render(request, 'account/berhitung.html')

def bilangan_view(request):
    return render(request, 'account/bilangan.html')

def geometri_view(request):
    return render(request, 'account/geometri.html') 