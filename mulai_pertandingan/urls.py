from django.urls import path
from dashboard.views import show_mulai_pertandingan, show_pilih_peristiwa

app_name = 'dashboard'

urlpatterns = [
    path('', show_mulai_pertandingan, name='show_mulai_pertandingan'),
    path('', show_pilih_peristiwa, name='show_pilih_peristiwa'),
]