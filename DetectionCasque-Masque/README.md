Détection de Casque et Gilet de Sécurité
Contexte du Projet
Les systèmes de vidéosurveillance jouent un rôle essentiel dans de nombreuses applications, garantissant la sécurité. Notre entreprise se spécialise dans le développement de solutions technologiques pour la vidéosurveillance. Dans ce projet, nous développons une application web basée sur l'intelligence artificielle (IA) capable de repérer les casques et gilets de sécurité dans des vidéos.

L'application doit activer la caméra de l'ordinateur et afficher en temps réel les résultats de la détection. En outre, elle génère une alerte si quelqu'un ne porte pas de casque ou de gilet de sécurité.

Objectif
Notre principal objectif est de créer une application web robuste capable de repérer en temps réel les casques et gilets de sécurité dans des vidéos. Voici nos principales missions :

Détection des Équipements de Sécurité : Développer un algorithme d'IA pour repérer la présence ou l'absence de casques et de gilets de sécurité dans des vidéos.

Interface Web Conviviale : Créer une interface conviviale affichant les vidéos et les résultats de la détection.

Gestion des Alertes : Générer des alertes sur la page web en cas de non-port de casque ou de gilet de sécurité.

Vérification de l'Uniforme : Afficher "Uniforme vérifié" si toutes les détections sont conformes, sinon "Uniforme non vérifié".

Fonctionnalités
Détection en temps réel des casques et gilets de sécurité dans les vidéos.
Affichage des vidéos en temps réel avec les résultats de la détection.
Alerte en cas de non-port de casque ou de gilet de sécurité.
Affichage de "Uniforme vérifié" si toutes les détections sont conformes, sinon "Uniforme non vérifié".
Prérequis
Avant de commencer, assurez-vous de disposer des éléments suivants :

Environnement de Développement : Python 3.x configuré sur votre ordinateur.

Bibliothèques Python : Installez les bibliothèques nécessaires en utilisant le fichier requirements.txt.

Caméra d'Ordinateur : Une caméra pour la détection en temps réel.

Structure du Projet
Organisez le projet sur votre machine comme suit :

Copy code
Safety-Detector/
│ 
├─── assets/
│   └─── pic1.png
│
├─── images/
│   ├─── worker.png
│   └─── worker_detected.png
│
├─── weights/
│   ├─── best.pt
│   ├─── yolo8n.pt
│   ├─── yolov8n-cls.pt
│   └─── yolov8n-seg.pt
│
├─── .gitignore
├─── README.md
├─── app.py
├─── helper.py
├─── settings.py
└─── requirements.txt

Installation et Utilisation
Pour mettre en place et utiliser l'application de détection de casque et gilet de sécurité, suivez ces étapes :

Clonez ce dépôt sur votre ordinateur.

Installez les dépendances requises en exécutant la commande suivante :

bash
Copy code
pip install -r requirements.txt
Lancez l'application web avec la commande :

bash
Copy code
streamlit run app.py
Ouvrez un navigateur et accédez à l'URL suivante : http://localhost:5001 (ou l'adresse affichée lors du lancement de l'application) pour utiliser l'application.