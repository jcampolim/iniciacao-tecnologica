from elasticsearch import Elasticsearch, exceptions
import numpy as np
import pandas as pd
import os

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
            index = "dados-meteorologicos"
            
            df = pd.read_excel("dados.xlsx")

            for i, row in df.iterrows():
                data = str(row["DATE"]).split("-")
                hora = str(row["TIME"]).split(":")

                dia = data[2].split()

                dataFormatada = f"{dia[0]}/{data[1]}/{data[0]} {hora[0]}:{hora[1]}"

                print(dataFormatada)

                doc = {
                    "Date": dataFormatada,
                    "Chuva Acumulada": row["Chuva Acumulada"],
                    "Dir. Vento": row["Dir. Vento"],
                    "Irrad. GHI Acum.": row["Irrad. GHI Acum."],
                    "Irrad. POA Acum.": row["Irrad. POA Acum."],
                    "Irrad. RHD Acum.": row["Irrad. RHD Acum."],
                    "Press. Atm.": row["Press. Atm."],
                    "Rad. GHI": row["Rad. GHI"],
                    "Rad. POA": row["Rad. POA"],
                    "Rad. RHD": row["Rad. RHD"],
                    "Temp. Ar_REG1": row["Temp. Ar_REG1"],
                    "Term. Contato 1": float(row["Term. Contato 1"]),
                    "Term. Contato 2": row["Term. Contato 2"],
                    "Term. Contato 3": row["Term. Contato 3"],
                    "Term. Contato 4": row["Term. Contato 4"],
                    "Term. Contato 5": row["Term. Contato 5"],
                    "Term. Contato 6": row["Term. Contato 6"],
                    "Umid. Ar_REG1": row["Umid. Ar_REG1"],
                    "Vel. Vento": row["Vel. Vento"],
                }
                
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