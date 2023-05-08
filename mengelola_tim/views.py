from django.shortcuts import render

# Create your views here.
def form_daftar_tim(request):
    return render(request, 'form_daftar_tim.html')

def list_tim(request):
    return render(request, 'list_tim.html')

def daftar_pemain(request):
    return render(request, 'daftar_pemain.html')

def daftar_pelatih(request):
    return render(request, 'daftar_pelatih.html')


