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
        index = "sem-otimizador"

        settings = {
            "settings": {
                "number_of_shards": 1,
                "number_of_replicas": 0
            },
            "mappings": {
                "properties": {
                    "Date": {"type":"date",
                            "format":"dd/MM/yyyy HH:mm"},
                    "YieldHarvest(kWh)": { "type": "float" },
                    "PV1_Volt(V)": { "type": "float" },
                    "PV2_Volt(V)": { "type": "float" },
                    "PV1_Cur(A)": { "type": "float" },
                    "PV2_Cur(A)": { "type": "float" },
                    "Ua/Uab(V)": { "type": "float" },
                    "Ia(A)": { "type": "float" },
                    "Q(kVar)": { "type": "float" },
                    "P(kW)": { "type": "float" },
                    "F(Hz)": { "type": "float" },
                    "P1(kW)": { "type": "float" },
                    "P2(kW)": { "type": "float" },
                }
            }
        }

        es.indices.create(index = index, ignore = 400, body = settings)
        
indexer()