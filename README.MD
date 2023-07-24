# Projeto de mentoria - Victor - Patrick

Este projeto se trata de uma API capaz de armazenar produtos, exibir produtos cadastrados, realizar pesquisa por um produto, atualizar preços e deletar produtos.

## Executando a API
> `python main.py`

## Testes unitários
### Para executar todos os testes:
> `python -m unittest`

onde a opção -m é usada para executar um módulo como um script.

O Python suporta a execução de módulos diretamente da linha de comando usando a opção -m. Quando você usa -m seguido pelo nome de um módulo, o interpretador Python executa esse módulo como se fosse um script.


### Para executar um único teste unitário:
> `python -m unittest -k test_stocks_in_data_base_when_receive_two_results`

onde -k significa "keyword" (palavra-chave)

### Para medir a cobertura de testes usando o coverage

Instale o coverage:
> `pip install coverage` 

Execute os testes usando o coverage:
> `coverage run -m unittest discover`

ou

> `coverage run -m unittest`

Para relatar os resultados:

> `coverage report`

Para uma apresentação de resultados mais elaborada, com detalhamento das linhas não cobertas, execute:

> `coverage html`