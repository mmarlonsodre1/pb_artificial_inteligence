# Operação

Aqui estão guardados os certificados da `coisa`.
Aqui estão presentes os códigos de operação da `coisa`.

`send_data_to_aws.py` -> Envio dos dados `data/processed/touch_events.csv` para o tópico `touch/events` na aws.

`public_shadow_data_to_aws.py` -> Envio dos dados `data/processed/touch_events.csv` para a sombra/shadow da coisa `touch` na aws.

`subscribe_shadow_data_to_aws.py` -> Escuta a mudança de estado da coisa `touch` pela sombra/shadow e executa a ação desejada.