# 📸 Application Streamlit — EXIF & Voyages

Cette application a été réalisée dans le cadre de l’exercice 4.2 du module **Outils Collaboratifs**.

Elle permet de :
- Modifier les métadonnées **EXIF GPS** d'une image JPEG
- Afficher sur une carte l'emplacement géographique d'une photo
- Représenter les lieux visités ou rêvés sur une carte interactive sous forme de POI

## 🚀 Lancer l'application en local

1. Cloner le projet :
git clone https://github.com/Ghratar/streamlit-exif-voyages.git
cd streamlit-exif-voyages

2. Créer et activer un environnement virtuel :
python -m venv venv
.\venv\Scripts\Activate.ps1    # ou `venv\Scripts\activate` sur CMD

3. Installer les dépendances :
pip install -r requirements.txt

4. Lancer l'application :
streamlit run app.py

L’application s’ouvre automatiquement dans le navigateur sur http://localhost:8501

## 🧰 Fonctionnalités

- Téléversement d'une image JPEG
- Formulaire pour modifier les coordonnées GPS (Latitude, Longitude)
- Sauvegarde d'une nouvelle image avec métadonnées modifiées
- Affichage de l'emplacement sur une carte (Folium)
- Carte interactive avec tous les voyages passés ou rêves depuis un fichier CSV

## 📁 Arborescence du projet

streamlit-exif-voyages/
│
├── app.py               → Application principale Streamlit
├── requirements.txt     → Liste des dépendances Python
├── README.md            → Fichier d’explication du projet
│
├── data/
│   └── photo.jpg        → Image JPEG à modifier
│
└── assets/
    └── lieux.csv        → Coordonnées des lieux à afficher sur la carte

## 🌐 Déploiement en ligne

Déploiement possible via https://streamlit.io/cloud en connectant ce dépôt GitHub.

## 👤 Auteur

Réalisé par @Ghratar dans le cadre de l’Université Paris 8.
