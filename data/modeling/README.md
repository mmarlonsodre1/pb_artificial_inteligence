# Dados para o modelo de predição

Etapas na aws para recuperar os dados:
* Criar uma coisa junto com todas as suas regras .
* Baixar os certificados necessários e atualizar os já existentes que estão no caminho `code/operationalization/certs`.
* Criar um channel
* Criar um datastore
* Criar um pipeline
* Criar um dataset
* Rodar o arquivo `send_data_to_aws.py` que está em `code/operationalization`
* Baixar os dados do dataset e colocar na pasta `data/modeling` com o nome `data_model.csv`