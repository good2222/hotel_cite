from django.contrib import admin
from .models import Room, Booking, ContactInfo


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'room_type', 'capacity', 'price_per_day', 'floor', 'is_active')
    list_filter = ('room_type', 'is_active', 'has_wifi', 'has_air_conditioning')
    search_fields = ('name',)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'room', 'start_date', 'end_date', 'status', 'is_confirmed', 'total_price')
    list_filter = ('status', 'is_confirmed')
    search_fields = ('user__username', 'room__name')


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'city', 'country', 'booking')
    search_fields = ('full_name', 'email', 'phone')