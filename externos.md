# 🤝 Integração com serviços externos

<p align="center">
  <img style="float: right;" src="imgs/login.png" alt="pessoa com computador, sentado em uma cadeira com gato próximo e uma planta"/>
</p>

Certo, temos a verificação da integridade do sistema, mas ainda temos outras funcionalidades a serem implementadas.

Nossa próxima tarefa será:

- [ ] Dado um pedido, retornar os seus itens

- [ ] Os itens de um pedido devem conter um identificador (sku), uma descrição, uma imagem, uma referência e a quantidade.

Mas antes disto, precisamos conhecer a API que iremos integrar. [Vamos explorar a API do Magalu](explorando_api.md).

> ⚠️ Como as APIs abertas do Magalu se encontram em alpha, uma autorização prévia é necessária. Por isso, você pode utilizar uma versão simulada da mesma.
> As instruções de instalação e execução se encontram no readme do [projeto](./apis-simuladas).
> Lembre-se de trocar "https://alpha.dev.magalu.com/" por "http://localhost:8080"
> A APIKEY utilizada no acesso simulado é "5734143a-595d-405d-9c97-6c198537108f".
>  Não deixe de explorar a API como demonstrado acima, mesmo que seja sua versão simulada.

## 📄 Definindo um esquema de entrada de dados e resposta

Nosso cliente deseja obter os itens de um pedido, vamos assumir então que ele possui a identificação do mesmo.

O retorno deve ser uma lista contendo a identificação e a quantidade daqueles produtos.

Iremos fazer a junção dos pacotes.

A rota para acesso desse recurso pode ser `/orders/{identificação do pedido}/items` assim temos uma entrada de dados bem definida através da url.

A identificação do pedido deve ser um uuid válido, caso isto não ocorra devemos avisar que o pedido não foi encontrado.

Nossa saída de dados será similar a apresentada abaixo:

```json
[
    {
        "sku": "229010200", 
        "description": "Kit Fraldas Huggies Turma da Mônica Supreme Care",
        "image_url": "https://a-static.mlcdn.com.br/{w}x{h}/kit-fraldas-huggies-turma-da-monica-supreme-care-tam-g-9-a-125kg-4-pacotes-com-64-unidades-cada/magazineluiza/229010200/8a99f6f5f613ef51676384884c3a10fc.jpg",
        "reference": "Tam. G 9 a 12,5kg 4 Pacotes com 64 Unidades Cada",
        "quantity": 1,
    }
]
```

Vamos escrever um esquema representando esta nossa saída de dados?

Vamos criar um arquivo `api_pedidos/esquema.py` e dentro dele vamos adicionar o seguinte conteúdo:

