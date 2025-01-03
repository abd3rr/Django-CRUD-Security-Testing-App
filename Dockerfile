FROM python:3.11-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de l'application
COPY . /app

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Commande pour exécuter l'application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
