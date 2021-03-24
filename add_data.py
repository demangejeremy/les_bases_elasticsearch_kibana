from Elasticsearch import Elasticsearch
import uuid

es = Elasticsearch(hosts=["http://localhost:9200"])

my_data = {
    "name": "George Peterson",
    "sex": "male",
    "age": "34",
    "years": "10"
}

response = es.index(
    index='employees',
    doc_type='person',
    id=uuid.uuid4(),
    body=my_data
)
