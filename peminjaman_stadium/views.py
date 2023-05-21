from django.shortcuts import render

# Create your views here.
def peminjaman_stadium(request):
    return render(request, 'peminjaman_stadium.html')

def pilih_stadium(request):
    return render(request, 'pilih_stadium.html')

def list_waktu_stadium(request):
    return render(request, 'list_waktu_stadium.html')
