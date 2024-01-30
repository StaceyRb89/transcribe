# Views.py
from transcribe.forms import ContactForm
from django.shortcuts import render, redirect, HttpResponse

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            pass
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def success(request):
    return HttpResponse ('Success!')
