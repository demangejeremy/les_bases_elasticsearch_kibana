from elasticsearch import Elasticsearch
import uuid

es = Elasticsearch()

my_data = {
    "name": "John Doe",
    "sex": "male",
    "age": "34",
}

response = es.index(
    index='my-first-index',
    id=uuid.uuid4(),
    body=my_data
)
