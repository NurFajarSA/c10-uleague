from django.urls import path
from dashboard.views import show_manajer_dashboard, show_panitia_dashboard, show_penonton_dashboard

app_name = 'dashboard'

urlpatterns = [
    path('', show_manajer_dashboard, name='show_manajer_dashboard'),
    path('', show_panitia_dashboard, name='show_panitia_dashboard'),
    path('', show_penonton_dashboard, name='show_penonton_dashboard'),
]
