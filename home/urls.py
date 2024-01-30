from django.urls import path
from .views import Index
from . import views

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('contact/', views.contact_view, name='contact'),
]