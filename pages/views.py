from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
from django.views.generic.list import ListView

from form_handlers.forms import InquiryForm
from .models import Faq
from blog.models import Blog

# Create your views here.
def index(request):
    faqs = Faq.objects.filter(is_active=True)
    blog = Blog.objects.all()[:3]

    return render(request,'pages/index.html',{
        'faqs':faqs,
        'blog':blog,
    })

def about(request):
    return render(request,'pages/about.html',{
        'form':InquiryForm(),
    })

def contact(request):
    return render(request,'pages/contact.html')


def test(request):
    return render(request,'pages/more/test.html')