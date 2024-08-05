# Configuração de ambiente

Neste projeto, nosso objetivo final é criar um ambiente Docker integrado com Elasticsearch e Kibana. A seguir, estão as instruções detalhadas para configurar este ambiente.

## Instalação do Docker

Primeiro, é necessário instalar o Docker na máquina que executará o projeto. A maneira mais fácil de fazer isso é utilizando o Docker Desktop, que está disponível para Windows, macOS e Linux. O Docker Desktop inclui o Docker Engine e o Docker Compose, além de fornecer suporte para contêineres Linux em sistemas Windows e macOS.

Para instalar o Docker Desktop, acesse o link: [Docker Desktop](https://www.docker.com/products/docker-desktop/).

Para máquinas Linux, a instalação pode ser feita diretamente via terminal, sendo uma instalação mais direcionada, apenas com os pacotes necessários:

```
## Instalação do Docker Engine:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

## Instalação do Docker Compose:
sudo apt-get update
sudo apt-get install docker-compose-plugin
```

* Documentação Docker Engine: [Docker Engine Installation for Linux](https://docs.docker.com/engine/install/ubuntu/).
* Documentação Docker Compose: [Docker Compose Installation for Linux](https://docs.docker.com/compose/install/linux/).

## Instalação do Elasticsearch e do Kibana

O Elasticsearch e o Kibana também precisam ser instalados para serem executados. Porém, a instalação será feita dentro dos contêineres do Docker Compose, simplificando a configuração e gestão dessas ferramentas.

Caso o objetivo não seja executar um ambiente Docker, é possível instalar o Elasticsearch e o Kibana localmente. A seguir estão os links para a instalação manual:

* Link para instalação do Elasticsearch: [Installing Elasticsearch](https://www.elastic.co/guide/en/elasticsearch/reference/8.14/install-elasticsearch.html).
* Link para instalação do Kibana: [Install Kibana](https://www.elastic.co/guide/en/kibana/8.14/install.html).

Para mais detalhes da instalação é possível consultar esse guia de instalação no Windows: [Instalação no Windows](https://github.com/jcampolim/wtt-elasticsearch/blob/main/instalacao-windows.md). Embora, o guia seja direcionado para o Windows, os passos são semelhantes para os outros sistemas operacionais.