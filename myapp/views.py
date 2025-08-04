from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.template.loader import render_to_string

def home(request=None):
    context = {
        'title': 'Accueil',
        'message': 'Bienvenue sur ma WebApp Django !',
        'current_time': datetime.now().strftime('%H:%M:%S'),
        'current_date': datetime.now().strftime('%d/%m/%Y'),
    }
    html = render_to_string('myapp/home.html', context)
    return HttpResponse(html)

def about(request=None):
    context = {
        'title': 'À propos',
        'description': 'Cette application a été créée avec Django pour démontrer une webApp légère.',
        'features': [
            'Interface moderne et responsive',
            'Architecture MVC',
            'Base de données SQLite',
            'Templates Django',
        ]
    }
    html = render_to_string('myapp/about.html', context)
    return HttpResponse(html)

def contact(request=None):
    context = {
        'title': 'Contact',
        'email': 'contact@example.com',
        'phone': '+33 1 23 45 67 89',
        'address': '123 Rue de la Paix, 75001 Paris'
    }
    html = render_to_string('myapp/contact.html', context)
    return HttpResponse(html)
