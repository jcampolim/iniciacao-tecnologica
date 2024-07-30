# Arquitetura

O projeto consiste em uma aplicação Docker com contêineres para executar o Elasticsearch e o Kibana. A aplicação também conta com um contêiner Python para criar índices no Elasticsearch e alimentá-los com os dados.

## Diagrama de arquitetura

## Componentes

### Elasticsearch

O Elasticsearch é um mecanismo de busca distribuído e de código aberto, projetado para armazenar, buscar e analisar grandes volumes de dados em tempo real e de maneira eficiente. 

É muito utilizado em casos de uso como pesquisa textual, análise de logs, monitoramento de sistemas e análise de dados, oferecendo escalabilidade, flexibilidade e uma poderosa capacidade de pesquisa e indexação. É comumente empregado em ambientes empresariais para facilitar a busca e análise de dados em larga escala.

O Elasticsearch faz parte de uma pilha de softwares livres, conhecida como Elastic Stack, que tem como produtos: Elasticsearch, Kibana, Beats e Logstash. A utilização em conjunto dessas ferramentas permite a coleta de dados de dados de maneira confiável e segura, juntamente com buscas, análises e visualizações desses dados. Nesse projeto são usados apenas o Elasticsearch e o Kibana para armazenamento, buscas, análises e visualizações.

Dessa forma, da maneira que está sendo utilizado, o Elasticsearch funcionará como um banco de dados não relacional responsável por armazenar grandes quantidades de dados e realizar a busca entre esses dados.

* Versão utilizada: 8.14.0.
* Link para a documentação: [Elasticsearch Guide](https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html).

### Kibana

O Kibana é uma interface gráfica de código aberto que pode se conectar com qualquer aplicação, desde bancos de dados até APIs e servidores. É capaz de realizar a análise de dados em larga escala de maneira eficiente e exibir os dados de maneira intuitiva. Com o Kibana, é possível elaborar tabelas, gráficos, mapas e outros tipos de visualização de maneira fácil e que não exige conhecimentos prévios de programação. Sendo uma ferramente muito eficiete para a análise de logs e a visualização deles em tempo real.

O Kibana faz parte do Elastic Stack, então ele se conecta muito bem com o Elasticsearch, facilitando a integração com dashboards personalizados.

Nesse projeto, o Kibana é usado para visualizar e analisar os dados coletados da usina solar, permitindo a criação de gráficos para exibir os dados meteorológicos e de produção de energia.

* Versão utilizada: 8.14.0.
* Link para a documentação: [Kibana Guide](https://www.elastic.co/guide/en/kibana/current/index.html).

### Docker

O Docker uma plataforma de código aberto que visa a criação de softwares em pacotes denominados contêineres, eles são unidades isoladas que agrupam seus próprios programas, bibliotecas e arquivos de configuração.

Os contêineres funcionam como máquinas virtuais Linux modulares e leve de serem executadas. Cada máquina vitual consegue ser executada de maneira independente, otimizando o uso da infraestrutura e mantendo um ambiente seguro.

É possível criar um ambiente do Elasticsearch integrado com o Kibana usando o Docker, mas há algumas limitações nesse ambiente. Dessa forma, usamos outra ferramenta do Docker, o Docker Compose, para criar um ambiente mais completo.

* Link para a documentação: [Docker docs](https://docs.docker.com/compose/).