# Estrutura de arquivos

Este projeto segue a seguinte estrutura de diretórios e arquivos:

```
docker/
├── docker-compose.yml
├── .env
├── app/
│   ├── Dockerfile
│   ├── data.xlsx
│   ├── main.py
│   └── requirements.txt
├── download/
│   └── download.py
```

Todas as configurações necessárias para criar os contêineres do Elasticsearch e do Kibana foram obtidas na documentação oficial da Elastic.

* Link para a documentação: [Elastic Stack and Docker Compose](https://www.elastic.co/pt/blog/getting-started-with-the-elastic-stack-and-docker-compose).

### `docker-compose.yml`

Para executar os arquivos com o Docker Compose, é preciso um arquivo `YAML` com todas as informações e comandos dos serviços que serão criados. Os serviços são definidos com todas as configurações dos contêineres do Docker.

No caso deste projeto, o arquivo `YAML` estabelece inicialmente os volumes da aplicação, que são responsáveis por armazenar os dados gerados pelos contêineres. Em seguida, é criada uma rede nomeada `elastic` que permite a comunicação entre todos os serviços definidos, sendo eles:

* `setup`: responsável por inicializar os certificados SSL/TLS para o Elasticsearch e Kibana, além de executar uma série de comandos para garantir que o Elasticsearch esteja pronto para se conectar ao Kibana e ao programa Python.

* `es01`: serviço que executa o Elasticsearch, geralmente na porta 9200 do computador.

* `kibana`: executa o Kibana para a visualização de dados na porta 5601. Depende dos dados presentes no Elasticsearch, então esse serviço só é executado após a inicialização do contêiner `es01` .

* `app`: responsável por compilar e executar a aplicação Python que irá se comunicar com o Elasticsearch. Este sesrviço também depende que o contêiner `es01` esteja inicializado. 

### `.env`

O arquivo `.env` possui todas as variáveis de ambiente que são usadas para configurar os serviços no `docker-compose.yml`. Este arquivo é essencial para manter o código mais seguro, pois não precisa ser compartilhado, protegendo informações sensíveis como as senhas do Elasticsearch e do Kibana. Além disso, facilita a mudança de variáveis, já que essas modificações precisam ser feitas em apenas um lugar.

### `app/Dockerfile`

O `Dockerfile` é um arquivo de texto com todos os comandos para criar uma imagem Docker. Uma imagem é usada para criar e executar uma aplicação dentro de um contêiner. Neste projeto, usamos uma imagem Python para ler os dados e inseri-los no contêiner do Elasticsearch.

É possível estabelecer alguns passos dentro do `Dockerfile`:

1. Definir a imagem base Python.
2. Copiar os arquivos necessários para a imagem.
3. Instalar as dependências necessárias para executar a imagem.
4. Especificar o comando para iniciar o contêiner.

* Link para a documentação: [Dockerfile](https://docs.docker.com/reference/dockerfile/).

### `app/data.xlsx`

Este arquivo contém os dados que serão adicionados ao Elasticsearch. Ele será lido pelo código Python, que irá tratar os dados e realizar a conexão com o Elasticsearch.
  
### `app/main.py`

O `main.py` um código Python que será usado para se comunicar com o Elasticsearch. Suas principais funções são:

1. Conectar com a API do Elasticsearch.
2. Ler dos dados que seão usados.
3. Tratar dos dados.
4. Inserir os dados no Elasticsearch por meio da API.

Algumas variações do código são abordadas na parte de [Scripts Python](https://github.com/jcampolim/iniciacao-tecnologica/blob/main/docs/scripts-python.md) da documentação.
  
### `app/requirements.txt`

É o arquivo que possui todas as dependências para executar a imagem. Neste projeto, é o arquivo de dependências da aplicação Python com todas as bibliotecas necessárias para o código executar corretamente. As dependências são:

* `elasticsearch`: Elasticsearch Python Client, responsável pela conexão com o Elasticsearch. É importante que esta biblioteca esteja na mesma versão do Elasticsearch do Docker (informação presente no `.env`).
* `numpy`: usada na manipulação de grandes listas e operações matemáticas, auxiliar na leitura de dados.
* `pandas`: biblioteca para a leitura e análise de dados, capaz de ler diversos formatos de arquivo.
* `openpyxl`: biblioteca complementar ao `pandas` para a leitura de arquivos Excel.

* Link para as documentações: [Numpy](https://numpy.org/doc/), [Pandas](https://pandas.pydata.org/docs/) e [OpenPyXL](https://openpyxl.readthedocs.io/en/stable/).

### `download/download.py`

Este arquivo é opcional. Nesse projeto, os dados são armazenados em uma pasta do [Google Drive](https://drive.google.com/drive/folders/1BJVmQrSIuSqF2MDvw-xvkUuKy5Ckfdj8?usp=sharing). Porém eles não são atualizados com frequência, então não há necessidade de automatizar a coleta de dados. Dessa forma, o arquivo contém código Python simples responsável por fazer o download do arquivo, cujos dados serão encaminhados para o Elasticsearch. 

Essa etapa é realizada manualmente, antes dos contêineres serem iniciados.

Para baixar os arquivos diretamente do Google Drive, é possível usar a biblioteca `gdown`.

* Link para a documentação: [Gdwon](https://pypi.org/project/gdown/).