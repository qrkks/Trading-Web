from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Inquiry, NotificationInbox
import threading
from django.conf import settings



@receiver(post_save, sender=Inquiry)
def send_inquiry_email(sender, instance, created, **kwargs):
    if created:
        # 查询 NotificationInbox 模型以获取所有邮箱地址
        recipient_list = NotificationInbox.objects.filter(is_active=True).values_list('email', flat=True)

        # 检查 recipient_list 是否非空
        if not recipient_list:
            print("Error: No recipients found in NotificationInbox")
            return
        
        # 在新线程中发送邮件
        email_thread = threading.Thread(target=send_email_in_thread, args=(instance, recipient_list))
        email_thread.start()


def send_email_in_thread(instance,recipient_list):
    subject = 'New Inquiry Received'
    message = f"""
    You have received a new inquiry with the following details:

    Name: {instance.name}
    Institution: {instance.institution}
    Email: {instance.email}
    Phone: {instance.phone}
    Country/Region: {instance.country_region}
    State: {instance.state}
    City: {instance.city}
    Message: {instance.message}
    Source Webpage: {instance.source_webpage}
    Source IP: {instance.source_ip}
    Country from IP: {instance.country_from_ip}
    """
    print('Email sent to:', recipient_list)
    email_from = f"Inquiry Request Service <{settings.EMAIL_HOST_USER}>"
    send_mail(subject, message, email_from, recipient_list)
    print('Email sent successfully')