from django.shortcuts import redirect, render
from utils.query import query
import datetime
import re

# Create your views here.
def list_pertandingan(request):
    role = request.COOKIES.get('role')

    if role == None:
        return redirect('home:login')
    if role not in ["PENONTON", "MANAJER"]:
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
    # print(type(list_pertandingan))
    info_pertandingan = []
    for i in range(len(list_pertandingan)):


        tim_bertanding, err = query(f"select distinct tm.nama_tim from tim_pertandingan tm, pertandingan p where tm.id_pertandingan = '{list_pertandingan[i][0]}'  ")

        tim_bertanding = f"{tim_bertanding[0][0]} vs {tim_bertanding[1][0]}"

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

        info_pertandingan.append([tim_bertanding, stadium, start_time, end_time])
    
    context = {
        "info_pertandingan": info_pertandingan,
        "role": role
    }

    print(info_pertandingan[1])
   
    return render(request, 'list_pertandingan.html', context)
