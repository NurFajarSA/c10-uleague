from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from peminjaman_stadium.forms import PeminjamanStadiumForm
from utils.query import query

# Create your views here.
def peminjaman_stadium(request):
    role = request.COOKIES.get('role')

    if role == None:
        return redirect('home:login')
    if role != "MANAJER":
        return redirect('home:home')
    
    context = {
        "role": role
    }
    
    return render(request, 'peminjaman_stadium.html', context)

def pilih_stadium(request):
    role = request.COOKIES.get('role')

    if role == None:
        return redirect('home:login')
    if role != "MANAJER":
        return redirect('home:home')
    
    list_stadium, err = query("select id_stadium, nama from stadium")
    
    context = {
        "role": role,
        "list_stadium": list_stadium
    }

    # gunakan form yang telah dibuat di forms.py
    if request.method == 'POST':
        form = PeminjamanStadiumForm(request.POST)
        if form.is_valid():
            # ambil data dari form
            stadium = form.cleaned_data['stadium']
            tanggal = form.cleaned_data['tanggal']
            print(stadium)
            print(tanggal)
            # redirect ke halaman list waktu stadium
            return redirect('peminjaman_stadium:list_waktu_stadium')
        

    return render(request, 'pilih_stadium.html', context)

@csrf_exempt
def list_waktu_stadium(request):
    role = request.COOKIES.get('role')

    if role == None:
        return redirect('home:login')
    if role != "MANAJER":
        return redirect('home:home')
    
    context = {
        "role": role
    }
    
    return render(request, 'list_waktu_stadium.html', context)
