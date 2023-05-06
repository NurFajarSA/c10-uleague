from django.shortcuts import render

# Create your views here.
def list_pertandingan(request):
    return render(request, 'list_pertandingan.html')