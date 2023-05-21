from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from utils.query import query
import uuid

# Create your views here.
@login_required(login_url='/login_register/')
def home(request):
    return render(request, 'home.html')

@csrf_exempt
def login_register(request):
    return render(request, 'login_register.html')

def register(request):
   
    return render(request, 'register.html')

def register_manajer(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        nama_depan = request.POST.get("nama_depan")
        nama_belakang = request.POST.get("nama_belakang")
        nomor_hp = request.POST.get("telp")
        email = request.POST.get("email")
        alamat = request.POST.get("alamat")
        role = request.POST.get("role")
        id = str(uuid.uuid4())

        print([username, password, nama_depan, nama_belakang, nomor_hp, email, alamat, role, id])
        
        try:
            ins_user_system, err = query(f"insert into user_system(username,password) values ('{username}', '{password}')")
            ins_non_pemain, err = query(f"insert into non_pemain(id,nama_depan,nama_belakang,nomor_hp,email,alamat) values ('{id}', '{nama_depan}', '{nama_belakang}','{nomor_hp}', '{email}','{alamat}')")
            ins_status_non_pemain, err = query(f"insert into status_non_pemain(id_non_pemain,status) values ('{id}', '{role}')")
            ins_manajer, err = query(f"insert into manajer(id_manajer ,username) values ('{id}', '{username}')")
        
            messages.success(request, "Berhasil mendaftar sebagai manajer!")
            return redirect("home:login")
            
        except Exception as e:
            messages.error(request, e)

    return render(request, "register_manajer.html")

def register_penonton(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        nama_depan = request.POST.get("nama_depan")
        nama_belakang = request.POST.get("nama_belakang")
        nomor_hp = request.POST.get("telp")
        email = request.POST.get("email")
        alamat = request.POST.get("alamat")
        role = request.POST.get("role")
        id = str(uuid.uuid4())

        print([username, password, nama_depan, nama_belakang, nomor_hp, email, alamat, role, id])
        
        try:
            ins_user_system, err = query(f"insert into user_system(username,password) values ('{username}', '{password}')")
            ins_non_pemain, err = query(f"insert into non_pemain(id,nama_depan,nama_belakang,nomor_hp,email,alamat) values ('{id}', '{nama_depan}', '{nama_belakang}','{nomor_hp}', '{email}','{alamat}')")
            ins_status_non_pemain, err = query(f"insert into status_non_pemain(id_non_pemain,status) values ('{id}', '{role}')")
            ins_penonton, err = query(f"insert into penonton(id_penonton ,username) values ('{id}', '{username}')")
        
            messages.success(request, "Berhasil mendaftar sebagai penonton!")
            return redirect("home:login")
            
        except Exception as e:
            messages.error(request, e)
            
    return render(request, "register_penonton.html")

def register_panitia(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        nama_depan = request.POST.get("nama_depan")
        nama_belakang = request.POST.get("nama_belakang")
        nomor_hp = request.POST.get("telp")
        email = request.POST.get("email")
        alamat = request.POST.get("alamat")
        role = request.POST.get("role")
        id = str(uuid.uuid4())
        jabatan = request.POST.get("jabatan")
        print([username, password, nama_depan, nama_belakang, nomor_hp, email, alamat, role, id, jabatan])
        
        try:
            ins_user_system, err = query(f"insert into user_system(username,password) values ('{username}', '{password}')")
            ins_non_pemain, err = query(f"insert into non_pemain(id,nama_depan,nama_belakang,nomor_hp,email,alamat) values ('{id}', '{nama_depan}', '{nama_belakang}','{nomor_hp}', '{email}','{alamat}')")
            ins_status_non_pemain, err = query(f"insert into status_non_pemain(id_non_pemain,status) values ('{id}', '{role}')")

            q4 =f"insert into panitia(id_panitia, jabatan ,username) values ('{id}', '{jabatan}', '{username}')"
            ins_panitia, err = query(q4)
            print(q4)

            messages.success(request, "Berhasil mendaftar sebagai panitia!")
            return redirect("home:login")
            
        except Exception as e:
            messages.error(request, e)
            
    return render(request, "register_panitia.html")




@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home:home')
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

@csrf_exempt
def logout_user(request):
    logout(request)
    return redirect('home:login_register')