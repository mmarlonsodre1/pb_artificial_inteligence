# pb_artificial_inteligence
Projeto educacional  para estudos

Estrutura do projeto:

	data:
		- raw
		- processed
		- modeling
	docs:
		- project
		- datareport
		- model
	code:
		- dataprep
		- model
		- operatinalization

Rodar projeto:
	Atualmente existe apenas um script no dataprep feito para preparar o dado bruto e transformar em um novo csv.


docker build . -t sensoraws
docker run -it sensoraws /bin/bash
python3 code/operationalization/send_data_to_aws_in.py

21/02/2022