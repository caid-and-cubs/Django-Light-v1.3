import os
import sys
from pathlib import Path

# Ajouter le répertoire du projet au path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# Import de l'application WSGI
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Handler pour Vercel
def handler(request, context):
    return application(request, context) 