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
        'title': 'Главная - О нас',
        'content': 'О нас',
        'text_on_page': 'Добро пожаловать в HackerZone, ваш надежный источник для приобретения специализированного программного обеспечения. Мы предлагаем широкий ассортимент инструментов для тестирования безопасности, анализа данных и других профессиональных решений. Обеспечьте себя лучшими инструментами для достижения ваших целей с HackerZone!'
    }
    return render(request, 'main/about.html', context)


def contact(request) -> HttpResponse:
    context: dict[str, Any] = {
        'title': 'Главная - Контактная информация',
        'content': 'Контакты',
        'text_on_page': 'По всем вопросам пишите на нашу почту: pawidla@mail.ru'
    }
    return render(request, 'main/contact.html', context)
