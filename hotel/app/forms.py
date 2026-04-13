#еаписано в 04.04.2026 19.14

from django import forms
from .models import Room, Booking, ContactInfo

class ContactInfoForm(forms.ModelForm):
    class Meta:
        model = ContactInfo
        fields = ['full_name', 'email', 'phone', 'city', 'country', 'passport']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'passport': forms.TextInput(attrs={'class': 'form-control'}),
        }
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['room', 'start_date', 'end_date', 'notes']
        widgets = {
            'room': forms.Select(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control'}),
        }
class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = [
            'name',
            'room_type',
            'capacity',
            'price_per_day',
            'description',
            'floor',
            'has_wifi',
            'has_tv',
            'has_air_conditioning',
            'is_active',
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'room_type': forms.Select(attrs={'class': 'form-control'}),
            'capacity': forms.NumberInput(attrs={'class': 'form-control'}),
            'price_per_day': forms.NumberInput(
                attrs={'class': 'form-control', 'step': '0.01'}
            ),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'floor': forms.NumberInput(attrs={'class': 'form-control'}),
            'has_wifi': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'has_tv': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'has_air_conditioning': forms.CheckboxInput(
                attrs={'class': 'form-check-input'}
            ),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }