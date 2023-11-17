from django.middleware.csrf import get_token
from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
from django.views.generic.list import ListView
from render_block import render_block_to_string

from form_handlers.forms import InquiryForm
from .models import Banner, Faq, HomeCarouselImage
from blog.models import Blog
from abstractapp.custom_context_processors import global_context

# Create your views here.


def index(request):
    faqs = Faq.objects.active().order_by('-custom_order')
    blog = Blog.objects.all()[:3]
    carousels = HomeCarouselImage.objects.active().all().order_by('-custom_order')
    banner = Banner.objects.active().order_by('-custom_order').first()
    context = {
        'faqs': faqs,
        'blog': blog,
        'carousels': carousels,
        'banner': banner,
    }
    if request.headers.get('HX-Request') == 'true':
        html = render_block_to_string('pages/index.html', 'content', context)
        return HttpResponse(html)

    return render(request, 'pages/index.html', context)


def about(request):
    context = global_context(request)
    context["csrf_token"] = get_token(request)

    if request.headers.get('HX-Request') == 'true':
        html = render_block_to_string(
            'pages/about.html', 'content', context)
        return HttpResponse(html)
    return render(request, 'pages/about.html')


def contact(request):
    context = global_context(request)
    context["csrf_token"] = get_token(request)

    if request.headers.get('HX-Request') == 'true':
        html = render_block_to_string('pages/contact.html', 'content', context)
        return HttpResponse(html)

    return render(request, 'pages/contact.html', context)


# def test(request):
#     return render(request,'pages/more/test.html')
