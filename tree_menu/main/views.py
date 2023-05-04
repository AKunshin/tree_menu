from django.shortcuts import get_object_or_404, render
from django.urls import Resolver404

from .models import MenuItem


def index(request, slug=None):
    context={}
    try:
        context_item = get_object_or_404(MenuItem, slug=slug)
        context = {"context_item": context_item}
    except Exception as e:
        print(e)
    return render(request, "main/index.html", context=context)
