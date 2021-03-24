# Les bases d'Elasticsearch et de Kibana

## Introduction
Ce dépôt contient une présentation ainsi que quelques scripts basiques en Python pour apprendre et découvrir les grandes bases d'ElasticSearch et de Kibana.

## Installation
Pour lancer ElasticSearch et Kibana, assurez-vous dans un premier temps d'avoir installé et lancé correctement Docker et Docker Compose : https://docs.docker.com/get-docker/

Une fois correctement installé, ouvrez votre terminal. Déplacez vous jusqu'au dossier __les_bases_elasticsearch_kibana__ et lancez la commande suivante :

```
docker-compose up -d
```

Rendez-vous sur http://localhost:9200 pour vérifier qu'ElasticSearch est bien lancé (cela peut prendre plusieurs minutes).

## Créer un premier index

```
PUT /my-first-index
```

## Ajouter des documents dans un index

```
POST my-first-index/_doc/
{
  "@timestamp": "2099-11-15T13:12:00",
  "message": "Hello World",
  "user": "mister"
}
```

Pour ajouter des données dans un index en Python, référez-vous au script __add_data.py__.
Pour ajouter ou modifier des champs dans des données sur un index en Python, référez-vous au script __modify_data.py__.

## Utiliser kibana

Rendez-vous sur http://localhost:5601 pour utiliser l'interface Kibana pour créer des analyses et visualiser vos index.