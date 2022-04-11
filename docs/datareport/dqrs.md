# Report da qualidade dos dados

É feita uma preparação dos dados antes de enviarmos para a AWS.
* Transformação de data para o formato (YYYY-mm-dd HH-MM-SS)
* Retirar a Coluna `event`.
* Atualização da coluna `class` para `int`

A preparação dos dados é feita pelo arquivo `code/dataprep/prep.py`
