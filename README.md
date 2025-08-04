# WebApp Django Légère - Optimisée pour Railway.com

Une application web Django légère et moderne, optimisée pour le déploiement sur Railway.com.

## 🚀 Déploiement rapide sur Railway.com

### Option 1 : Déploiement via GitHub
1. Forkez ce repository
2. Connectez votre compte GitHub à [Railway.com](https://railway.com)
3. Créez un nouveau projet
4. Importez le repository depuis GitHub
5. Ajoutez une base de données PostgreSQL
6. Déployez en un clic !

### Option 2 : Déploiement via CLI
```bash
# Installer Railway CLI
npm install -g @railway/cli

# Se connecter à Railway
railway login

# Déployer
railway up
```

## 🛠️ Développement local

```bash
# Installer les dépendances
pip install -r requirements.txt

# Appliquer les migrations
python manage.py migrate

# Lancer le serveur de développement
python manage.py runserver
```

## 📁 Structure optimisée

```
├── myproject/            # Configuration Django
├── myapp/               # Application principale
├── templates/           # Templates HTML
├── Procfile            # Configuration Railway
├── railway.json        # Configuration Railway
└── requirements.txt    # Dépendances Python
```

## ✨ Fonctionnalités

- 🎨 Interface moderne et responsive
- 📱 Design adaptatif pour tous les écrans
- ⚡ Optimisé pour Railway.com
- 🚀 Déploiement en un clic
- 🔧 Configuration simplifiée
- 💾 Base de données PostgreSQL
- 🔒 SSL automatique

## 🌐 Accès

Une fois déployé, votre application sera accessible à l'adresse fournie par Railway.com.
https://web-production-6ec3.up.railway.app/

## 📝 Notes

- Cette version est optimisée pour Railway.com avec PostgreSQL
- Support complet des sessions et authentification
- Parfait pour les applications de production
- Déploiement automatique depuis GitHub 
