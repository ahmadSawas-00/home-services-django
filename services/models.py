from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name="اسم الخدمة")
    description = models.TextField(verbose_name="وصف الخدمة")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="السعر")
    is_available = models.BooleanField(default=True, verbose_name="متاحة؟")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإضافة")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاريخ التحديث")

    def __str__(self):
        return self.title