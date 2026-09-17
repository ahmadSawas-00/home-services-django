from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from services.models import Service

class Booking(models.Model):
    STATUS_CHOICES = (
        ('pending', 'قيد الانتظار'),
        ('confirmed', 'مؤكد'),
        ('completed', 'مكتمل'),
        ('cancelled', 'ملغى'),
    )

    # وضع default=1 يعين المستخدم رقم 1 كمالك افتراضي لأي سجل جديد أو قديم لا يحوي مستخدم
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        default=1, 
        related_name='bookings', 
        verbose_name="المستخدم"
    )
    
    # وضع default=1 يعين الخدمة رقم 1 كخدمة افتراضية
    service = models.ForeignKey(
        Service, 
        on_delete=models.CASCADE, 
        default=1, 
        related_name='bookings', 
        verbose_name="الخدمة"
    )
    
    # وضع default=timezone.now يعين الوقت والتاريخ الحالي تلقائياً
    booking_date = models.DateTimeField(
        default=timezone.now, 
        verbose_name="تاريخ ووقت الحجز"
    )
    
    # وضع default='' يمنع طلب إدخال نص افتراضي للعنوان في الـ Terminal
    address = models.TextField(
        default='', 
        blank=True, 
        verbose_name="العنوان"
    )
    
    status = models.CharField(
        max_length=20, 
        choices=STATUS_CHOICES, 
        default='pending', 
        verbose_name="حالة الحجز"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name="تاريخ الطلب"
    )

    def __str__(self):
        return f"حجز {self.service.title} - {self.user.username}"