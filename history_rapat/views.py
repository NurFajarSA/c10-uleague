from django.shortcuts import redirect, render

from utils.query import query
import datetime
import re

# Create your views here.
def history_rapat(request):
    role = request.COOKIES.get('role')

    if role == None:
        return redirect('home:login')
    if role not in ["MANAJER"]:
        return redirect('home:home')
    
    month_translations = {
    "January": "Januari",
    "February": "Februari",
    "March": "Maret",
    "April": "April",
    "May": "Mei",
    "June": "Juni",
    "July": "Juli",
    "August": "Agustus",
    "September": "September",
    "October": "Oktober",
    "November": "November",
    "December": "Desember"
    }
    
    list_pertandingan, err = query("select * from pertandingan")
    list_rapat, err = query("select * from rapat")
    # print(type(list_pertandingan))
    info_rapat = []
    for i in range(len(list_pertandingan)):


        tim_rapat, err = query(f"select distinct tm.nama_tim from tim_pertandingan tm, pertandingan p where tm.id_pertandingan = '{list_pertandingan[i][0]}'  ")

        tim_rapat = f"{tim_rapat[0][0]} vs {tim_rapat[1][0]}"

        stadium, err = query(f"select distinct s.nama from stadium s, pertandingan p where s.id_stadium = '{list_pertandingan[i][3]}' ")

        stadium = stadium[0][0]

        start_time = list_pertandingan[i][1]
        start_time = start_time.strftime("%d %B %Y, %H:%M")
        
        for month in month_translations:
            if month in start_time:
                translated_month = month_translations[month]
                start_time = re.sub(r'\b{}\b'.format(month), translated_month, start_time)
                    

        end_time = list_pertandingan[i][2]
        end_time = end_time.strftime("%H:%M")

        nama_panitia, err = query(f"SELECT CONCAT(np.nama_depan, ' ', np.nama_belakang) FROM non_pemain np JOIN panitia p ON p.id_panitia = np.id JOIN rapat r ON r.perwakilan_panitia = p.id_panitia where p.id_panitia = '{list_rapat[i][2]}'")
        nama_panitia = nama_panitia[0][0]
        laporan_rapat, err = query(f"select isi_rapat from rapat where id_pertandingan = '{list_pertandingan[i][0]}'")
        info_rapat.append([tim_rapat, nama_panitia, stadium, start_time, end_time, laporan_rapat[0][0]])
        
    context = {
        "info_rapat": info_rapat,
        
        "role": role

    }
   
    return render(request, 'history_rapat.html', context)

def isi_rapat(request,isi):
    role = request.COOKIES.get('role')

    if role == None:
        return redirect('home:login')
    if role not in ["MANAJER"]:
        return redirect('home:home')
    context = {
        "isi_rapat": isi,
        "role": role
    }
    return render(request, 'isi_rapat.html', context)