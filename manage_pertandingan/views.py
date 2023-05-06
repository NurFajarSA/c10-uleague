from django.shortcuts import render

# Create your views here.
def manage_pertandingan(request):
    return render(request, 'manage_pertandingan.html')