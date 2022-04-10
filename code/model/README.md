# Modelos de predição
Aqui existem dois modelos de predição (Prophet e Auto Arima)

Para realizar a predição, antes é necessário recuperar os dados da seguinte forma na aws:
* Criar uma coisa junto com todas as suas regras .
* Baixar os certificados necessários e atualizar os já existentes que estão no caminho `code/operationalization/certs`.
* Criar um channel
* Criar um datastore
* Criar um pipeline
* Criar um dataset
* Rodar o arquivo `send_data_to_aws.py` que está em `code/operationalization`
* Baixar os dados do dataset e colocar na pasta `data/modeling` com o nome `data_model.csv`

Após as etapas, só rodar qualquer modelo de predição que os mesmos retornarão a predição dos próximos 30 eventos.

