# Arquitetura

O projeto consiste em uma aplicação Docker com contêineres para executar o Elasticsearch e o Kibana. A aplicação também conta com um contêiner Python para criar índices no Elasticsearch e alimentá-los com os dados.

## Diagrama de arquitetura

<img src="https://github.com/jcampolim/iniciacao-tecnologica/blob/main/assets/diagrama-de-arquitetura.png" alt="Diagrama de arquitetura">

## Componentes

### Elasticsearch

O Elasticsearch é um mecanismo de busca distribuído e de código aberto, projetado para armazenar, buscar e analisar grandes volumes de dados em tempo real e de maneira eficiente. 

É muito utilizado em casos de uso como pesquisa textual, análise de logs, monitoramento de sistemas e análise de dados, oferecendo escalabilidade, flexibilidade e uma poderosa capacidade de pesquisa e indexação. É comumente empregado em ambientes empresariais para facilitar a busca e análise de dados em larga escala.

O Elasticsearch faz parte de uma pilha de softwares livres, conhecida como Elastic Stack, que tem como produtos: Elasticsearch, Kibana, Beats e Logstash. A utilização em conjunto dessas ferramentas permite a coleta de dados de maneira confiável e segura, juntamente com buscas, análises e visualizações desses dados. Neste projeto são usados apenas o Elasticsearch e o Kibana para armazenamento, buscas, análises e visualizações.

Dessa forma, da maneira que está sendo utilizado, o Elasticsearch funcionará como um banco de dados não relacional responsável por armazenar grandes quantidades de dados e realizar a busca entre esses dados.

* Versão utilizada: 8.14.0.
* Documentação: [Elasticsearch Guide](https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html).

### Kibana

O Kibana é uma interface gráfica de código aberto que pode se conectar com qualquer aplicação, desde bancos de dados até APIs e servidores. É capaz de realizar a análise de dados em larga escala de maneira eficiente e exibir os dados de maneira intuitiva. Com o Kibana, é possível elaborar tabelas, gráficos, mapas e outros tipos de visualização de maneira fácil e que não exige conhecimentos prévios de programação. Sendo uma ferramenta muito eficiete para a análise de logs e a visualização deles em tempo real.

O Kibana faz parte do Elastic Stack, então ele se conecta muito bem com o Elasticsearch, facilitando a comunicação entre eles para o desenvolvimento de dashboards personalizados.

Nesse projeto, o Kibana é usado para visualizar e analisar os dados coletados da usina solar, permitindo a criação de gráficos para exibir os dados meteorológicos e de produção de energia.

* Versão utilizada: 8.14.0.
* Documentação: [Kibana Guide](https://www.elastic.co/guide/en/kibana/current/index.html).

### Docker

O Docker uma plataforma de código aberto que facilita a criação de softwares em pacotes denominados contêineres. Esses contêineres são unidades isoladas que incluem programas, bibliotecas e arquivos de configuração necessários para a execução de cada pacote. Eles funcionam como máquinas virtuais modulares e leves, permitindo uma execução eficiente e independente para cada contêiner, otimizando o uso da infraestrutura e mantendo um ambiente seguro.

É uma ferramenta muito popular por sua portabilidade e sua escalabilidade. Os contêineres podem ser executados em qualquer sistema que suporte o Docker e é fácil criar e gerenciar múltiplos contêineres.

Para criar um ambiente com o Elasticsearch integrado ao Kibana, é possível utilizar o Docker para criar contêineres individuais. Entretanto, há algumas limitações nessa abordagem e, para criar um ambiente mais completo, uma solução é usar o Docker Compose, uma ferramenta da mesma empresa. 

Com o Compose, é possível gerenciar múltiplos contêineres de forma simples e eficaz. Ele permite que os processos de criação e inicialização do Elasticsearch e do Kibana sejam feitos automaticamente com alguns comandos simples no terminal, facilitando o acesso aos contêineres do projeto.

* Documentação: [Docker docs](https://docs.docker.com/compose/).
* Lista de comandos Docker Compose: [Docker Compose Reference](https://docs.docker.com/reference/cli/docker/compose/).