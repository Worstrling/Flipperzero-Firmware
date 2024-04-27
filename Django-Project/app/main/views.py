from typing import Any

from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories


def index(request) -> HttpResponse:
    context: dict[str, Any] = {
        'title': 'Главная',
        'content': 'Магазин программного обеспечения - HackerZone',
    }
    return render(request, 'main/index.html', context)


def about(request) -> HttpResponse:
    context: dict[str, Any] = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': 'Text'
    }
    return render(request, 'main/about.html', context)
