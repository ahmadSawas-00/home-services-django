from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Service
from .serializers import ServiceSerializer
from django.shortcuts import render
from django.http import HttpResponse

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all().order_by('-created_at')
    serializer_class = ServiceSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    

def service_list_view(request):
    services = Service.objects.filter(is_available=True)
    return render(request, 'services/service_list.html', {'services': services})


def home_view(request):
    html_content = """
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Home Services API Platform</title>
        <script src="https://cdn.tailwindcss.com"></script>
    </head>
    <body class="bg-slate-900 text-white min-h-screen flex items-center justify-center font-sans">
        <div class="text-center p-8 bg-slate-800 rounded-2xl shadow-2xl border border-slate-700 max-w-lg w-full">
            <h1 class="text-4xl font-extrabold text-blue-400 mb-4">منصة الخدمات المنزلية</h1>
            <p class="text-slate-300 text-lg mb-8 leading-relaxed">
                مرحباً بك في واجهة REST API الخاصة بإدارة الخدمات والصيانة المنزلية.
            </p>
            <div class="flex flex-col gap-4">
                <a href="/api/services/" class="bg-blue-600 hover:bg-blue-500 text-white font-bold py-3 px-6 rounded-xl transition duration-300 shadow-lg shadow-blue-500/30">
                    استكشاف الخدمات (API Services) 🚀
                </a>
                <a href="/admin/" class="bg-slate-700 hover:bg-slate-600 text-slate-200 font-semibold py-3 px-6 rounded-xl transition duration-300 border border-slate-600">
                    لوحة التحكم (Django Admin) ⚙️
                </a>
            </div>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html_content)