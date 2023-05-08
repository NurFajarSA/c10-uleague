from django.shortcuts import render

# Create your views here.
def pilih_pertandingan(request):
    return render(request, 'pilih_pertandingan.html')

def rapat_pertandingan(request):
    return render(request, 'rapat_pertandingan.html')

