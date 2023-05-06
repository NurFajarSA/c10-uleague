from django.shortcuts import render

# Create your views here.
def pembelian_tiket(request):
    return render(request, 'pembelian_tiket.html')

def list_waktu_stadium_tiket(request):
    return render(request, 'list_waktu_stadium_tiket.html')

def pilih_stadium_tiket(request):
    return render(request, 'pilih_stadium_tiket.html')

def list_pertandingan_tiket(request):
    return render(request, 'list_pertandingan_tiket.html')