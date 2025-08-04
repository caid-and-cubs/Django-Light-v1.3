import os
import sys
from pathlib import Path

# Ajouter le répertoire du projet au path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# Configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# Importer Django et les vues
import django
django.setup()

from myapp.views import home, about, contact

# Handler pour Vercel
def handler(request, context):
    try:
        # Configuration pour Vercel
        os.environ.setdefault('VERCEL', 'True')
        
        # Obtenir le chemin de la requête
        path = request.get('url', '/')
        
        # Router vers la bonne vue
        if path == '/':
            response = home()
        elif path == '/about/':
            response = about()
        elif path == '/contact/':
            response = contact()
        else:
            # Page 404
            from django.http import HttpResponse
            response = HttpResponse('Page not found', status=404)
        
        # Retourner la réponse au format Vercel
        return {
            'statusCode': response.status_code,
            'headers': {
                'Content-Type': 'text/html; charset=utf-8',
            },
            'body': response.content.decode('utf-8')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Error: {str(e)}'
        } 