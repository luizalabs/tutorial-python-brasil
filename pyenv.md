### 🏭 Pyenv

#### O que é?

[Pyenv](https://github.com/pyenv/pyenv) é um ambiente de desenvolvimento de software que permite ao usuário escolher qual versão do python que deseja utilizar.

#### Para que serve?

O pyenv é uma ferramenta que nos ajuda a gerenciar múltiplas versões de python instaladas na mesma máquina e ajuda a não ter problemas com versões incompatíveis entre si.

#### Como instalar?

O pyenv pode ser baixado como um repositório no github:

```bash
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
```

Inclua no final do seu arquivo de configuração do bash ou similar (.bashrc, .zshrc, etc) o seguinte:

```
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"
```

Reinicie seu shell para que as mudanças tenham efeito

```
exec $SHELL
```

#### Vamos verificar se deu tudo certo?

Abra um terminal e digite:

`pyenv --version`

A saída deverá ser similar a apresentada abaixo:

```
pyenv 2.0.7-32-gc81a2810
```

#### Como usar?

> ℹ️ É recomendado antes de instalar uma versão que se instale as dependências do python de acordo com o sistema operacional
> https://github.com/pyenv/pyenv/wiki#suggested-build-environment

Para instalar uma versão específica do python basta digitar:

```
pyenv install <versão>
```

Para definir aquela versão como padrão basta digitar:

```
pyenv global <versão>
```

ou caso queira definir somente para um projeto:

```
pyenv local <versão>
```

Para verificar as versões instaladas:

```
pyenv versions
```

[↩️ Voltar](ferramentas.md)