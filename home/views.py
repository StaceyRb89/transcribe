from django.shortcuts import render
from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = 'home/index.html'

def contact_view(request):
    # Your contact view implementation
    return render(request, 'contact/contact.html') 