from django.shortcuts import redirect, render

# Create your views here.
def pilih_pertandingan(request):
    role = request.COOKIES.get('role')

    if role == None:
        return redirect('home:login')
    if role != "PANITIA":
        return redirect('home:home')
    
    context = {
        "role": role
    }
    
    return render(request, 'pilih_pertandingan.html', context)

def rapat_pertandingan(request):
    role = request.COOKIES.get('role')

    if role == None:
        return redirect('home:login')
    if role != "PANITIA":
        return redirect('home:home')
    
    context = {
        "role": role
    }

    return render(request, 'rapat_pertandingan.html', context)

