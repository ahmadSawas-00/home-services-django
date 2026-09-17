from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from services.views import service_list_view  # استيراد الـ view
from bookings.views import booking_list_view  # استيراد الـ view

from django.http import HttpResponse

def home_view(request):
    html_content = """
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <title>منصة الخدمات المنزلية</title>
        <style>
            body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #0f172a; color: #fff; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
            .card { background-color: #1e293b; padding: 40px; border-radius: 16px; box-shadow: 0 10px 25px rgba(0,0,0,0.5); text-align: center; max-width: 450px; width: 100%; }
            h1 { color: #38bdf8; margin-bottom: 10px; font-size: 28px; }
            p { color: #94a3b8; font-size: 15px; line-height: 1.6; margin-bottom: 30px; }
            .btn { display: block; width: 100%; padding: 12px 0; margin: 10px 0; border-radius: 8px; text-decoration: none; font-weight: bold; font-size: 16px; transition: 0.3s; box-sizing: border-box; }
            .btn-primary { background-color: #3b82f6; color: white; }
            .btn-primary:hover { background-color: #2563eb; }
            .btn-success { background-color: #10b981; color: white; }
            .btn-success:hover { background-color: #059669; }
            .btn-secondary { background-color: #334155; color: white; }
            .btn-secondary:hover { background-color: #475569; }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>منصة الخدمات المنزلية</h1>
            <p>مرحباً بك في المنصة الخاصة بإدارة الخدمات والصيانة المنزلية.</p>
            <a href="/services-ui/" class="btn btn-primary">🏷️ استكشاف الخدمات</a>
            <a href="/bookings-ui/" class="btn btn-success">📅 استكشاف الحجوزات</a>
            <a href="/admin/" class="btn btn-secondary">⚙️ لوحة التحكم (Django Admin)</a>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html_content)

urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    path('api/', include('services.urls')),
    path('api/', include('bookings.urls')),
    path('services-ui/', service_list_view, name='services-ui'),
    path('bookings-ui/', booking_list_view, name='bookings-ui'),
]