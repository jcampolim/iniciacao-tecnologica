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
            index = "sem-otimizador"
            
            df = pd.read_excel("dados.xlsx", skiprows=3)

            for i, row in df.iterrows():
                dateRow = str(row["YYYY/MM/DD HH:MM:SS"]).split()
                
                data = dateRow[0].split("-")
                hora = dateRow[1].split(":")

                dataFormatada = f"{data[2]}/{data[1]}/{data[0]} {hora[0]}:{hora[1]}"

                print(dataFormatada)

                doc = {
                    "Date": dataFormatada,
                    "YieldHarvest(kWh)": row["YieldHarvest(kWh)"],
                    "PV1_Volt(V)": row["PV1_Volt(V)"],
                    "PV2_Volt(V)": row["PV2_Volt(V)"],
                    "PV1_Cur(A)": row["PV1_Cur(A)"],
                    "PV2_Cur(A)": row["PV2_Cur(A)"],
                    "Ua/Uab(V)": row["Ua/Uab(V)"],
                    "Ia(A)": row["Ia(A)"],
                    "Q(kVar)": row["Q(kVar)"],
                    "P(kW)": row["P(kW)"],
                    "F(Hz)": row["F(Hz)"],
                    "P1(kW)": row["P1(kW)"],
                    "P2(kW)": row["P2(kW)"],
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