from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
from django.views.generic.list import ListView

from form_handlers.forms import InquiryForm


# Create your views here.
def index(request):
    return render(request,'pages/index.html')

def about(request):
    return render(request,'pages/about.html',{
        'form':InquiryForm(),
    })
