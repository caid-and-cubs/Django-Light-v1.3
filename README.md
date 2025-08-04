# WebApp Django Légère

Une application web simple créée avec Django.

## Installation

1. Créer un environnement virtuel :
```bash
python -m venv venv
```

2. Activer l'environnement virtuel :
- Windows : `venv\Scripts\activate`
- Linux/Mac : `source venv/bin/activate`

3. Installer les dépendances :
```bash
pip install -r requirements.txt
```

4. Appliquer les migrations :
```bash
python manage.py migrate
```

5. Créer un superutilisateur (optionnel) :
```bash
python manage.py createsuperuser
```

## Lancement

Pour démarrer le serveur de développement :
```bash
python manage.py runserver
```

L'application sera accessible à l'adresse : http://127.0.0.1:8000/

## Structure du projet

- `myproject/` - Configuration principale du projet Django
- `myapp/` - Application principale avec les vues et modèles
- `templates/` - Templates HTML
- `static/` - Fichiers statiques (CSS, JS, images) 