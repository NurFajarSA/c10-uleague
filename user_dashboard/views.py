from django.shortcuts import render

# Create your views here.
def manajer_dashboard(request):
    return render(request, 'manajer_dashboard.html')

def panitia_dashboard(request):
    return render(request, 'panitia_dashboard.html')

def penonton_dashboard(request):
    return render(request, 'penonton_dashboard.html')