#написано в 04.04.2026 19.30
# оновлено 05.04.2026 11.12 : додано booking_create 

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Room, Booking, ContactInfo
from .forms import BookingForm, ContactInfoForm


def room_list(request):
    rooms = Room.objects.filter(is_active=True)
    return render(request, 'room_list.html', {'rooms': rooms})


def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, 'booking_list.html', {'bookings': bookings})


def booking_create(request, room_pk):
    room = get_object_or_404(Room, pk=room_pk, is_active=True)

    if request.method == 'POST':
        user = User.objects.filter(is_superuser=True).first()
        if user is None:
            user = User.objects.first()

        booking = Booking.objects.create(
            user=user,
            room=room,
            start_date=request.POST.get('start_date') or None,
            end_date=request.POST.get('end_date') or None,
            notes=request.POST.get('notes', ''),
            status='pending',
        )

        ContactInfo.objects.create(
            booking=booking,
            full_name=request.POST.get('full_name', ''),
            email=request.POST.get('email', ''),
            phone=request.POST.get('phone', ''),
            city=request.POST.get('city', ''),
            country=request.POST.get('country', ''),
            passport=request.POST.get('passport', ''),
        )

        return redirect('booking_list')

    return render(request, 'booking_form.html', {'room': room})
