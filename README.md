# TestRepo - SpaceX Data Collection

[![nbviewer](https://img.shields.io/badge/View%20in-nbviewer-orange)](https://nbviewer.org/github/Augustin-MI/TestRepo/blob/main/jupyter-labs-spacex-data-collection-api.ipynb)

## 📌 Description
Ce dépôt contient les notebooks du projet SpaceX réalisé dans le cadre du cours IBM Data Science.

L'objectif est de collecter, nettoyer et analyser les données des lancements SpaceX pour prédire l'atterrissage du premier étage de Falcon 9.

## 📁 Fichiers

| Fichier | Description |
|---------|-------------|
| `jupyter-labs-spacex-data-collection-api.ipynb` | Collecte via l'API REST SpaceX |
| `dataset_part_1.csv` | Données exportées après nettoyage (API) |
| `jupyter-labs-webscraping.ipynb` | Collecte via Web Scraping (Wikipedia) |
| `spacex_web_scraped.csv` | Données extraites par Web Scraping |
| `labs-jupyter-spacex-Data wrangling.ipynb` | Nettoyage et transformation des données (création de la colonne `Class`) |
| `dataset_part_2.csv` | Données finales avec colonne d'atterrissage (0 = échec, 1 = succès) |

## 📊 Résultats du Data Wrangling

| Indicateur | Valeur |
|------------|--------|
| Nombre total de lancements Falcon 9 | 90 |
| Atterrissages réussis (Classe 1) | 60 |
| Atterrissages échoués (Classe 0) | 30 |
| **Taux de succès** | **66.67%** |

### Répartition des classes
- **Classe 1 (succès)** : 60 lancements
- **Classe 0 (échec)** : 30 lancements

## 🔧 Compétences mises en œuvre

| Étape | Compétences |
|-------|-------------|
| Collecte API | Requêtes HTTP, JSON, `pandas.json_normalize()` |
| Web Scraping | `BeautifulSoup`, extraction de tableaux HTML |
| Data Wrangling | Nettoyage, transformation, création de variable cible |
| Gestion des données | Valeurs manquantes (moyenne, suppression), filtrage |

## 📊 Visualiser les notebooks

Les notebooks peuvent ne pas s'afficher correctement sur GitHub. Utilisez nbviewer :

- [Notebook API](https://nbviewer.org/github/Augustin-MI/TestRepo/blob/main/jupyter-labs-spacex-data-collection-api.ipynb)
- [Notebook Web Scraping](https://nbviewer.org/github/Augustin-MI/TestRepo/blob/main/jupyter-labs-spacex-webscraping.ipynb)
- [Notebook Data Wrangling](https://nbviewer.org/github/Augustin-MI/TestRepo/blob/main/labs-jupyter-spacex-Data%20wrangling.ipynb)

## 👤 Auteur
Augustin MI

## 📅 Projet réalisé dans le cadre de
IBM Data Science Professional Certificate - Coursera
