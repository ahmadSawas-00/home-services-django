from rest_framework import viewsets, permissions
from .models import Booking
from .serializers import BookingSerializer
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # الأدمن يرى جميع الحجوزات، والمستخدم العادي يرى حجوزاته فقط
        if self.request.user.is_staff:
            return Booking.objects.all().order_by('-created_at')
        return Booking.objects.filter(user=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        # ربط الحجز بالمستخدم المسجل حالياً تلقائياً
        serializer.save(user=self.request.user)


@login_required
def booking_list_view(request):
    # جلب حجوزات المستخدم المسجل حالياً فقط
    user_bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/booking_list.html', {'bookings': user_bookings})