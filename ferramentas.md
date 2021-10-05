# 🧰 Escolhendo as melhores ferramentas

<p align="center">
  <img style="float: right;" src="imgs/ferramentas.png" alt="Ferramentas sob a mesa"/>
</p>

## 🛠️ Ferramentas

Assim como um carpinteiro, eletricista, o programador precisa de ferramentas para trabalhar. E boas ferramentas ajudam a desempenhar melhor o seu trabalho.

Escolher as melhores ferramentas faz parte do seu trabalho.

> Para quem tem um martelo, todo parafuso é prego.

Para o tutorial foram escolhidas ferramentas pensando na didática da pessoa desenvolvedora assim como compatibilidade de sistemas operacionais e também por serem as principais escolhas no mercado de trabalho.

Para garantir o acompanhamento do tutorial, verifique se as ferramentas apresentadas a seguir estão instaladas e funcionando.

### 🐍 Python

> ⚠️ É necessário versão igual ou acima da versão 3.6.2 para acompanhar o curso.

#### O que é?

Python é uma linguagem de programação com foco em legibilidade e produtividade, criada para escrever código bom e fácil de manter de maneira rápida.

#### Para que serve?

É uma linguagem bastante versátil, e hoje em dia é amplamente utilizada para escrever sistemas web, integrações entre sistemas, ciência de dados, automatizar tarefas e muitas outras coisas

#### Como instalar?

Versões mais recentes do sistema operacional linux já possuem  o python em sua versão 3 instalado.

Para usuários de Mac ou Windows vocês podem seguir os seguintes tutoriais respectivamente:

[Instalando o Python no Windows](https://github.com/cassiobotaro/do_zero_a_implantacao/blob/master/ferramentas_windows.md#snake-python)

[Instalando o Python no Mac](https://github.com/cassiobotaro/do_zero_a_implantacao/blob/master/ferramentas_mac.md#snake-python)

#### Vamos verificar se deu tudo certo?

Abra um terminal e digite:

```
python --version
```

A saída deverá ser similar a apresentada abaixo:

```
Python 3.10.0
```

### 🏭 Pyenv (não obrigatório)

Algumas vezes a versão do python do sistema operacional se torna obsoleta ou o projeto que está trabalhando é incompatível com a versão do python do sistema operacional.

Existe uma ferramenta que nos ajuda a resolver este problema, gerenciando diferentes instalações do python no sistema operacional.

Se quiser utiliza-la, siga este [guia](pyenv.md).

> ℹ️ Esta ferramenta não é necessária neste tutorial mas pode ser bem útil no seu dia a dia.

### 📦 Poetry

#### O que é?

Poetry é uma ferramenta de gerenciamento de dependências do python. Auxilia na instalação de pacotes e ajuda na configuração do ambiente de desenvolvimento.

#### Para que serve?

Utilizaremos o poetry para controlar a versão das bibliotecas utilizadas para desenvolvimento do sistema. Com ele podemos baixar uma versão específica de uma biblioteca ou facilmente atualizar suas dependências.

Ele também nos ajuda a manter um ambiente isolado de desenvolvimento entre pacotes e dependências.

O poetry nos ajuda a ter um ambiente separado para cada projeto.

#### Como instalar?

Abra um terminal e digite:

```
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```

Existem [outras](https://python-poetry.org/docs/#alternative-installation-methods-not-recommended) opções de instalação mas esta é a mais recomendada.

#### Vamos verificar se deu tudo certo?

Abra um terminal e digite:

```
poetry --version
```

A saída deverá ser similar a apresentada abaixo:

```
Poetry version 1.1.11
```

### :octocat: Git

[Git](https://git-scm.com/) é um controle de versão livre e de código aberto, construido para lidar com projetos pequenos e grandes de maneira rápida e eficiente.

**Para que serve?**

Com certeza você já escreveu um arquivo, mais tarde trocou algumas coisas e e no fim salvou com o nome `versao_final.doc`. Mais tarde ou no outro dia você decide fazer mais mudanças e chama de `agoravai.doc` e quando menos percebe já tem um monte de arquivos e talvez nem se lembre mais qual a ultima versão.

É para gerenciar alterações feitas no projeto durante o tempo que serve esta ferramenta. Durante o curso vamos salvando cada progresso feito sem precisar de ter várias cópias do mesmo arquivo.

**Como instalar**

É possivel encontrar instruções de instalação para cada um dos sistemas operacionais mais utilizados:

[Mac](https://git-scm.com/download/mac)

[Linux](https://git-scm.com/download/linux)

[Windows](https://git-scm.com/download/windows)

**Vamos verificar se deu tudo certo?**

Abra um terminal e digite `git --version`.

A saída deverá ser similar a apresentada abaixo:

```bash
$ git --version
git version 2.33.0
```

### ⌨️ VS Code

#### O que é?

O [VSCode](https://code.visualstudio.com) é um editor de texto e possui uma excelente extensão para Python que pode ser instalada através da [marketplace](https://marketplace.visualstudio.com/items?itemName=ms-python.python).

#### Para que serve?

O _plugin_ de Python para VSCode fornece _auto-complete_ , integração com os _linters_ mais conhecidos, também é uma ferramenta para depuração de código.

#### Como instalar?

O VS Code pode ser baixado no site oficial [aqui](https://code.visualstudio.com/download).

A instalação do _ plugin_ de Python pode ser feita através da marketplace ou através dos comandos abaixo: 

Abra o VS Code Quick Open (Ctrl+P) , cole o comando a seguir e pressione enter .

```
ext install ms-python.python
```

#### Vamos verificar se deu tudo certo?

Você pode abrir o VS Code e verificar se o plugin foi instalado com sucesso.

---

🎉  Parabéns! Instalamos todas as ferramentas que precisaremos para acompanhar este curso, vamos para o próximo passo!


[Iniciando o projeto ➡️](projeto.md)

[⬅️ Planejando o que será desenvolvido](planejando.md)

[↩️ Voltar ao README ](README.md)