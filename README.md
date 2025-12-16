# login

Starter FastAPI service scaffold.

## Démarrage rapide
- Crée un environnement virtuel puis installe les dépendances: `pip install -r requirements.txt`
- Démarre le serveur de dev: `uvicorn main:app --reload`
- Consulte la doc interactive: ouvre `http://127.0.0.1:8000/docs`

## Configuration
- Les valeurs par défaut sont définies dans `app/core/config.py`.
- Tu peux surcharger via des variables d'environnement (ex: `APP_NAME`, `DEBUG`, `ENVIRONMENT`) ou un fichier `.env`.
