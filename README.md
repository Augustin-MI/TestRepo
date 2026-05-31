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
| `jupyter-labs-eda-sql-coursera_sqllite.ipynb` | Analyse exploratoire des données avec SQL (10 requêtes) |
| `edadataviz.ipynb` | Visualisation des données et Feature Engineering (EDA avec Python) |
| `lab_jupyter_launch_site_location.ipynb` | Cartes interactives avec Folium (géolocalisation, distances, MarkerCluster) |

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

## 📊 Résultats de l'analyse SQL

| Requête | Résultat |
|---------|----------|
| Sites de lancement uniques | CCAFS LC-40, VAFB SLC-4E, KSC LC-39A, CCAFS SLC-40 |
| Masse totale NASA (CRS) | 45 596 kg |
| Masse moyenne F9 v1.1 | 2 928.4 kg |
| Premier atterrissage réussi (ground pad) | 2015-12-22 |
| Boosters avec succès (drone ship, masse 4000-6000 kg) | F9 FT B1022, B1026, B1021.2, B1031.2 |
| Missions réussies (drone ship) | 14 |
| Missions réussies (ground pad) | 9 |
| Missions échouées (drone ship) | 5 |

## 📊 Résultats de l'EDA Visualisation

| Visualisation | Observation clé |
|---------------|-----------------|
| Flight Number vs Launch Site | Plus le numéro de vol augmente, plus le taux de succès s'améliore |
| Payload Mass vs Launch Site | VAFB SLC-4E n'a jamais lancé de charge lourde (>10 000 kg) |
| Succès par type d'orbite | LEO, ISS et Polar ont les meilleurs taux de réussite |
| Tendance annuelle | Le taux de succès augmente régulièrement depuis 2013 |

## 🗺️ Résultats de l'analyse géographique (Folium)

| Observation | Distance | Conclusion |
|-------------|----------|-------------|
| Distance à la côte (coastline) | 0.58 km | Très proche ✅ |
| Distance à la ville (city) | 19.52 km | Relativement éloigné |
| Distance au chemin de fer (railway) | 1.31 km | Très proche ✅ |
| Distance à l'autoroute (highway) | 1.84 km | Très proche ✅ |

**Conclusions :**
- Les sites de lancement sont stratégiquement situés **à proximité immédiate de la côte** (facilité de transport maritime)
- Ils sont également **bien desservis par les infrastructures** (railways, highways) pour l'acheminement des fusées
- Les villes sont **suffisamment éloignées** pour des raisons de sécurité
- Les lancements réussis (vert) sont majoritaires sur tous les sites

## 🔧 Compétences mises en œuvre

| Étape | Compétences |
|-------|-------------|
| Collecte API | Requêtes HTTP, JSON, `pandas.json_normalize()` |
| Web Scraping | `BeautifulSoup`, extraction de tableaux HTML |
| Data Wrangling | Nettoyage, transformation, création de variable cible |
| EDA avec SQL | `SELECT`, `WHERE`, `GROUP BY`, `ORDER BY`, `substr()`, sous-requêtes |
| EDA avec Python | `matplotlib`, `seaborn`, `catplot`, graphiques en barres, tendances |
| Feature Engineering | One-Hot Encoding (`pd.get_dummies`), conversion `float64` |
| Cartographie interactive | `folium`, cercles, marqueurs, MarkerCluster, PolyLine, calcul de distances |
| Gestion des données | Valeurs manquantes (moyenne, suppression), filtrage |

## 📊 Visualiser les notebooks

Les notebooks peuvent ne pas s'afficher correctement sur GitHub. Utilisez nbviewer :

- [Notebook API](https://nbviewer.org/github/Augustin-MI/TestRepo/blob/main/jupyter-labs-spacex-data-collection-api.ipynb)
- [Notebook Web Scraping](https://nbviewer.org/github/Augustin-MI/TestRepo/blob/main/jupyter-labs-spacex-webscraping.ipynb)
- [Notebook Data Wrangling](https://nbviewer.org/github/Augustin-MI/TestRepo/blob/main/labs-jupyter-spacex-Data%20wrangling.ipynb)
- [Notebook EDA SQL](https://nbviewer.org/github/Augustin-MI/TestRepo/blob/main/jupyter-labs-eda-sql-coursera_sqllite.ipynb)
- [Notebook EDA Visualisation](https://nbviewer.org/github/Augustin-MI/TestRepo/blob/main/edadataviz.ipynb)
- [Notebook Folium - Cartes interactives](https://nbviewer.org/github/Augustin-MI/TestRepo/blob/main/lab_jupyter_launch_site_location.ipynb)

## 👤 Auteur
Augustin MI

## 📅 Projet réalisé dans le cadre de
IBM Data Science Professional Certificate - Coursera
