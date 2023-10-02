
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
            # send email
            subject = 'New Inquiry Received'
            message = f"""You have received a new inquiry with the following details:

            Name: {inquiry.name}
            Institution: {inquiry.institution}
            Email: {inquiry.email}
            Phone: {inquiry.phone}
            Country/Region: {inquiry.country_region}
            State: {inquiry.state}
            City: {inquiry.city}
            Message: {inquiry.message}
            Source Webpage: {inquiry.source_webpage}
            Source IP: {inquiry.source_ip}
            Country from IP: {inquiry.country_from_ip}
            """            
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ['34028312@qq.com',]  # 收件人地址
            send_mail( subject, message, email_from, recipient_list )

            return redirect('inquiry_create')
    else:
        form = InquiryForm()
    inquiries = Inquiry.objects.all()
    return render(request, 'form_handlers/inquiry_create.html', {'form': form, 'inquiries': inquiries})


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_country_from_ip(ip):
    try:
        response = requests.get(f"https://freegeoip.app/json/{ip}")
        data = response.json()
        return data.get('country_name', '')
    except Exception as e:
        return ''


# from django.conf import settings
# from django.shortcuts import render, redirect
# from django.http import JsonResponse
# from .forms import InquiryForm
# from .models import Inquiry
# import requests
# from django.core.mail import send_mail
# from asgiref.sync import sync_to_async

# @sync_to_async
# def send_mail_async(subject, message, email_from, recipient_list):
#     send_mail(subject, message, email_from, recipient_list)

# async def inquiry_create(request):
#     if request.method == "POST":
#         form = InquiryForm(request.POST)
#         if form.is_valid():
#             inquiry = form.save(commit=False)
#             inquiry.source_webpage = request.META.get('HTTP_REFERER', '')
#             inquiry.source_ip = await get_client_ip(request)
#             inquiry.country_from_ip = await get_country_from_ip(inquiry.source_ip)
#             await sync_to_async(inquiry.save)()

#             subject = 'New Inquiry Received'
#             message = f"""You have received a new inquiry with the following details:

#             Name: {inquiry.name}
#             Institution: {inquiry.institution}
#             Email: {inquiry.email}
#             Phone: {inquiry.phone}
#             Country/Region: {inquiry.country_region}
#             State: {inquiry.state}
#             City: {inquiry.city}
#             Message: {inquiry.message}
#             Source Webpage: {inquiry.source_webpage}
#             Source IP: {inquiry.source_ip}
#             Country from IP: {inquiry.country_from_ip}
#             """
#             email_from = settings.EMAIL_HOST_USER
#             recipient_list = ['34028312@qq.com',]  
#             await send_mail_async(subject, message, email_from, recipient_list)

#             return redirect('inquiry_create')
#     else:
#         form = InquiryForm()
#     inquiries = await sync_to_async(Inquiry.objects.all())()
#     return render(request, 'form_handlers/inquiry_create.html', {'form': form, 'inquiries': inquiries})

# @sync_to_async
# def get_client_ip(request):
#     x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
#     if x_forwarded_for:
#         ip = x_forwarded_for.split(',')[0]
#     else:
#         ip = request.META.get('REMOTE_ADDR')
#     return ip

# @sync_to_async
# def get_country_from_ip(ip):
#     try:
#         response = requests.get(f"https://freegeoip.app/json/{ip}")
#         data = response.json()
#         return data.get('country_name', '')
#     except Exception as e:
#         return ''