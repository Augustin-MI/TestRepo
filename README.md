# TestRepo - SpaceX Data Collection

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
| `labs-jupyter-spacex-Data wrangling.ipynb` | Nettoyage et transformation des données |
| `dataset_part_2.csv` | Données avec colonne d'atterrissage (0 = échec, 1 = succès) |
| `jupyter-labs-eda-sql-coursera_sqllite.ipynb` | Analyse exploratoire avec SQL |
| `edadataviz.ipynb` | Visualisation et Feature Engineering |
| `lab_jupyter_launch_site_location.ipynb` | Cartes interactives avec Folium |
| `spacex-dash-app.py` | Tableau de bord interactif Plotly Dash |
| `SpaceX_Machine Learning Prediction_Part_5.ipynb` | Prédiction avec Machine Learning |

## 📊 Résultats du Data Wrangling

| Indicateur | Valeur |
|------------|--------|
| Nombre total de lancements Falcon 9 | 90 |
| Atterrissages réussis (Classe 1) | 60 |
| Atterrissages échoués (Classe 0) | 30 |
| **Taux de succès** | **66.67%** |

## 📊 Résultats de l'analyse SQL

| Requête | Résultat |
|---------|----------|
| Sites de lancement uniques | CCAFS LC-40, VAFB SLC-4E, KSC LC-39A, CCAFS SLC-40 |
| Masse totale NASA (CRS) | 45 596 kg |
| Masse moyenne F9 v1.1 | 2 928.4 kg |
| Premier atterrissage réussi (ground pad) | 2015-12-22 |
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

## 📊 Résultats du Tableau de bord Dash

| Question | Réponse |
|----------|---------|
| Which site has the largest successful launches? | CCAFS SLC-40 |
| Which site has the highest launch success rate? | KSC LC-39A |
| Which payload range(s) has the highest launch success rate? | 0-2000 kg |
| Which payload range(s) has the lowest launch success rate? | 8000-10000 kg |
| Which Booster version has the highest launch success rate? | F9 B5 |

## 🤖 Résultats du Machine Learning

| Modèle | Score Validation | Test Accuracy |
|--------|------------------|---------------|
| Logistic Regression | ~85% | ~83% |
| SVM | ~88% | ~89% |
| Decision Tree | ~82% | ~78% |
| KNN | ~84% | ~83% |

### 🏆 Meilleur modèle
**Support Vector Machine (SVM)** avec environ **89%** de précision.

## 🔧 Compétences mises en œuvre

| Étape | Compétences |
|-------|-------------|
| Collecte API | Requêtes HTTP, JSON, pandas |
| Web Scraping | BeautifulSoup, extraction HTML |
| Data Wrangling | Nettoyage, transformation |
| EDA SQL | SELECT, GROUP BY, sous-requêtes |
| EDA Python | matplotlib, seaborn |
| Feature Engineering | One-Hot Encoding |
| Cartographie | folium, MarkerCluster |
| Dashboard | plotly dash, callbacks |
| Machine Learning | scikit-learn, GridSearchCV |

## 📊 Visualiser les notebooks

Cliquez sur les liens ci-dessous pour visualiser les notebooks avec **nbviewer** (affichage garanti) :

| Notebook | Lien nbviewer |
|----------|---------------|
| Collecte API | [![nbviewer](https://img.shields.io/badge/View-nbviewer-orange)](https://nbviewer.org/github/Augustin-MI/TestRepo/blob/main/jupyter-labs-spacex-data-collection-api.ipynb) |
| Web Scraping | [![nbviewer](https://img.shields.io/badge/View-nbviewer-orange)](https://nbviewer.org/github/Augustin-MI/TestRepo/blob/main/jupyter-labs-webscraping.ipynb) |
| Data Wrangling | [![nbviewer](https://img.shields.io/badge/View-nbviewer-orange)](https://nbviewer.org/github/Augustin-MI/TestRepo/blob/main/labs-jupyter-spacex-Data%20wrangling.ipynb) |
| EDA SQL | [![nbviewer](https://img.shields.io/badge/View-nbviewer-orange)](https://nbviewer.org/github/Augustin-MI/TestRepo/blob/main/jupyter-labs-eda-sql-coursera_sqllite.ipynb) |
| EDA Visualisation | [![nbviewer](https://img.shields.io/badge/View-nbviewer-orange)](https://nbviewer.org/github/Augustin-MI/TestRepo/blob/main/edadataviz.ipynb) |
| Folium | [![nbviewer](https://img.shields.io/badge/View-nbviewer-orange)](https://nbviewer.org/github/Augustin-MI/TestRepo/blob/main/lab_jupyter_launch_site_location.ipynb) |
| Machine Learning | [![nbviewer](https://img.shields.io/badge/View-nbviewer-orange)](https://nbviewer.org/github/Augustin-MI/TestRepo/blob/main/SpaceX_Machine%20Learning%20Prediction_Part_5.ipynb) |

Ou utilisez les liens directs :

- https://nbviewer.org/github/Augustin-MI/TestRepo/blob/main/jupyter-labs-spacex-data-collection-api.ipynb
- https://nbviewer.org/github/Augustin-MI/TestRepo/blob/main/jupyter-labs-webscraping.ipynb
- https://nbviewer.org/github/Augustin-MI/TestRepo/blob/main/labs-jupyter-spacex-Data%20wrangling.ipynb
- https://nbviewer.org/github/Augustin-MI/TestRepo/blob/main/jupyter-labs-eda-sql-coursera_sqllite.ipynb
- https://nbviewer.org/github/Augustin-MI/TestRepo/blob/main/edadataviz.ipynb
- https://nbviewer.org/github/Augustin-MI/TestRepo/blob/main/lab_jupyter_launch_site_location.ipynb
- https://nbviewer.org/github/Augustin-MI/TestRepo/blob/main/SpaceX_Machine%20Learning%20Prediction_Part_5.ipynb

## 👤 Auteur
Augustin MI

## 📅 Projet réalisé dans le cadre de
IBM Data Science Professional Certificate - Coursera
