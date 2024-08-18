# Elasticsearch: uma plataforma para monitoramento de sinais

> Autores: Júlia Campolim de Oste e Rogério de Oliveira

<img src="https://github.com/jcampolim/iniciacao-tecnologica/blob/main/assets/subsistemas.png" alt="Dashboard de subsistemas feito com o Kibana">

Este projeto foi desenvolvido como parte de uma iniciação tecnológica para monitorar os dados de uma usina solar localizada no campus Higienopólis da Universidade Presbiteriana Mackenzie.

Para atingir esse objetivo, foi criada uma aplicação Docker com três contêineres principais: Elasticsearch, Kibana e Python. 

Os dados são coletados a partir de uma pasta do [Google Drive](https://drive.google.com/drive/folders/1BJVmQrSIuSqF2MDvw-xvkUuKy5Ckfdj8?usp=drive_link), são processados e utilizados na construção de painéis de visualização.

A usina solar coleta três tipos principais de dados: inversores, subsistemas e meteorológicos. 

* <strong>Dados de inversores:</strong> contêm informações de nível técnico sobre o desempenho dos painéis solares.

* <strong>Dados de subsistemas:</strong> são divididos em três categorias (com otimizador, sem otimizador e parcial). A análise desses dados têm como objetivo avaliar a eficácia do otimizador, que, até o momento, não demonstrou resultados positivos.

* <strong>Dados meteorológicos:</strong> informações climáticas, que podem ser correlacionadas com a produção de energia dos painéis solares.

Durante a minha tragetória, eu tive a oportunidade de ministrar uma oficina introdutória de Elasticsearch e Kibana em um workshop do Mackenzie. Nessa apresentação, eu abordei conceitos básicos do Elastic Stack e propus uma dinâmica para cada parcipante criar alguns gráficos a partir de dados meteorológicos separados previamente.

* Material teórico da oficina: [Elasticsearch](https://github.com/jcampolim/wtt-elasticsearch).

### Como executar

<strong>Pré-requisito:</strong> possuir o docker instalado na máquina que irá hospedar o projeto. Mais detalhes em: [Configuração de ambiente](https://github.com/jcampolim/iniciacao-tecnologica/blob/main/docs/configuracao-de-ambiente.md).

Para iniciar o projeto, basta executar `docker-compose up` no terminal. 

Entretanto, na primeira vez executando, é preciso importar os dados e as configurações de ambiente, este processo está detalhado em: [Primeira execução](https://github.com/jcampolim/iniciacao-tecnologica/blob/main/docs/configuracao-de-ambiente.md).

### Documentação

- [Arquitetura](https://github.com/jcampolim/iniciacao-tecnologica/blob/main/docs/arquitetura.md);
- [Configuração de ambiente](https://github.com/jcampolim/iniciacao-tecnologica/blob/main/docs/configuracao-de-ambiente.md);
- [Contribuições futuras](https://github.com/jcampolim/iniciacao-tecnologica/blob/main/docs/contribuicoes-futuras.md);
- [Dashboards](https://github.com/jcampolim/iniciacao-tecnologica/blob/main/docs/dashboards.md);
- [Estrutura de arquivos](https://github.com/jcampolim/iniciacao-tecnologica/blob/main/docs/estrutura-de-arquivos.md);
- [Scripts Python](https://github.com/jcampolim/iniciacao-tecnologica/blob/main/docs/scripts-python.md);

### Agradecimentos 

Agradeço ao meu orientador, professor Rogério de Oliveira, por todo apoio durante esta jornada e à Universidade Presbiteriana Mackenzie pela oportunidade.
