O `data/raw/touch_events.csv` vem com 3 tabelas já completas de dados (doc_created_utc_milli, event, class), porém só irei utilizar duas (doc_created_utc_milli e class):

* doc_created_utc_milli -> data e horário do evento. (String)
* event -> Lista de Eventos (List<Float>)
* class -> tipo de evento : (String)

Após o preparo dados dados fica:
* time -> data e horário do evento. (String)
* class -> Tipo de evento: (Int)
	- Interruptor 1 = 0
	- Interruptor 2 = 1
	- Interruptor 3 = 2

Após o envio dados para a aws fica:
* ds -> data e horário do evento. (String)
* y -> Tipo de evento (Int)