# Fake Catalog

Projeto auxiliar para tutorial da pybr 2021

## Dependencias

- python 3.6+
- poetry


## Instalação

```bash
poetry install
```

## Configurações

| ENVVAR | Descrição | Valor padrão |
| ------ | --------- | ------------ |
| `FAIL_RATE` | Valor de 0 à 100 referente a taxa (%) de falha esperada | 0 |


## Execução

```bash
poetry run uvicorn main:app
```
