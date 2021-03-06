## Dados
O projeto visa utilizar uma tabela já existente no kaggle.com pelo link https://www.kaggle.com/nilsnoreyson/touch-sensor-events

## Atuação
Interruptores inteligentes para residências.

## Escopo
Acionamento de 3 interruptores:
* O primeiro irá ligar ou desligar o ventilador
* O segundo irá ligar ou desligar a luz
* O terceiro irá desbloquear a porta.

## Métrica
Facilidade de automação residencial.

## Planejamento
Etapas do processo:
* Escolha dos dados para iniciar a pesquisa.
* Preparação do dado
* Criação da coisa na AWS
* Envio dos dados para a AWS
* Envio e recebimento dos dados para a sombra/shadow da coisa
* Atualizar o estado da coisa a partir do recimento dos dados da AWS.

## Arquitetura
* Dado:
    - touch_events.csv 

* Tratativa:
    - Leitura do csv e envio dos dados para a AWS
    - Utilização dos dados na aws para predição e mudança de estado da `coisa`

* Serviços e Ferramentas
    - AWS para utilização dos serviços de IoT
    - Prophet para predição
    - Auto Arima para predição

## Diagrama da solução
![plot](../../assets/diagrama.png)