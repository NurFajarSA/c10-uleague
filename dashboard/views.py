from django.shortcuts import render

# Create your views here.
def show_manajer_dashboard(request):
    return render(request, 'manajer_dashboard.html')

def show_panitia_dashboard(request):
    return render(request, 'panitia_dashboard.html')

def show_penonton_dashboard(request):
    return render(request, 'penonton_dashboard.html')