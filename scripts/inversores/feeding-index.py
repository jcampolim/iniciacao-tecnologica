from datetime import datetime
from elasticsearch import Elasticsearch, exceptions
import numpy as np
import pandas as pd
import os
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def replace_invalid_values(data):
    for k, v in data.items():
         if k != "Date": 
            if isinstance(v, str) and not v.replace('.', '', 1).isdigit():
                data[k] = None
            elif isinstance(v, float) and np.isnan(v):
                data[k] = None
    return data

def indexer():
    try:
        es = Elasticsearch(
            hosts=["https://host.docker.internal:9200"],
            basic_auth=('elastic', os.getenv("ELASTIC_PASSWORD")),
            verify_certs=False,
            max_retries=30,
            retry_on_timeout=True,
            request_timeout=30,
        )

        if es.ping():
            print("Connection with Elasticsearch: Success")

            index = "inversores"
            
            df = pd.read_excel("dados.xlsx")
            df = df.where(pd.notnull(df), None)
            df.dropna()

            for i, row in df.iterrows():
                data = str(row["Data"]).split("-")
                hora = str(row["Hora"]).split(":")

                dia = data[2].split()
                
                dataFormatada = f"{dia[0]}/{data[1]}/{data[0]} {hora[0]}:{hora[1]}"

                print(dataFormatada)

                doc = {
                    "Date": dataFormatada,
                    "Vrms ph-n L1N Mín": row["Vrms ph-n L1N Mín"],
                    "Vrms ph-n L1N Méd.": row["Vrms ph-n L1N Méd."],
                    "Vrms ph-n L1N Máx": row["Vrms ph-n L1N Máx"],
                    "Vrms ph-n L1N Status": row["Vrms ph-n L1N Status"],
                    "Vrms ph-n L2N Mín": row["Vrms ph-n L2N Mín"],
                    "Vrms ph-n L2N Méd.": row["Vrms ph-n L2N Méd."],
                    "Vrms ph-n L2N Máx": row["Vrms ph-n L2N Máx"],
                    "Vrms ph-n L2N Status": row["Vrms ph-n L2N Status"],
                    "Vrms ph-n L3N Mín": row["Vrms ph-n L3N Mín"],
                    "Vrms ph-n L3N Méd.": row["Vrms ph-n L3N Méd."],
                    "Vrms ph-n L3N Máx": row["Vrms ph-n L3N Máx"],
                    "Vrms ph-n L3N Status": row["Vrms ph-n L3N Status"],
                    "Vrms ph-n NG Mín": row["Vrms ph-n NG Mín"],
                    "Vrms ph-n NG Méd.": row["Vrms ph-n NG Méd."],
                    "Vrms ph-n NG Máx": row["Vrms ph-n NG Máx"],
                    "Vrms ph-n NG Status": row["Vrms ph-n NG Status"],
                    "Vrms ph-ph L12 Mín": row["Vrms ph-ph L12 Mín"],
                    "Vrms ph-ph L12 Méd.": row["Vrms ph-ph L12 Méd."],
                    "Vrms ph-ph L12 Máx": row["Vrms ph-ph L12 Máx"],
                    "Vrms ph-ph L12 Status": row["Vrms ph-ph L12 Status"],
                    "Vrms ph-ph L23 Mín": row["Vrms ph-ph L23 Mín"],
                    "Vrms ph-ph L23 Méd.": row["Vrms ph-ph L23 Méd."],
                    "Vrms ph-ph L23 Máx": row["Vrms ph-ph L23 Máx"],
                    "Vrms ph-ph L23 Status": row["Vrms ph-ph L23 Status"],
                    "Vrms ph-ph L31 Mín": row["Vrms ph-ph L31 Mín"],
                    "Vrms ph-ph L31 Méd.": row["Vrms ph-ph L31 Méd."],
                    "Vrms ph-ph L31 Máx": row["Vrms ph-ph L31 Máx"],
                    "Vrms ph-ph L31 Status": row["Vrms ph-ph L31 Status"],
                    "Corrente L1 Mín": row["Corrente L1 Mín"],
                    "Corrente L1 Méd.": row["Corrente L1 Méd."],
                    "Corrente L1 Máx": row["Corrente L1 Máx"],
                    "Corrente L1 Status": row["Corrente L1 Status"],
                    "Corrente L2 Mín": row["Corrente L2 Mín"],
                    "Corrente L2 Méd.": row["Corrente L2 Méd."],
                    "Corrente L2 Máx": row["Corrente L2 Máx"],
                    "Corrente L2 Status": row["Corrente L2 Status"],
                    "Corrente L3 Mín": row["Corrente L3 Mín"],
                    "Corrente L3 Méd.": row["Corrente L3 Méd."],
                    "Corrente L3 Máx": row["Corrente L3 Máx"],
                    "Corrente L3 Status": row["Corrente L3 Status"],
                    "Corrente N Mín": row["Corrente N Mín"],
                    "Corrente N Méd.": row["Corrente N Méd."],
                    "Corrente N Máx": row["Corrente N Máx"],
                    "Corrente N Status": row["Corrente N Status"],
                    "Freqüência Mín": row["Freqüência Mín"],
                    "Freqüência Méd.": row["Freqüência Méd."],
                    "Freqüência Máx": row["Freqüência Máx"],
                    "Freqüência Status": row["Freqüência Status"],
                    "Assimetria Vn Mín": row["Assimetria Vn Mín"],
                    "Assimetria Vn Méd.": row["Assimetria Vn Méd."],
                    "Assimetria Vn Máx": row["Assimetria Vn Máx"],
                    "Assimetria Vn Status": row["Assimetria Vn Status"],
                    "Assimetria Vz Mín": row["Assimetria Vz Mín"],
                    "Assimetria Vz Méd.": row["Assimetria Vz Méd."],
                    "Assimetria Vz Máx": row["Assimetria Vz Máx"],
                    "Assimetria Vz Status": row["Assimetria Vz Status"],
                    "Assimetria An Mín": row["Assimetria An Mín"],
                    "Assimetria An Méd.": row["Assimetria An Méd."],
                    "Assimetria An Máx": row["Assimetria An Máx"],
                    "Assimetria An Status": row["Assimetria An Status"],
                    "Assimetria Az Mín": row["Assimetria Az Mín"],
                    "Assimetria Az Méd.": row["Assimetria Az Méd."],
                    "Assimetria Az Máx": row["Assimetria Az Máx"],
                    "Assimetria Az Status": row["Assimetria Az Status"],
                    "Potência Ativa L1N Mín": row["Potência Ativa L1N Mín"],
                    "Potência Ativa L1N Méd.": row["Potência Ativa L1N Méd."],
                    "Potência Ativa L1N Máx": row["Potência Ativa L1N Máx"],
                    "Potência Ativa L1N Status": row["Potência Ativa L1N Status"],
                    "Potência Ativa L2N Mín": row["Potência Ativa L2N Mín"],
                    "Potência Ativa L2N Méd.": row["Potência Ativa L2N Méd."],
                    "Potência Ativa L2N Máx": row["Potência Ativa L2N Máx"],
                    "Potência Ativa L2N Status": row["Potência Ativa L2N Status"],
                    "Potência Ativa L3N Mín": row["Potência Ativa L3N Mín"],
                    "Potência Ativa L3N Méd.": row["Potência Ativa L3N Méd."],
                    "Potência Ativa L3N Máx": row["Potência Ativa L3N Máx"],
                    "Potência Ativa L3N Status": row["Potência Ativa L3N Status"],
                    "Potência Ativa Total Mín": row["Potência Ativa Total Mín"],
                    "Potência Ativa Total Méd.": row["Potência Ativa Total Méd."],
                    "Potência Ativa Total Máx": row["Potência Ativa Total Máx"],
                    "Potência Aparente L1N Mín": row["Potência Aparente L1N Mín"],
                    "Potência Aparente L1N Méd.": row["Potência Aparente L1N Méd."],
                    "Potência Aparente L1N Máx": row["Potência Aparente L1N Máx"],
                    "Potência Aparente L1N Status": row["Potência Aparente L1N Status"],
                    "Potência Aparente L2N Mín": row["Potência Aparente L2N Mín"],
                    "Potência Aparente L2N Méd.": row["Potência Aparente L2N Méd."],
                    "Potência Aparente L2N Máx": row["Potência Aparente L2N Máx"],
                    "Potência Aparente L2N Status": row["Potência Aparente L2N Status"],
                    "Potência Aparente L3N Mín": row["Potência Aparente L3N Mín"],
                    "Potência Aparente L3N Méd.": row["Potência Aparente L3N Méd."],
                    "Potência Aparente L3N Máx": row["Potência Aparente L3N Máx"],
                    "Potência Aparente L3N Status": row["Potência Aparente L3N Status"],
                    "Potência Aparente Total Mín": row["Potência Aparente Total Mín"],
                    "Potência Aparente Total Méd.": row["Potência Aparente Total Méd."],
                    "Potência Aparente Total Máx": row["Potência Aparente Total Máx"],
                    "Fator de Potência L1N Mín": row["Fator de Potência L1N Mín"],
                    "Fator de Potência L1N Méd.": row["Fator de Potência L1N Méd."],
                    "Fator de Potência L1N Máx": row["Fator de Potência L1N Máx"],
                    "Fator de Potência L1N Status": row["Fator de Potência L1N Status"],
                    "Fator de Potência L2N Mín": row["Fator de Potência L2N Mín"],
                    "Fator de Potência L2N Méd.": row["Fator de Potência L2N Méd."],
                    "Fator de Potência L2N Máx": row["Fator de Potência L2N Máx"],
                    "Fator de Potência L2N Status": row["Fator de Potência L2N Status"],
                    "Fator de Potência L3N Mín": row["Fator de Potência L3N Mín"],
                    "Fator de Potência L3N Méd.": row["Fator de Potência L3N Méd."],
                    "Fator de Potência L3N Máx": row["Fator de Potência L3N Máx"],
                    "Fator de Potência L3N Status": row["Fator de Potência L3N Status"],
                    "Fator de Potência Total Mín": row["Fator de Potência Total Mín"],
                    "Fator de Potência Total Méd.": row["Fator de Potência Total Méd."],
                    "Fator de Potência Total Máx": row["Fator de Potência Total Máx"],
                    "Energia Ativa L1N Mín": row["Energia Ativa L1N Mín"],
                    "Energia Ativa L1N Méd.": row["Energia Ativa L1N Méd."],
                    "Energia Ativa L1N Máx": row["Energia Ativa L1N Máx"],
                    "Energia Ativa L1N Status": row["Energia Ativa L1N Status"],
                    "Energia Ativa L2N Mín": row["Energia Ativa L2N Mín"],
                    "Energia Ativa L2N Méd.": row["Energia Ativa L2N Méd."],
                    "Energia Ativa L2N Máx": row["Energia Ativa L2N Máx"],
                    "Energia Ativa L2N Status": row["Energia Ativa L2N Status"],
                    "Energia Ativa L3N Mín": row["Energia Ativa L3N Mín"],
                    "Energia Ativa L3N Méd.": row["Energia Ativa L3N Méd."],
                    "Energia Ativa L3N Máx": row["Energia Ativa L3N Máx"],
                    "Energia Ativa L3N Status": row["Energia Ativa L3N Status"],
                    "Energia Ativa Total Mín": row["Energia Ativa Total Mín"],
                    "Energia Ativa Total Méd.": row["Energia Ativa Total Méd."],
                    "Energia Ativa Total Máx": row["Energia Ativa Total Máx"],
                    "THD V L1N Mín": row["THD V L1N Mín"],
                    "THD V L1N Méd.": row["THD V L1N Méd."],
                    "THD V L1N Máx": row["THD V L1N Máx"],
                    "THD V L1N Status": row["THD V L1N Status"],
                    "THD V L2N Mín": row["THD V L2N Mín"],
                    "THD V L2N Méd.": row["THD V L2N Méd."],
                    "THD V L2N Máx": row["THD V L2N Máx"],
                    "THD V L2N Status": row["THD V L2N Status"],
                    "THD V L3N Mín": row["THD V L3N Mín"],
                    "THD V L3N Méd.": row["THD V L3N Méd."],
                    "THD V L3N Máx": row["THD V L3N Máx"],
                    "THD V L3N Status": row["THD V L3N Status"],
                    "THD V NG Mín": row["THD V NG Mín"],
                    "THD V NG Méd.": row["THD V NG Méd."],
                    "THD V NG Máx": row["THD V NG Máx"],
                    "THD V NG Status": row["THD V NG Status"],
                    "THD A L1 Mín": row["THD A L1 Mín"],
                    "THD A L1 Méd.": row["THD A L1 Méd."],
                    "THD A L1 Máx": row["THD A L1 Máx"],
                    "THD A L1 Status": row["THD A L1 Status"],
                    "THD A L2 Mín": row["THD A L2 Mín"],
                    "THD A L2 Méd.": row["THD A L2 Méd."],
                    "THD A L2 Máx": row["THD A L2 Máx"],
                    "THD A L2 Status": row["THD A L2 Status"],
                    "THD A L3 Mín": row["THD A L3 Mín"],
                    "THD A L3 Méd.": row["THD A L3 Méd."],
                    "THD A L3 Máx": row["THD A L3 Máx"],
                    "THD A L3 Status": row["THD A L3 Status"],
                    "THD A N Mín": row["THD A N Mín"],
                    "THD A N Méd.": row["THD A N Méd."],
                    "THD A N Máx": row["THD A N Máx"],
                    "THD A N Status": row["THD A N Status"],
                }
                
                doc = replace_invalid_values(doc)
                
                try:
                    es.index(index=index, body=doc)
                except exceptions.RequestError as e:
                    print(f"RequestError: {e}")
                except exceptions.ConnectionError as e:
                    print(f"ConnectionError: {e}")
                except exceptions.AuthenticationException as e:
                    print(f"AuthenticationException: {e}")
                except exceptions.AuthorizationException as e:
                    print(f"AuthorizationException: {e}")
                except Exception as e:
                    print(f"An error occurred while indexing document {i}: {e}")

        else:
            print("Connection with Elasticsearch: Failed")
    
    except exceptions.ConnectionError as e:
        print(f"ConnectionError: {e}")
    except exceptions.AuthenticationException as e:
        print(f"AuthenticationException: {e}")
    except exceptions.AuthorizationException as e:
        print(f"AuthorizationException: {e}")
    except exceptions.RequestError as e:
        print(f"RequestError: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

indexer()