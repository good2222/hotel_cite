from django.db import models
from django.contrib.auth.models import User
#написано в 03.04.2026 21.01 


class Room(models.Model):
    ROOM_TYPES = [
        ('single', 'Одномісний'),
        ('double', 'Двомісний'),
        ('suite', 'Люкс'),
        ('family', 'Сімейний'),
    ]

    name = models.CharField(max_length=100, verbose_name='Назва')
    room_type = models.CharField(max_length=10, choices=ROOM_TYPES, default='single', verbose_name='Тип кімнати')
    capacity = models.PositiveIntegerField(verbose_name='Місткість')
    price_per_day = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Ціна за день')
    description = models.TextField(blank=True, verbose_name='Опис')
    floor = models.PositiveIntegerField(default=1, verbose_name='Поверх')
    has_wifi = models.BooleanField(default=True, verbose_name='Wi-Fi')
    has_tv = models.BooleanField(default=True, verbose_name='Телевізор')
    has_air_conditioning = models.BooleanField(default=False, verbose_name='Кондиціонер')
    is_active = models.BooleanField(default=True, verbose_name='Активна')

    class Meta:
        verbose_name = 'Кімната'
        verbose_name_plural = 'Кімнати'

    def __str__(self):
        return f"{self.name} ({self.get_room_type_display()})"


class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Очікує'),
        ('confirmed', 'Підтверджено'),
        ('cancelled', 'Скасовано'),
        ('completed', 'Завершено'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='bookings',
        verbose_name='Користувач'
    )
    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE,
        related_name='bookings',
        verbose_name='Кімната'
    )
    start_date = models.DateTimeField(null=True, blank=True, verbose_name='Дата заїзду')
    end_date = models.DateTimeField(null=True, blank=True, verbose_name='Дата виїзду')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Створено')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Оновлено')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending', verbose_name='Статус')
    is_confirmed = models.BooleanField(default=False, verbose_name='Підтверджено')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name='Загальна вартість')
    notes = models.TextField(blank=True, verbose_name='Примітки')

    class Meta:
        verbose_name = 'Бронювання'
        verbose_name_plural = 'Бронювання'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} - {self.room.name}"

    def nights(self):
        return (self.end_date - self.start_date).days


class ContactInfo(models.Model):
    booking = models.OneToOneField(
        Booking,
        on_delete=models.CASCADE,
        related_name='contact',
        verbose_name='Бронювання'
    )
    full_name = models.CharField(max_length=150, verbose_name='Повне імʼя')
    email = models.EmailField(verbose_name='Email')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    city = models.CharField(max_length=100, blank=True, verbose_name='Місто')
    country = models.CharField(max_length=100, blank=True, verbose_name='Країна')
    passport = models.CharField(max_length=20, blank=True, verbose_name='Паспорт')

    class Meta:
        verbose_name = 'Контактна інформація'
        verbose_name_plural = 'Контактна інформація'

    def __str__(self):
        return self.full_name