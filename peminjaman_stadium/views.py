from django.shortcuts import redirect, render

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
    
    context = {
        "role": role
    }
    return render(request, 'pilih_stadium.html', context)

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
