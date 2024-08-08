# Scripts Python

Um script Python é usado para comunicar os dados do Google Drive com o Docker. Inicialmente, podemos definir dois modelos de código diferentes que foram usados: o primeiro para criar um índice no Elasticsearch (um índice é um espaço lógico que contém uma coleção de documentos, onde cada documento possui vários campos ordenados por pares de chave-valor) e o segundo para enviar dados para um índice já criado.

Em ambos os casos, a primeira coisa a ser feita é indicar a porta que o Elasticsearch está alocado (definida no arquivo `docker-compose.yml`, mas por padrão é 9200). 

```python
import os
import Elasticsearch from elasticsearch

es = Elasticsearch(
    hosts=["https://host.docker.internal:9200"],
    basic_auth=('elastic', os.getenv("ELASTIC_PASSWORD")),
    verify_certs=False,
    max_retries=30,
    retry_on_timeout=True,
    request_timeout=30,
)
```

Para que esse comando funcione, é preciso ter instalado o Elasticsearch Python Client. Geralmente basta executar `pip install elasticsearch` no terminal para instalar. Entretanto, nesse caso, essa biblioteca já está presente no arquivo de requerimentos, que irá instalar todas as dependências utilizadas no código Python.

Para verificar se a conexão foi estabelecida com sucesso, é possível usar o comando `es.ping()`, que retornará um valor booleano indicando se o Python conseguiu se conectar. Se a conexão com o Elasticsearch for estabelecida, então é possível dar continuidade ao script.

### Criando um índice no ELasticsearch

Para criar um índice usamos o comando `es.indices.create(index=index)`. Porém, antes de criar um índice é importante definir suas propriedades, ou seja, é importante definir os dados e os tipos de dados que serão armazenados. Para fazer isso, utilizamos um dicionário com todas os campos mapeados, como no exemplo abaixo:

```python
if es.ping():
    index = "parcial"

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
    es.indices.create(index=index, body=settings)
```

O Elasticsearch possui alguns tipos de dados nativos, entre eles: keyword, text, numeric (integer, long, float ou double), date, IP e boolean. Além disso, é possível estabelecer uma formatação para alguns campos, como foi feito no campo de data acima.

### Adicionando dados a um índice existente

Para adicionar dados a um índice já existente, primeiro é preciso ler os dados do arquivo. Para isso, é possível usar a biblioteca do Python `pandas` (que será instalada junto com os requerimentos). Além disso, também é preciso estabelecer quais colunas correspondem aos dados mapeados no índice. Um exemplo de como esse código ficaria é:

```python
import pandas as pd

index = "dados-meteorologicos"
df = pd.read_excel("inversores.xlsx")

for i, row in df.iterrows():
    data = str(row["DATE"]).split("-")
    hora = str(row["TIME"]).split(":")
    dia = data[2].split()

    dataFormatada = f"{dia[0]}/{data[1]}/{data[0]} {hora[0]}:{hora[1]}"

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

    es.index(index=index, body=doc)
```

Alguns arquivos podem ser mais complexos e precisar ter os dados tratados antes de serem enviados para o Elasticsearch. Um caso que ocorreu durante o desenvolvimento do projeto foi com os dados de inversores, que tinham diversas colunas vazias ou com dados que não condiziam ao tipo que foi estabelecido para eles.

A parte de colunas vazias pode ser resolvida facilmente com o comando `df.dropna()` do Pandas. Já para os dados com os tipos diferentes, uma solução foi criar uma função que percorre cada linha para verificar se os dados estão adequados. Essa solução nem sempre é a melhor, em casos de menor volumetria é possível fazer o tratamento somente nas colunas mais despadronizadas, que têm uma tendência maior a erros de leitura.
