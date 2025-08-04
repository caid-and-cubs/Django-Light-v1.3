# WebApp Django Légère - Optimisée pour Render.com

Une application web Django légère et moderne, optimisée pour le déploiement sur Render.com.

## 🚀 Déploiement rapide sur Render.com

### Option 1 : Déploiement via GitHub
1. Forkez ce repository
2. Connectez votre compte GitHub à [Render.com](https://render.com)
3. Créez un nouveau "Web Service"
4. Importez le projet depuis GitHub
5. Déployez en un clic !

### Option 2 : Déploiement via render.yaml
Le fichier `render.yaml` est déjà configuré pour un déploiement automatique.

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
├── build.sh            # Script de build Render
├── render.yaml         # Configuration Render
└── requirements.txt    # Dépendances Python
```

## ✨ Fonctionnalités

- 🎨 Interface moderne et responsive
- 📱 Design adaptatif pour tous les écrans
- ⚡ Optimisé pour Render.com
- 🚀 Déploiement en un clic
- 🔧 Configuration simplifiée
- 💾 Base de données persistante

## 🌐 Accès

Une fois déployé, votre application sera accessible à l'adresse fournie par Render.com.

## 📝 Notes

- Cette version est optimisée pour Render.com avec base de données persistante
- Support complet des sessions et authentification
- Parfait pour les applications de production 