# Primeira execução

Na primeira execução do projeto, é necessário importar os dados e as configurações dos dashboards. Para isso, abra duas abas do terminal no diretório do projeto e siga os passos abaixo:

### 1. Importar os dados do Elasticsearch

Na primeira aba do terminal, execute o comando para iniciar um contêiner temporário:

```bash
docker run -it --name temp-container -v docker_esdata01:/volume -v $(pwd):/backup alpine
```
> [!IMPORTANT]  
> `$(pwd)` funciona no Git Bash e em máquinas Linux e MacOS. No Windows, é possível usar `${pwd}` no PowerShell e `%cd%` no CMD.

Depois de iniciar o contêiner, abra a segunda aba e execute o seguinte comando para extrair os dados para o volume do Elasticseach:

```bash
docker exec temp-container sh -c "cd /volume && tar xvf /backup/docker/backup/esdata01.tar"
```

Depois de extrair os dados, pare e remova o contêiner com os comandos abaixo:

```bash
docker stop temp-container
docker rm temp-container
```

### 2. Importar configurações dos dashboards do Kibana

Na primeira aba do terminal, repita o processo para a criação de um contêiner temporário para o Kibana:

```
docker run -it --name temp-container -v docker_kibanadata:/volume -v $(pwd):/backup alpine
```

Na segunda aba, execute o comando para extrair as configurações dos dashboards:

```bash
docker exec temp-container sh -c "cd /volume && tar xvf /backup/docker/backup/kibanadata.tar"
```

Pare e remova o contêiner temporário com:

```bash
docker stop temp-container
docker rm temp-container
```

Certifique-se de seguir os passos cuidadosamente para garantir que os dados sejam importandos corretamente.