from django.shortcuts import render
from utils.query import query
import datetime
import re
from random import randint

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"

# Create your views here.
def pembelian_tiket(request,id_pertandingan):
    if request.method == 'POST':
        jenis_tiket = request.POST.get('jenis_tiket')
        pembayaran = request.POST.get('Pembayaran')
        
        #ubah kalo login udah diimplement
        id_penonton = "4194aa96-eccb-11ed-a05b-0242ac120003"

        receipt_builder = ""

        
        receipt_builder += pembayaran[0]


        for i in range(7):
            check = randint(0,1)
            if check == 0:
                receipt_builder += alphabet[randint(0,25)]
            else: 
                receipt_builder += number[randint(0,9)]
        
        print([jenis_tiket,pembayaran,id_penonton,id_pertandingan])
        q4 = f"insert into pembelian_tiket(nomor_receipt,id_penonton, jenis_tiket, jenis_pembayaran, id_pertandingan) values ('{receipt_builder}','{id_penonton}', '{jenis_tiket}', '{pembayaran}', '{id_pertandingan}')"
        ins_pembelian_tiket, err = query(q4)
        print(q4)
   
        
    return render(request, 'pembelian_tiket.html')


def list_waktu_stadium_tiket(request):
    if request.method == 'POST':
        stadium = request.POST.get('stadium')
        date = request.POST.get('date')
        
        list_pertandingan, err = query(f"Select p.start_datetime, p.end_datetime from pertandingan p where '{date}' = DATE(p.start_datetime) and p.stadium in (select p.stadium from pertandingan p, stadium s where p.stadium =  s.id_stadium and s.nama = '{stadium}')")
        
        clean_list_pertandingan = []
        
        for i in range(len(list_pertandingan)):
            clean_list_pertandingan.append([0,0])
            clean_list_pertandingan[i][0] = list_pertandingan[i][0].strftime("%H:%M")
            clean_list_pertandingan[i][1] = list_pertandingan[i][1].strftime("%H:%M")

        # print(clean_list_pertandingan)
        context = {
            'stadium': stadium,
            # 'date': list_pertandingan[0].strftime("%d %B %Y, %H:%M"),
            'date': list_pertandingan[0][0].strftime("%Y-%m-%d %H:%M"),

            'list_pertandingan' : clean_list_pertandingan
        }
        return render(request, 'list_waktu_stadium_tiket.html', context)
    
    return render(request, 'list_waktu_stadium_tiket.html')


# def pilih_stadium_tiket(request):
#     return render(request, 'pilih_stadium_tiket.html')



def list_pertandingan_tiket(request,waktu,stadium):
    print(waktu)
    print(stadium)
    id_pertandingan, err = query(f"select id_pertandingan from pertandingan where start_datetime='{waktu}' and stadium=(select p.stadium from pertandingan p, stadium s where p.stadium = s.id_stadium and s.nama = '{stadium}')")
    id_pertandingan = str(id_pertandingan[0][0])
    
    tim_bertanding, err = query(f"select distinct tm.nama_tim from tim_pertandingan tm, pertandingan p where tm.id_pertandingan = '{str(id_pertandingan)}'" )
    tim_bertanding = [tim_bertanding[0][0], tim_bertanding[1][0]]
    context = {
        'tim_bertanding' : tim_bertanding,
        'id_pertandingan' : id_pertandingan
    }
    return render(request, 'list_pertandingan_tiket.html',context)


# Create your views here.
def pilih_stadium_tiket(request):
    
    list_stadium, err = query("select nama from stadium")
   
    for i in range(len(list_stadium)):
        list_stadium[i] = list_stadium[i][0]
    
    context = {
        "list_stadium" : list_stadium
    }

    print(list_stadium)
   
    return render(request, 'pilih_stadium_tiket.html', context)

