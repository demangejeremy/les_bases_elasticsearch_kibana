# Imports
from elasticsearch import Elasticsearch
import re

# Var
i = 0

# Index et champs a analyser
indexlocal = "my-first-index"
champsatraiter = "name"

# Modifier le code au besoin
es = Elasticsearch()
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
        texte = doc['_source'][champsatraiter]
        print(texte)

        # Ajouter un champs
        new = ["test"]
        # new = postagging(texte)
        entry = {'nouveau': new}

        print(i)
        print("="*20)

        # Ajout entree
        resp = es.update(index=indexlocal, id=idloc, body={"doc": entry})
