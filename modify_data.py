# Imports
from elasticsearch import Elasticsearch
import re

# Var
boolindex = 0
i = 0

# Index et champs a analyser
indexlocal = "proverbes"
champsatraiter = "texte"

# Modifier le code au besoin
es = Elasticsearch(hosts=["http://localhost:9200"])
es.indices.put_settings(index=indexlocal,
                        body={"index": {
                            "max_result_window": 500000
                        }})
# {"match": {"texte": {"query": "gilets"}}}})
res = es.search(index=indexlocal, body={"query":  {"match_all": {}}})
nbreresul = res['hits']['total']
print(nbreresul)
# {"match": {"texte": {"query": "gilets"}}}},size=10)
res = es.search(index=indexlocal, body={
                "query":  {"match_all": {}}})
for hit in res['hits']['hits']:
    i += 1
    source = hit['_source']
    if (champsatraiter not in hit['_source']):
        print("chaine vide")
        textinteg = "pas de description"
    else:
        textinteg = source[champsatraiter]
        textinteg = ' '.join(textinteg.split())
        idloc = hit['_id']
        # print(idloc)
        doc = es.get(index=indexlocal, id=idloc)

        # Recup texte
        texte = doc['_source']['texte']
        print(texte)

        # Ajouter un champs
        new = []
        # new = postagging(texte)
        entry = {'nouveau_champs': new}

        print(i)
        print("="*20)

        # Ajout entree
        resp = es.update(index=indexlocal, id=idloc, body={"doc": entry})
