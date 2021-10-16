# 📟 Logging

#### O que é?

[Logging](https://docs.python.org/pt-br/3/library/logging.html) é um módulo nativo do python para registrar eventos.

#### Para que serve?

O Logging fornece registro de eventos de uma forma muito flexível e funcional utilizando as seções Loggers, Handlers e Formatters que são totalmente customizados.


#### Como usar?

Primeiramente é necessário uma [configuração](https://docs.python.org/pt-br/3/library/logging.config.html) dos seus logs para definir o formato do seu log e como ele será manipulado.

Após configurar o seu log, basta instanciar uma variável que chame o método getLogger e usar os levels que forem necessários para registrar os logs.


#### Seção - Formatters

Formatters é a parte de configuração do seu log para definir como ele será mostrado. Exemplo de log:
> 2021-10-13 22:40:40,531 - [DEBUG] api_pedidos.api [1237316] [api.healthcheck:11]: Hello healthcheck!

Exemplo de uma configuração:

```python
{
  # ...
  "formatters": {
    "standard": {
      "format": (
        "%(asctime)s - [%(levelname)s] %(name)s [%(process)d] "
        "[%(module)s.%(funcName)s:%(lineno)d]: %(message)s"
      ),
    },
  }
  # ...
}
```

#### Seção - Handlers

Com os manipuladores de logs, é possível determinar se o seu log será exibido na saída padrão de seu terminal, em um arquivo rotacionado, criar integrações com outras plataformas, enviar os logs por email, etc.
Há vários tipos de [handlers](https://docs.python.org/pt-br/3/library/logging.handlers.html), mas os mais usados são:

- StreamHandler: Envia o log na saída padrão de seu terminal.
- RotatingFileHandler: Grava em um arquivo que é rotacionado de acordo com o tamanho do arquivo.
- TimedRotatingFileHandler: Grava um arquivo que é rotacionado de acordo com o intervalo de tempo passado.

E o mais legal, é que podemos aproveitar a sobreposição de métodos do python para manipular as classes e definir como queremos usar o log.

Exemplo de uma configuração:

```python
{
  # ...
  "handlers": {
    "console": {
      "level": "DEBUG",
      "class": "logging.StreamHandler",
      "formatter": "standard"
    },
    "discord": {
        "level": "ERROR",
        "class": "api_pedidos.core.logger_discord.DiscordStreamHandler",  # classe que podemos herdar por exemplo do logging.StreamHandler para enviarmos atraves de um webhook para o discord 
        "formatter": "standard"
    },
   "rotating_file": {
        "class": "logging.handlers.RotatingFileHandler",
        "filename": "info.log",
        "formatter": "standard",
        "maxBytes": 1048576,  # 1 mb
        "backupCount": 2,
        "level": "INFO",
    },
    "timed_rotating_file": {
        "class": "logging.handlers.TimedRotatingFileHandler",
        "filename": "timed_info.log",
        "formatter": "standard",
        "when": "midnight",
        "interval": 1,
        "backupCount": 2,
        "level": "WARNING",
    },
  }
  # ...
}
```

#### Seção - Loggers

Parte da configuração aonde é determinado qual log será buscado e como ele será tratado chamando um handler.

Exemplo de uma configuração:
```python
{
    # ...
    "loggers": {
        "api_pedidos.api": {
            "handlers": ["timed_rotating_file"],
            "level": "DEBUG",
        },
        "api_pedidos": {
            "handlers": ["console", "rotating_file_info"],
            "level": "DEBUG",
        },
        "api_pedidos": {
            "handlers": ["discord"],
            "level": "ERROR",
        },
    },
    # ...
}
```

#### Usando os logs

Após configurado, irá usar uma chamada parecida com esta para chamar o log em seu arquivo python:
> logger = logging.getLogger(__name__)

E registrar um log:
> logger.debug("Hello world!")

## Level dos logs

Os logs são separados em 5 levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
E estes levels respeitam esta ordem. Então se por exemplo eu seu arquivo de configuração estiver no level 'INFO', nenhum log de DEBUG será registrado.


#### Exemplo de estrutura

Então para resumir, se fossemos incluir em nosso projeto, podemos criar uma estrutura desta forma:

api_pedidos/config_logging.py
```python
import logging.config

logging.config.dictConfig(config={
    "version": 1,
    "formatters": {
        "standard": {
            "format": (
                "%(asctime)s - [%(levelname)s] %(name)s [%(process)d] "
                "[%(module)s.%(funcName)s:%(lineno)d]: %(message)s"
            ),
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "standard",
        },
    },
    "loggers": {
        "api_pedidos": {
            "handlers": ["console"],
            "level": "DEBUG",
        },
    },
})
```

api_pedidos/api.py
```python
from fastapi import FastAPI
from api_pedidos.config_logging import logging


logger = logging.getLogger(__name__)
app = FastAPI()


@app.get("/healthcheck")
async def healthcheck():
    logger.debug("Hello healthcheck!")
    return {"status": "ok"}
```

[↩️ Voltar](avancadas.md#log)