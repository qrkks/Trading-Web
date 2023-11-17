
# Create your views here.
from django.conf import settings
from django.shortcuts import render, redirect
from .forms import InquiryForm
from .models import Inquiry
import requests
from django.core.mail import send_mail



def inquiry_create(request):
    if request.method == "POST":
        form = InquiryForm(request.POST)
        if form.is_valid():
            inquiry = form.save(commit=False)
            inquiry.source_webpage = request.META.get('HTTP_REFERER', '')
            inquiry.source_ip = get_client_ip(request)
            inquiry.country_from_ip = get_country_from_ip(inquiry.source_ip)
            inquiry.save()
            return render(request,'form_handlers/indicator-submitted.html')
    else:
        form = InquiryForm()
    # inquiries = Inquiry.objects.all()
    return render(request, 'form_handlers/indicator-submitted.html', {'form': form})

# ... other functions ...



def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_country_from_ip(ip):
    try:
        response = requests.get(f"https://freegeoip.app/json/{ip}",timeout=10)
        data = response.json()
        return data.get('country_name', '')
    except Exception as e:
        return ''

