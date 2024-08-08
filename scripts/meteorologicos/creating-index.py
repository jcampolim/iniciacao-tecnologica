from datetime import datetime
from elasticsearch import Elasticsearch
import pandas as pd
import os

def indexer():
    es = Elasticsearch(
        hosts=["https://host.docker.internal:9200"],
        basic_auth=('elastic', os.getenv("ELASTIC_PASSWORD")),
        verify_certs=False,
        max_retries=30,
        retry_on_timeout=True,
        request_timeout=30,
    )

    if es.ping: 
        print("Connection with Elasticsearch: Success")    
        index = "dados-meteorologicos"

        settings = {
            "settings": {
                "number_of_shards": 1,
                "number_of_replicas": 0
            },
            "mappings": {
                "properties": {
                    "Date": {"type":"date",
                            "format":"dd/MM/yyyy HH:mm"},
                    "Chuva Acumulada": { "type": "float" },
                    "Dir. Vento": { "type": "float" },
                    "Irrad. GHI Acum.": { "type": "float" },
                    "Irrad. POA Acum.": { "type": "float" },
                    "Irrad. RHD Acum.": { "type": "float" },
                    "Press. Atm.": { "type": "float" },
                    "Rad. GHI": { "type": "float" },
                    "Rad. POA": { "type": "float" },
                    "Rad. RHD": { "type": "float" },
                    "Temp. Ar_REG1": { "type": "float" },
                    "Term. Contato 1": { "type": "float" },
                    "Term. Contato 2": { "type": "float" },
                    "Term. Contato 3": { "type": "float" },
                    "Term. Contato 4": { "type": "float" },
                    "Term. Contato 5": { "type": "float" },
                    "Term. Contato 6": { "type": "float" },
                    "Umid. Ar_REG1": { "type": "float" },
                    "Vel. Vento": { "type": "float" },
                }
            }
        }
        
        es.indices.create(index = index, ignore = 400, body = settings)
indexer()