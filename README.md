# WebApp Django Légère - Optimisée pour Vercel

Une application web Django légère et moderne, optimisée pour le déploiement sur Vercel.

## 🚀 Déploiement rapide sur Vercel

### Option 1 : Déploiement via GitHub
1. Forkez ce repository
2. Connectez votre compte GitHub à [Vercel](https://vercel.com)
3. Importez le projet depuis GitHub
4. Déployez en un clic !

### Option 2 : Déploiement via CLI
```bash
# Installer Vercel CLI
npm install -g vercel

# Se connecter à Vercel
vercel login

# Déployer
vercel
```

## 🛠️ Développement local

```bash
# Installer les dépendances
pip install -r requirements.txt

# Lancer le serveur de développement
python manage.py runserver
```

## 📁 Structure optimisée

```
├── api/
│   └── index.py          # Handler Vercel
├── myproject/            # Configuration Django
├── myapp/               # Application principale
├── templates/           # Templates HTML
├── vercel.json         # Configuration Vercel
└── requirements.txt    # Dépendances Python
```

## ✨ Fonctionnalités

- 🎨 Interface moderne et responsive
- 📱 Design adaptatif pour tous les écrans
- ⚡ Optimisé pour Vercel (serverless)
- 🚀 Déploiement en un clic
- 🔧 Configuration simplifiée

## 🌐 Accès

Une fois déployé, votre application sera accessible à l'adresse fournie par Vercel.

## 📝 Notes

- Cette version est optimisée pour Vercel et ne nécessite pas de base de données persistante
- Les sessions sont temporaires (serverless)
- Parfait pour les démonstrations et prototypes 