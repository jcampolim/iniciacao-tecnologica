# Contribuições futuras

Embora este projeto tenha sido finalizado, ainda existem muitas melhorias que podem ser feitas.

## Atualização automática dos dados

Atualmente, os dados da usina solar são atualizadosem uma pasta do [Google Drive](), porém esses dados não são atualizados com frequência, então a aplicação não busca novos dados automaticamente. Assim, o download de cada arquivo é feito manualmente para que ele seja adicionado ao Elasticsearch.

Esse processo manual pode ser facilmente automatizado. É possível criar um script Python para ser executado periodicamente que verifique a pasta do Google Drive em busca de arquivos que ainda não foram inseridos. Para manter o controle dos arquivos já inseridos, uma solução seria escrever os nomes dos arquivos lidos em um arquivo `.txt`.

A conexão do script com a pasta de arquivos pode ser feita por meio da API do Google Drive, sendo necessário criar um novo projeto no Console de Desenvolvedores Google.