> ℹ️ Utilizaremos a biblioteca [pydantic](https://pydantic-docs.helpmanual.io/) para definir nosso esquema, ela já possui integração com o _FastAPI_ e é uma das mais poderosas ferramentas disponíveis no mercado.

```python
from pydantic import BaseModel


class Item(BaseModel):
    sku: str
    description: str
    image_url: str
    reference: str
    quantity: int
```

## ✍️ Escrevendo código

> Daqui pra frente sempre que ver ❌ escreva o teste mostrado e em seguida rode os testes que devem falhar.
> Logo em seguida deverá aparecer ✔️ e o trecho de código que deve ser alterado. Lembre-se de rodar os testes para garantir que estão funcionando.

Como temos bem definido que a entrada de dados deve ser um uuid válido, vamos escrever nosso primeiro teste deste _endpoint_ à partir disto.

❌

> tests/test_api.py
```python
def test_obter_itens_quando_receber_identificacao_do_pedido_invalido_um_erro_deve_ser_retornado(cliente):
    resposta = cliente.get("/orders/valor-invalido/items")
    assert resposta.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
```

✔️ 
> api_pedidos/api.py
```python
from uuid import UUID

# ...

@app.get("/orders/{identificacao_do_pedido}/items")
def listar_itens(identificacao_do_pedido: UUID):
    pass
```

A verificação de uma identificação de pedido como UUID está testada. 

Próximo passo é testar a obtenção de um pedido e em seguida seus itens.
    
❌
> tests/test_api.py
```python
def test_obter_itens_quando_identificacao_do_pedido_nao_encontrado_um_erro_deve_ser_retornado(cliente):
    resposta = cliente.get("/orders/7e290683-d67b-4f96-a940-44bef1f69d21/items")
    assert resposta.status_code == HTTPStatus.NOT_FOUND
```

>🎎 Vamos criar dublês para testar a obtenção de um pedido e seus itens, assim não precisamos realizar a requisição real por enquanto.

O dublê pode ser escrito da seguinte maneira:

```python
def duble(identificacao_do_pedido: UUID) -> list[Item]:
    raise PedidoNaoEncontradoError()
```

❌
> tests/test_api.py
```python
from uuid import UUID
from api_pedidos.esquema import Item
from api_pedidos.excecao import PedidoNaoEncontradoError
# ...

def test_obter_itens_quando_identificacao_do_pedido_nao_encontrado_um_erro_deve_ser_retornado(cliente):
    def duble(identificacao_do_pedido: UUID) -> list[Item]:
        raise PedidoNaoEncontradoError()
    resposta = cliente.get("/orders/7e290683-d67b-4f96-a940-44bef1f69d21/items")
    assert resposta.status_code == HTTPStatus.NOT_FOUND
```

Como deve ter notado, um erro acontece pois não definimos o nosso erro.

> api_pedidos/excecao.py
```python
class PedidoNaoEncontradoError(Exception):
    pass
```

Ainda não estamos utilizando nosso dublê, isso porque não temos uma função que retorne os itens  de um pedido a ser substituida.

Vamos declará-la e avisar ao endpoint para utilizá-la:

> api_pedidos/api.py
```python
from fastapi import FastAPI, Depends
from api_pedidos.esquema import Item
# ...


def recuperar_itens_por_pedido(identificacao_do_pedido: UUID) -> list[Item]:
    pass

# ...

@app.get("/orders/{identificacao_do_pedido}/items")
def listar_itens(itens: list[Item] = Depends(recuperar_itens_por_pedido)):
    return itens
```

Estamos utilizando aqui uma técnica de [injeção de dependência](https://fastapi.tiangolo.com/tutorial/dependencies/). Esta técnica vai nos permitir mudar o recuperador de itens para um dublê nos testes e também nos permite no futuro mudar a tecnologia/maneira utilizada para recuperar os itens de um pedido sem precisar modificar todos os lugares que dependem da função de recuperação de itens.

A simples definição da função já é suficiente para que possamos modificá-la posteriormente nos testes.

Vamos voltar ao nosso teste, substituir a nossa dependência e rodar novamente.

❌
> tests/test_api.py
```python
from api_pedidos.api import app, recuperar_itens_por_pedido


# ...

def test_obter_itens_quando_identificacao_do_pedido_nao_encontrado_um_erro_deve_ser_retornado(cliente):
    def duble(identificacao_do_pedido: UUID) -> list[Item]:
        raise PedidoNaoEncontradoError()
    app.dependency_overrides[recuperar_itens_por_pedido] = duble
    resposta = cliente.get("/orders/ea78b59b-885d-4e7b-9cd0-d54acadb4933/items")
    assert resposta.status_code == HTTPStatus.NOT_FOUND
```

Agora vamos preparar nosso sistema para tratar este erro.

✔️ 
> api_pedidos/api.py
```python
from api_pedidos.excecao import PedidoNaoEncontradoError
from fastapi import FastAPI, Depends, Request
from fastapi.responses import JSONResponse
from http import HTTPStatus
# ...

@app.exception_handler(PedidoNaoEncontradoError)
def tratar_erro_pedido_nao_encontrado(request: Request, exc: PedidoNaoEncontradoError):
    return JSONResponse(status_code=HTTPStatus.NOT_FOUND, content={"message": "Pedido não encontrado"})

# ...
```

Vamos fazer um teste então para quando o pedido for encontrado?

Assim teremos certeza que temos o código de status correto e a saída de dados no formato esperado.

> ⁉️ Significa, vamos verificar se nossa api está correta? Rode os testes e modifique o código se necessário.

⁉️
> tests/test_api.py
```python
def test_obter_itens_quando_encontrar_pedido_codigo_ok_deve_ser_retornado(cliente):
    def duble(identificacao_do_pedido: UUID) -> list[Item]:
        return []
    app.dependency_overrides[recuperar_itens_por_pedido] = duble
    resposta = cliente.get("/orders/7e290683-d67b-4f96-a940-44bef1f69d21/items")
    assert resposta.status_code == HTTPStatus.OK
```

⁉️
> tests/test_api.py
```python
def test_obter_itens_quando_encontrar_pedido_deve_retornar_itens(cliente):
    itens = [
        Item(sku='1', description='Item 1', image_url='http://url.com/img1', reference='ref1', quantity=1),
        Item(sku='2', description='Item 2', image_url='http://url.com/img2', reference='ref2', quantity=2),
    ]
    def duble(identificacao_do_pedido: UUID) -> list[Item]:
        return itens
    app.dependency_overrides[recuperar_itens_por_pedido] = duble
    resposta = cliente.get("/orders/7e290683-d67b-4f96-a940-44bef1f69d21/items")
    assert resposta.json() == itens
```

Neste momento o arquivo de vocês devem estar da seguinte maneira:

<details>
<summary> tests/test_api.py </summary>

```python
from http import HTTPStatus

import pytest
from api_pedidos.api import app, recuperar_itens_por_pedido
from fastapi.testclient import TestClient
from uuid import UUID
from api_pedidos.esquema import Item
from api_pedidos.excecao import PedidoNaoEncontradoError


@pytest.fixture
def cliente():
    return TestClient(app)


def test_quando_verificar_integridade_devo_ter_como_retorno_codigo_de_status_200(cliente):
    resposta = cliente.get("/healthcheck")
    assert resposta.status_code == HTTPStatus.OK


def test_quando_verificar_integridade_formato_de_retorno_deve_ser_json(cliente):
    resposta = cliente.get("/healthcheck")
    assert resposta.headers["Content-Type"] == "application/json"


def test_quando_verificar_integridade_deve_conter_informacoes(cliente):
    resposta = cliente.get("/healthcheck")
    assert resposta.json() == {
        "status": "ok",
    }


def test_obter_itens_quando_receber_identificacao_do_pedido_invalido_um_erro_deve_ser_retornado(cliente):
    resposta = cliente.get("/orders/valor-invalido/items")
    assert resposta.status_code == HTTPStatus.UNPROCESSABLE_ENTITY


def test_obter_itens_quando_identificacao_do_pedido_nao_encontrado_um_erro_deve_ser_retornado(cliente):
    def duble(identificacao_do_pedido: UUID) -> list[Item]:
        raise PedidoNaoEncontradoError()
    app.dependency_overrides[recuperar_itens_por_pedido] = duble
    resposta = cliente.get("/orders/ea78b59b-885d-4e7b-9cd0-d54acadb4933/items")
    assert resposta.status_code == HTTPStatus.NOT_FOUND


def test_obter_itens_quando_encontrar_pedido_codigo_ok_deve_ser_retornado(cliente):
    def duble(identificacao_do_pedido: UUID) -> list[Item]:
        return []
    app.dependency_overrides[recuperar_itens_por_pedido] = duble
    resposta = cliente.get("/orders/7e290683-d67b-4f96-a940-44bef1f69d21/items")
    assert resposta.status_code == HTTPStatus.OK


def test_obter_itens_quando_encontrar_pedido_deve_retornar_itens(cliente):
    itens = [
        Item(sku='1', description='Item 1', image_url='http://url.com/img1', reference='ref1', quantity=1),
        Item(sku='2', description='Item 2', image_url='http://url.com/img2', reference='ref2', quantity=2),
    ]
    def duble(identificacao_do_pedido: UUID) -> list[Item]:
        return itens
    app.dependency_overrides[recuperar_itens_por_pedido] = duble
    resposta = cliente.get("/orders/7e290683-d67b-4f96-a940-44bef1f69d21/items")
    assert resposta.json() == itens
```

</details>
<details>
<summary> api_pedidos/api.py </summary>

```python
from fastapi import FastAPI, Depends, Request
from fastapi.responses import JSONResponse
from uuid import UUID
from api_pedidos.esquema import Item
from api_pedidos.excecao import PedidoNaoEncontradoError
from http import HTTPStatus


app = FastAPI()


def recuperar_itens_por_pedido(identificacao_do_pedido: UUID) -> list[Item]:
    pass


@app.exception_handler(PedidoNaoEncontradoError)
def tratar_erro_pedido_nao_encontrado(request: Request, exc: PedidoNaoEncontradoError):
    return JSONResponse(status_code=HTTPStatus.NOT_FOUND, content={"message": "Pedido não encontrado"})


@app.get("/healthcheck")
async def healthcheck():
    return {"status": "ok"}


@app.get("/orders/{identificacao_do_pedido}/items")
def listar_itens(itens: list[Item] = Depends(recuperar_itens_por_pedido)):
    return itens
```
</details>
<details>
<summary> api_pedidos/esquema.py </summary>

```python
from pydantic import BaseModel


class Item(BaseModel):
    sku: str
    description: str
    image_url: str
    reference: str
    quantity: int
```
</details>
<details>
<summary> api_pedidos/excecao.py </summary>

```python
class PedidoNaoEncontradoError(Exception):
    pass
```
</details>

## 🧙 Refatorando o código

Um único arquivo com vários testes está começando a ficar confuso. Que tal separarmos os testes de cada _endpoint_?

> 
```python
from http import HTTPStatus

import pytest
from api_pedidos.api import app, recuperar_itens_por_pedido
from fastapi.testclient import TestClient
from uuid import UUID
from api_pedidos.esquema import Item
from api_pedidos.excecao import PedidoNaoEncontradoError

@pytest.fixture
def cliente():
    return TestClient(app)


class TestHealthCheck:
    def test_devo_ter_como_retorno_codigo_de_status_200(self, cliente):
        resposta = cliente.get("/healthcheck")
        assert resposta.status_code == HTTPStatus.OK


    def test_formato_de_retorno_deve_ser_json(self, cliente):
        resposta = cliente.get("/healthcheck")
        assert resposta.headers["Content-Type"] == "application/json"


    def test_deve_conter_informacoes(self, cliente):
        resposta = cliente.get("/healthcheck")
        assert resposta.json() == {
            "status": "ok",
        }


class TestListarPedidos:
    def test_quando_identificacao_do_pedido_invalido_um_erro_deve_ser_retornado(self, cliente):
        resposta = cliente.get("/orders/valor-invalido/items")
        assert resposta.status_code == HTTPStatus.UNPROCESSABLE_ENTITY


    def test_quando_pedido_nao_encontrado_um_erro_deve_ser_retornado(self, cliente):
        def duble(identificacao_do_pedido: UUID) -> list[Item]:
            raise PedidoNaoEncontradoError()
        app.dependency_overrides[recuperar_itens_por_pedido] = duble
        resposta = cliente.get("/orders/ea78b59b-885d-4e7b-9cd0-d54acadb4933/items")
        assert resposta.status_code == HTTPStatus.NOT_FOUND


    def test_quando_encontrar_pedido_codigo_ok_deve_ser_retornado(self, cliente):
        def duble(identificacao_do_pedido: UUID) -> list[Item]:
            return []
        app.dependency_overrides[recuperar_itens_por_pedido] = duble
        resposta = cliente.get("/orders/7e290683-d67b-4f96-a940-44bef1f69d21/items")
        assert resposta.status_code == HTTPStatus.OK

    def test_quando_encontrar_pedido_deve_retornar_itens(self, cliente):
        itens = [
            Item(sku='1', description='Item 1', image_url='http://url.com/img1', reference='ref1', quantity=1),
            Item(sku='2', description='Item 2', image_url='http://url.com/img2', reference='ref2', quantity=2),
        ]
        def duble(identificacao_do_pedido: UUID) -> list[Item]:
            return itens
        app.dependency_overrides[recuperar_itens_por_pedido] = duble
        resposta = cliente.get("/orders/7e290683-d67b-4f96-a940-44bef1f69d21/items")
        assert resposta.json() == itens
```

✨ Aproveitei a refatoração e modifiquei alguns nomes dos testes.

Agrupei os testes em classes separadas para facilitar a leitura.

Outro detalhe importante que precisamos fazer é modificar os testes para que eles sejam independentes dos outros testes. Como estamos modificando o app em alguns testes, seria interessante retornar para o estado inicial ao final do teste.

Vamos criar uma _fixture_ que configure um cenário onde a função foi modificada e ao termino retorna o app para o estado inicial.

```python
# ...

@pytest.fixture
def sobreescreve_recuperar_itens_por_pedido():
    def _sobreescreve_recuperar_itens_por_pedido(itens_ou_erro):
        def duble(identificacao_do_pedido: UUID) -> list[Item]:
            if isinstance(itens_ou_erro, Exception):
                raise itens_ou_erro
            return itens_ou_erro
        app.dependency_overrides[recuperar_itens_por_pedido] = duble
    yield _sobreescreve_recuperar_itens_por_pedido
    app.dependency_overrides.clear()

# ...

class TestListarPedidos:
    def test_quando_identificacao_do_pedido_invalido_um_erro_deve_ser_retornado(self, cliente):
        resposta = cliente.get("/orders/valor-invalido/items")
        assert resposta.status_code == HTTPStatus.UNPROCESSABLE_ENTITY


    def test_quando_pedido_nao_encontrado_um_erro_deve_ser_retornado(self, cliente, sobreescreve_recuperar_itens_por_pedido):
        sobreescreve_recuperar_itens_por_pedido(PedidoNaoEncontradoError())
        resposta = cliente.get("/orders/ea78b59b-885d-4e7b-9cd0-d54acadb4933/items")
        assert resposta.status_code == HTTPStatus.NOT_FOUND


    def test_quando_encontrar_pedido_codigo_ok_deve_ser_retornado(self, cliente, sobreescreve_recuperar_itens_por_pedido):
        sobreescreve_recuperar_itens_por_pedido([])
        resposta = cliente.get("/orders/7e290683-d67b-4f96-a940-44bef1f69d21/items")
        assert resposta.status_code == HTTPStatus.OK

    def test_quando_encontrar_pedido_deve_retornar_itens(self, cliente, sobreescreve_recuperar_itens_por_pedido):
        itens = [
            Item(sku='1', description='Item 1', image_url='http://url.com/img1', reference='ref1', quantity=1),
            Item(sku='2', description='Item 2', image_url='http://url.com/img2', reference='ref2', quantity=2),
        ]
        sobreescreve_recuperar_itens_por_pedido(itens)
        resposta = cliente.get("/orders/7e290683-d67b-4f96-a940-44bef1f69d21/items")
        assert resposta.json() == itens
```
Embora a fixture seja um pouco mais complexa, os testes ficam mais simples e garantimos que a sobrescrita não propague entre os testes.

## 🔗 Integrando a API do Magalu


> ⚠️ Como as APIs abertas do Magalu se encontram em alpha, uma autorização prévia é necessária. Por isso, você pode utilizar uma versão simulada da mesma.
> As instruções de instalação e execução se encontram no readme do [projeto](./apis-simuladas).
> Lembre-se de trocar "https://alpha.dev.magalu.com/" por "http://localhost:8080"
> A APIKEY utilizada no acesso simulado é "5734143a-595d-405d-9c97-6c198537108f".

Vamos iniciar um pouquinho diferente dessa vez, vamos parar a programação guiada por testes e explorar a solução. Depois fica como exercício do leitor escrever estes testes.

> 💁 Uma dica muito importante é a utilização de marcas nestes testes indicando que eles são lentos.
> Visto a dificuldade de simular a falha de conexão com o servidor, normalmente os testes deste tipo se resumem a caminhos felizes ou críticos.
> Para marcar um teste como lento adicione acima dele `@pytest.mark.slow` ou adicione a seguinte linha no módulo `pytestmark = slow`.
> Para evitar a execução destes testes utilize `pytest -m "not slow"`
> Mais informações em https://docs.pytest.org/en/latest/example/markers.html

Vamos olhar o código de integração com a API do Magalu. Este arquivo deve ser criado com o seguinte conteúdo.

> api_pedidos/magalu_api.py

```python
from http import HTTPStatus
import os
from uuid import UUID
from api_pedidos.esquema import Item
from api_pedidos.excecao import PedidoNaoEncontradoError, FalhaDeComunicacaoError

import httpx

# tenant e apikey fixos somente para demonstrações
APIKEY = os.environ.get("APIKEY", "coloque aqui sua apikey")
TENANT_ID = os.environ.get("TENANT_ID", "21fea73c-e244-497a-8540-be0d3c583596")
MAGALU_API_URL = "https://alpha.api.magalu.com"
MAESTRO_SERVICE_URL = f"{MAGALU_API_URL}/maestro/v1"

def _recupera_itens_por_pacote(uuid_do_pedido, uuid_do_pacote):
    response = httpx.get(
        f"{MAESTRO_SERVICE_URL}/orders/{uuid_do_pedido}/packages/{uuid_do_pacote}/items",
        headers={"X-Api-Key": APIKEY, "X-Tenant-Id": TENANT_ID},
    )
    response.raise_for_status()
    return [
        Item(
            sku=item["product"]["code"],
            # campos que utilizam a função get são opicionais
            description=item["product"].get("description", ""),
            image_url=item["product"].get("image_url", ""),
            reference=item["product"].get("reference", ""),
            quantity=item["quantity"],
        )
        for item in response.json()
    ]


def recuperar_itens_por_pedido(identificacao_do_pedido: UUID) -> list[Item]:
    try:
        response = httpx.get(
            f"{MAESTRO_SERVICE_URL}/orders/{identificacao_do_pedido}",
            headers={"X-Api-Key": APIKEY, "X-Tenant-Id": TENANT_ID},
        )
        response.raise_for_status()
        pacotes = response.json()["packages"]
        itens = []
        for pacote in pacotes:
            itens.extend(
                _recupera_itens_por_pacote(identificacao_do_pedido, pacote["uuid"])
            )
        return itens
    except httpx.HTTPStatusError as exc:
        # aqui poderiam ser tratados outros erros como autenticação
        if exc.response.status_code == HTTPStatus.NOT_FOUND:
            raise PedidoNaoEncontradoError() from exc
        raise exc
    except httpx.HTTPError as exc:
        raise FalhaDeComunicacaoError() from exc
```

> 💁 Uma ferramenta muito interessante para testar nosso código sem precisar fazer as chamadas reais a todo momento é o [vcrpy](https://github.com/kevin1024/vcrpy). Ele grava as respostas das requisições uma única vez e depois faz a simulação das chamadas.

Leia o código e entenda o que está acontecendo.

Uma coisa interessante apareceu durante o desenvolvimento deste código. Erros de comunicação com o servidor remoto precisam ser tratados.

Vamos adicionar um teste para isto.

❌
> tests/test_api.py
```python
from api_pedidos.excecao import PedidoNaoEncontradoError, FalhaDeComunicacaoError


# ...

    # ... classe de testes ...
    def test_quando_fonte_de_pedidos_falha_um_erro_deve_ser_retornado(self, cliente, sobreescreve_recuperar_itens_por_pedido):
        sobreescreve_recuperar_itens_por_pedido(FalhaDeComunicacaoError())
        resposta = cliente.get("/orders/ea78b59b-885d-4e7b-9cd0-d54acadb4933/items")
        assert resposta.status_code == HTTPStatus.BAD_GATEWAY
```

✔️ 
> api_pedidos/excecao.py

```python
# ...


class FalhaDeComunicacaoError(Exception):
    pass
```

✔️ 
> api_pedidos/api.py

```python
from api_pedidos.excecao import PedidoNaoEncontradoError, FalhaDeComunicacaoError
# ...
@app.exception_handler(FalhaDeComunicacaoError)
def tratar_erro_falha_de_comunicacao(request: Request, exc: FalhaDeComunicacaoError):
    return JSONResponse(status_code=HTTPStatus.BAD_GATEWAY, content={"message": "Falha de comunicação com o servidor remoto"})
# ...
```

Ufa! Agora podemos testar a nossa api.

Substitua a função (`recuperar_itens_por_pedido`) criada anteriormente pela nossa  nova função e vamos testar manualmente nossa api.

## 🔧 Testando manualmente

A nossa aplicação pode estar ainda rodando, mas caso não esteja vamos inicia-la.

O comando para isto é `uvicorn --reload api_pedidos.api:app`.

Vamos testar alguns cenários?

O que acontece se passar um valor qualquer ao invés de um uuid válido?

`http :8000/orders/invalido/items`

E um pedido que não existe?

`http :8000/orders/e3ae3598-8034-4374-8eed-bdca8c31d5a0/items`

Por fim vamos ver um pedido que existe.

`http :8000/orders/efb77dcf-d83c-4935-81ac-7be5f37e6cdc/items`

Você pode testar a falha do servidor remoto modificando a url no arquivo `api_pedidos/magalu_api.py`.

## 💾 Salvando a versão atual do código

Com tudo terminado, vamos salvar a versão atual do código.

Primeiro passo é checar o que foi feito até agora:

```bash
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   api_pedidos/api.py
        modified:   tests/test_api.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        api_pedidos/esquema.py
        api_pedidos/excecao.py
        api_pedidos/magalu_api.py

no changes added to commit (use "git add" and/or "git commit -a")
```

Vamos adicionar ao versionamento os arquivos novos e avisar modificações em alguns já existentes.

`git add api_pedidos tests`

💾 Agora vamos consolidar uma nova versão.

`git commit -m "Adiciona listagem de itens em um pedido"`

:octocat: Por fim envie ao github a versão atualizada do projeto.

`git push`

Podemos marcar como pronto as seguintes tarefas:

- [x] Dado um pedido, retornar os seus itens

- [x] Os itens de um pedido devem conter um identificador (sku), uma descrição, uma imagem, uma referência e a quantidade.

> 🐂 Uma API robusta possui uma entrada de dados e resposta bem definida, facilitando assim integração com outros sistemas.

[Documentação ➡️](docs.md)

[⬅️ Olá API](ola_api.md)

[↩️ Voltar ao README ](README.md)
