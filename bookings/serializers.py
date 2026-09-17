from rest_framework import serializers
from .models import Booking
from services.serializers import ServiceSerializer

class BookingSerializer(serializers.ModelSerializer):
    # إظهار تفاصيل الخدمة عند العرض
    service_detail = ServiceSerializer(source='service', read_only=True)

    class Meta:
        model = Booking
        fields = '__all__'
        read_only_fields = ('user',)