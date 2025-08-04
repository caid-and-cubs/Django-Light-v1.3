from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def home(request):
    context = {
        'title': 'Accueil',
        'message': 'Bienvenue sur ma WebApp Django !',
        'current_time': datetime.now().strftime('%H:%M:%S'),
        'current_date': datetime.now().strftime('%d/%m/%Y'),
    }
    return render(request, 'myapp/home.html', context)

def about(request):
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
    return render(request, 'myapp/about.html', context)

def contact(request):
    context = {
        'title': 'Contact',
        'email': 'contact@example.com',
        'phone': '+33 1 23 45 67 89',
        'address': '123 Rue de la Paix, 75001 Paris'
    }
    return render(request, 'myapp/contact.html', context)
