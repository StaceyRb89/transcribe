# urls.py
from django.contrib import admin
from django.urls import path
from transcribe.views import contact, success

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', contact, name='contact'),
    path('success/', success, name='success'),
]