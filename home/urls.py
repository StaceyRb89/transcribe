from django.urls import path
from .views import Index, team, faq
from . import views

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('contact/', views.contact_view, name='contact'),
    path('team/', team, name='team'),
    path('faq/', faq, name='faq'),
]
