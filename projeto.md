# 📐 Iniciando o projeto

<p align="center">
  <img style="float: right;" src="imgs/planta.png" alt="capacete amarelo e ferramentas de desenho sobre a planta de uma construção"/>
</p>

O primeiro passo para a construção do nosso projeto é iniciar seu repositório e adicionar suas dependências.

Faremos isto utilizando o [Github](https://github.com/), que é uma plataforma gratuita, muito conhecida e que irá nos ajudar com algumas integrações no futuro.

Mas por que iniciaremos criando o projeto lá e não no próprio computador?

Queremos contar desde o início do projeto com uma cópia remota, garantindo assim que nosso trabalho não será perdido e que estará compartilhado. A cada passo dado vamos consolidando o que temos no momento.

## 🚧 Começando a tirar do papel o projeto

Abra seu navegador, e acesse o seguinte [endereço](http://github.com). Crie uma conta se ainda não tiver.

Aperte o botão novo_repositório.

![novo repositório](imgs/novo_repositorio.png " Novo repositório")

Preencha os campos como visto na imagem abaixo.

![novo repositório](imgs/novorepo.png "Novo repositório")

Agora faça um "clone" do seu repositório.

```bash
git clone https://github.com/cassiobotaro/tutorial-pybr.git
```

`git clone` é um comando para criar uma cópia dos arquivos e suas versões. Pode ser feito para trazer uma cópia do repositório do servidor para o computador local.

> ⚠️ Os comandos abaixo devem ser modificados com seu email e nome de usuário do github. USUARIO deve ser modificado para seu usuário do github e EMAIL substituido pelo email utilizado no github.

```bash
$ git config --local user.email EMAIL

$ git config --local user.name USUARIO
```

"Voilà", já temos o projeto iniciado.

Navegue até o diretório onde foi executado o comando de `clone` do projeto. Prossiga com a instalação das bibliotecas que serão utilizadas no projeto.

## 📏 Iniciando um projeto Python

Agora com o repositório criado, vamos começar a criar um projeto Python.

Execute o comando:

```
poetry init -n
```

> ℹ️ A opção -n evita que o poetry fique perguntando algumas opções do projeto. Considere remove-la em próximos projetos.

Este comando iniciliza um arquivo `pyproject.toml` de configuração do projeto.

Com o projeto iniciado, vamos instalar as dependências.

## 📚 Bibliotecas e utilitários

Chegou a hora de instalar algumas bibliotecas e utilitários que nos auxiliarão na criação do nosso sistema web, na realização de testes unitários e testes manuais.

> 🖥️ O ambiente virtual

> Como estamos utilizando o poetry, todas as bibliotecas serão instaladas em um ambiente virtual isolado, exclusivo para este projeto. Na primeira vez que o comando add for utilizado, o ambiente virtual será criado.
> Veja mais detalhes sobre ambientes virtuais [aqui](ambientes_virtuais.md).

### ⚡ FastAPI

#### O que é?

O [fastapi](https://fastapi.tiangolo.com) é uma ferramenta para desenvolvimento web, possui alta performance, fácil de aprender, rápida para escrever código e pronta para colocar o código no ar.

#### Para que serve?

Serve para escrevermos nossa aplicação web de forma rápida e customizável.

Possui funções que auxiliam operações como roteamento, tratamento de requisições, renderização de conteúdo, gerenciamento de sessão e cookies, assim como várias outras que são típicas da web.

#### Como instalar?

Execute o comando:

```
poetry add fastapi
```

#### Vamos verificar se deu tudo certo?

Execute 

```
poetry run python -c "import fastapi"
```
Nenhum erro deve ocorrer.

### 🦋 Httpx

#### O que é?

[Httpx](https://www.python-httpx.org/) é um cliente HTTP completo, com suporte ao protocolo HTTP/2 e provê interface de programação síncrona e assíncrona.

#### Para que serve?

Utilizaremos para fazer a integração com serviços externos. Suas funções facilitam a criação de requisições HTTP.

#### Como instalar?

Execute o comando:

```
poetry add httpx
```

#### Vamos verificar se deu tudo certo?
Execute o seguinte comando:

```
poetry run python -c "import httpx"
```
Nenhum erro deve ocorrer.

### 🔗 Httpie

#### O que é?

[HTTPie](https://github.com/jakubroztocil/httpie) é um cliente HTTP por linha de comando. Seu objetivo é transformar a interação com serviços web o mais humano possível.

#### Para que serve?

Diversos momentos do curso, teremos de testar manualmente se nosso sistema está funcionando, ainda que possua testes automatizados.

Também será utilizado para explorar as API's que iremos integrar.

Esta ferramenta ajuda a fazer estes testes de uma maneira mais simples.

#### Como instalar?

Execute o comando:

```
poetry add httpie --dev
```

> ℹ️ Utilizamos a opção --dev pois o httpie é um pacote necessário somente durante o desenvolvimento e não durante a execução do software.

#### Vamos verificar se deu tudo certo?
Execute o seguinte comando:

```bash
poetry run http --version
```
> ℹ️ O comando é http e não httpie.

A saída deve ser similar a:

```
2.5.0
```

### 🦄 Uvicorn

#### O que é?

O uvicorn é um servidor de aplicação com suporte a frameworks assíncronos.

#### Para que serve?

O uvicorn serve para rodar a nossa aplicação, tanto na nossa máquina quanto em um servidor na internet.

#### Como instalar?

Execute o comando:

```
poetry add uvicorn
```

#### Vamos verificar se deu tudo certo?

Execute o seguinte comando:

```bash
poetry run uvicorn --version
```

A saída deve ser similar a:

```
Running uvicorn 0.15.0 with CPython 3.9.7 on Linux
```

### 🚦 Pytest

#### O que é?

O framework [pytest](https://docs.pytest.org/en/latest/) é fácil para escrever teste simples, ainda escala para suportar testes funcionais complexos para aplicações e bibliotecas.

#### Para que serve?

Já dizia Michael C. Feathers, "Um código sem testes, é um código ruim. Não importa quão bem ele foi escrito".  Vamos então instalar o pytest, que é uma ferramenta que auxilia na execução de testes.

#### Como instalar?

Execute o comando:

```
poetry add pytest --dev
```

> ℹ️ Utilizamos a opção --dev pois o pytest é um pacote necessário somente durante o desenvolvimento e não durante a execução do software.

#### Vamos verificar se deu tudo certo?

Execute o seguinte comando:

```
poetry run pytest --version
```

A saída deve ser similar a:

```
pytest 6.2.5
```

## 💾 Salvando o momento atual do nosso projeto

Neste momento seu diretório deve estar assim:

```
.
├── LICENSE
├── poetry.lock
├── pyproject.toml
└── README.md
```

Instalado as dependências, vamos consolidar uma primeira versão do nosso projeto com o nosso andamento?

Primeiro passo é checar o que foi feito até agora:

```bash
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	poetry.lock
	pyproject.toml

nothing added to commit but untracked files present (use "git add" to track)
```

Vemos dois arquivos não rastreados, precisamos avisar ao controle de versão que monitore estes arquivos.

`git add pyproject.toml poetry.lock`

💾 Agora vamos marcar esta versão como consolidada.

`git commit -m "Adiciona as dependências do projeto"`

:octocat: Por fim, envie ao github a versão atualizada do projeto.

`git push`

🍰 Entusiasmados a começar a escrever sua aplicação? Agora que temos todo o ambiente configurado, já estamos bem próximo disso. Vamos ao próximo passo!

[Olá API ➡️](ola_api.md)

[⬅️ Escolhendo as melhores ferramentas](ferramentas.md)

[↩️ Voltar ao README ](README.md)
