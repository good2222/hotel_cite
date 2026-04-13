#написано в 04.04.2026 19.40
# оновлено 05.04.2024 13.49 : додано booking_create 
from django.urls import path
from . import views

urlpatterns = [
    path('', views.room_list, name='room_list'),
    path('bookings/', views.booking_list, name='booking_list'),
    path('bookings/create/<int:room_pk>/', views.booking_create, name='booking_create'),
]

