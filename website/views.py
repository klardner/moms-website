from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import ContactForm


def home(request):
    return render(request, 'website/home.html')


def services(request):
    return render(request, 'website/services.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your message. I will get back to you soon.')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'website/contact.html', {'form': form})


def faq(request):
    return render(request, 'website/faq.html')
