# ✔️ Integração contínua

![Integração contínua](imgs/ci.jpg "Integração contínua")

## Conceito

O desenvolvedor integra o código alterado e/ou desenvolvido ao projeto principal na mesma frequência com que as funcionalidades são desenvolvidas, sendo feito muitas vezes.

Todo o nosso projeto será construído utilizando testes automatizados, e sempre rodaremos os testes localmente.

Mas como garantir que minha alteração não impacta com o restante do projeto, ter isto de forma simples e automatizada?
Como garantir que a qualidade do código foi mantida?

Utilizaremos o serviço [Github Actions](https://github.com/features/actions) para checar que nosso código não quebra a "build", ou seja, quando integrado o novo código ao sistema, todo o sistema continua funcional.

Basicamente, a grande vantagem da integração contínua está no feedback instantâneo. Isso funciona da seguinte forma: a cada commit no repositório, o build é feito automaticamente, com todos os testes sendo executados de forma automática e falhas sendo detectadas. Se algum commit não compilar ou quebrar qualquer um dos testes, a equipe toma conhecimento instantâneamente (através de email, por exemplo, indicando as falhas e o commit causador das mesmas). A equipe pode então corrigir o problema o mais rápido possível, o que é fundamental para não introduzir erros ao criar novas funcionalidades, refatorar, etc. Integração contínua é mais uma forma de trazer segurança em relação a mudanças: você pode fazer modificações sem medo, pois será avisado caso algo saia do esperado.

## Ferramentas

### 🎨 Flake8

#### O que é?

Flake8 é um programa de linha de comando que verifica seu código e busca por erros ou formatações que não seguem o guia de estilo padrão do python, conhecido como PEP-8 . Além disso também verifica a complexidade ciclamática do seu código.

#### Para que serve?

É muito comum cometermos alguns erros de sintaxe, principalmente quando ainda estamos nos familiarizando com uma linguagem nova. Assim como durante o nosso dia a dia podemos esquecer algum código não utilizado. Esta ferramenta vai analisar o seu código e procurar possíveis erros, evitando assim que só ocorram no momento em que o código for executado.
Esta ferramenta também aponta possíveis linhas que não estão seguindo o estilo de código definido para a linguagem python.
Outra coisa bem comum quando estamos escrevendo código é que uma parte dele começa a se tornar tão complexa que há n caminhos por onde seu algoritmo pode seguir. Normalmente isto indica que devemos modificar o código para torná-lo mais simples e legível. O Flake8 irá apontar qual parte do seu código está complexa e que deve ser modificada.
Esta ferramenta será integrada ao editor, dessa maneira, ao salvar o arquivo, teremos os erros encontrados apontados diretamente no mesmo.

#### Como instalar

Execute o comando abaixo:

```
poetry add flake8 --dev
```

> ℹ️ Utilizamos a opção --dev pois é um pacote necessário somente durante o desenvolvimento e não durante a execução do software.

#### Como executar

```
poetry run flake8 .
```

### 🔠 isort

#### O que é?

isort é uma ferramenta que ordena de forma alfabética as importações, separando as bilbiotecas que são padrões da linguagem, as externas ao sistema e as nativas do próprio sistema.

#### Para que serve?

O isort irá modificar o seu código ordenando as importações alfabéticamente. Dessa forma, o bloco de importações fica organizado e padronizado no projeto.

#### Como instalar

Execute o comando abaixo:

```
poetry add isort --dev
```

> ℹ️ Utilizamos a opção --dev pois é um pacote necessário somente durante o desenvolvimento e não durante a execução do software.

#### Configuração

Precisamos adicionar no arquivo `pyproject.toml` a seguinte configuração

```
[tool.isort]
profile = "black"
line_length = 79
```

#### Como executar

```
poetry run isort .
```

Assim evitamos um conflito com a ferramenta `black` e `flake8`.

### ✨ Black

#### O que é?

Black é o formatador de código Python intransigente. Ao usá-lo, você concorda em ceder o controle sobre as minúcias da formatação manual. Em troca, o black dá a você velocidade, determinismo e liberdade do irritante pycodestyle sobre formatação. Você economizará tempo e energia mental para assuntos mais importantes.

#### Para que serve?

O black é um formatador automático de código, ele irá modificar o seu código seguindo o guia de estilo do Python. Iremos configurá-lo junto ao nosso editor para que a formatação seja feita através de um atalho do teclado como shift + ctrl + i.

#### Como instalar

Execute o comando abaixo:

```
poetry add black --dev
```

> ℹ️ Utilizamos a opção --dev pois é um pacote necessário somente durante o desenvolvimento e não durante a execução do software.

#### Configuração

Precisamos adicionar no arquivo `pyproject.toml` a seguinte configuração

```
[tool.black]
line-length = 79
```

#### Como executar

```
poetry run black .
```

Assim evitamos um conflito com a ferramenta `flake8`.

### 🕵️ pre-commit (Menção honrosa 🏅) 

Existem ferramentas que podem executar algum comando antes de um commit, com o objetivo de identificar possíveis problemas no seu programa antes do envio do código para o repositório remoto. Os comandos listados acima são bons exemplos de execuções que podem ocorrer neste momento. Uma das ferramentas que provê essa funcionalidade é o pre-commit. Para saber mais, [clique aqui](https://pre-commit.com/).

## :octocat: Configurando o Github Actions

- Crie a pasta `.github/workflows` dentro do seu repositório. Essa é a pasta padrão para as configurações do Github Actions.

- Dentro da pasta crie um arquivo chamado `main.yml`. Esse arquivo será utilizado para determinar quais passos serão executados na integração. O arquivo deve possuir o seguinte conteúdo:

```yml
name: main

on: [push, pull_request]

jobs:
  linter-and-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.9
      - name: Set up poetry
        uses: abatilo/actions-poetry@v2.1.0
        with:
          poetry-version: 1.1.5

      - name: Configure poetry
        shell: bash
        run: python -m poetry config virtualenvs.in-project true

      - name: Set up cache
        uses: actions/cache@v2
        id: cache
        with:
          path: .venv
          key: venv-${{ hashFiles('**/poetry.lock') }}

      - name: Ensure cache is healthy
        if: steps.cache.outputs.cache-hit == 'true'
        shell: bash
        run: timeout 10s python -m poetry run pip --version || rm -rf .venv

      - name: Install dependencies
        shell: bash
        run: python -m poetry install

      - name: Run isort
        shell: bash
        run: python -m poetry run python -m isort --check .

      - name: Run black
        shell: bash
        run: python -m poetry run python -m black --check .
      
      - name: Run flake8
        shell: bash
        run: python -m poetry run python -m flake8 . --exclude=.venv

      - name: Run tests
        shell: bash
        run: python -m poetry run python -m pytest .
```

Através do arquivo de configuração, nós definimos que alguns passos serão executados toda vez que houver um `push` ou a abertura de um `pull request` no repositório. Os passos executados serão os seguintes:

1 - Instalar todas as dependências necessárias.

2 - Executar o isort.

3 - Executar o black.

4 - Executar o flake8.

4 - Executar os testes.

🎉 Pronto, a partir de agora, o Github Actions irá rodar todos as validações e testes do seu projeto de forma automatizada e indicará se a construção do mesmo está com problemas.

Isto será extremamente útil nos próximos passos.

## 💾 Salvando a versão atual do código

Primeiro passo é checar o que foi feito até agora:

```bash
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .github/

nothing added to commit but untracked files present (use "git add" to track)
```

Vemos uma pasta não rastreada, precisamos avisar ao controle de versão que monitore a pasta e seu conteúdo.

```
git add .github/
```

> ⚠️ Adicione também os arquivos que possivelmente foram modificados por nossas ferramentas de qualidade.

💾 Agora vamos marcar esta versão como consolidada.

```
git commit -m "Integração contínua"
```

:octocat: Por fim, envie ao github a versão atualizada do projeto.
```
git push
```

> 🐂 Uma api robusta possui evolução contínua garantindo qualidade a cada versão.

[Desafios ➡️](desafios.md)

[⬅️ Documentação](docs.md)

[↩️ Voltar ao README ](README.md)
