from django.urls import path
from pembelian_tiket.views import *

app_name = 'pembelian_tiket'

urlpatterns = [
    path('', pilih_stadium_tiket, name='pilih_stadium_tiket'),
    path('list_waktu_stadium/', list_waktu_stadium_tiket, name='list_waktu_stadium_tiket'),
    path('list_pertandingan/', list_pertandingan_tiket, name="list_pertandingan_tiket"),
    path('beli_tiket/', pembelian_tiket, name="pembelian_tiket")
    

]