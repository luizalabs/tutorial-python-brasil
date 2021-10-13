# 🦸 Técnicas (um pouco) mais avançadas

## 🚱 Rate limit
### O que é ?
Rate Limit é a limitação de solicitação entre um controlador de origem e uma interface destino. No mundo de serviços web podemos dizer que Rate Limit é a limitação de requisições de um usuário (client) para uma WebAPI.

### Quando utilizar
Utiliza a estratégia de Rate Limit no ambiente de WebAPIs para evitar ataques de invasores, quando o mesmo fica explorando as vulnerabilidades de segurança do sistema para infectar e controlar máquinas e dispositivos. 

### Dicas / Links / Ferramentas
https://pypi.org/project/fastapi-limiter/
https://pypi.org/project/slowapi/

## 🔒 Autenticação e Autorização
### O que é ?
Autenticação é o processo do sistema para verificar a identidade virtual do usuário o client, normalmente baseado em um login e senha. Autorização é o processo que permite o usuário ou client acessar uma ou mais funcionalidades e recursos do sistema.

### Quando utilizar?
Colocar um processo de Autenticação na sua é WebAPI reforçar a segurança da mesma evitando que usuários maliciosos consigam acessá-la e causar algum impacto no sistema. O processo de Autorização vem na sequência, a importância de adotar esse processo é que mesmo os usuários que consigam se autenticar não necessariamente eles terão acessos às informações e recursos. Na Autorização você consegue limitar o usuário nos acessos aos recursos e os dados do sistema.

### Dicas / Links / Ferramentas
https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/
https://pypi.org/project/python-oauth2/
https://pypi.org/project/python-openid/
https://www.keycloak.org/

## 🗺️ Hateoas
### O que é ?
Hateoas (Hypermedia As the Engine Of Application State) vem da palavra Hypermedia, onde os documentos são integrados através de links. Ou seja, quando clicamos em uma frase ou imagem em um site e é o direcionado para outra página essa ação acontece de forma implicita ao usuário e utilizando hyperlink. Em WebAPIs é a capacidade de linkar recursos através de links dentro do documento json. Os clients não precisam conhecer as URLs de recursos, apenas de entrypoint. Ou seja, a API passa a fornecer links que indicarão aos clients como navegar através dos seus recursos. 

### Quando utilizar?
A utilização de Hateoas acontece quando o FrontEnd (client) não precisa ter as regras para saber consumir as API. Pois, no próprio documento json tem os atributos existentes com os possíveis links para a navegação dos próximos recursos. Isso é importante quando temos APIs abertas e os clients não conhecem as regras de negócio do server (backend). Também podemos utilizar em times grandes que trabalham provendo recursos para várias equipes através de WebAPIs. 

### Dicas / Links / Ferramentas
https://restful-api-design.readthedocs.io/en/latest/urls.html
https://pypi.org/project/ripozo/

## 📰 Log
### O que é ?
Log nada mais é que a apresentação das informações de etapas percorridas do sistema ou ações que o algorítmo executou em algum processo. Essas informações são  registros que ficam gravados em arquivos e ajudam a identificar o comportamento do sistema e até identificação de erros.

### Quando utilizar?
Sempre! Mas depende do tipo de log. Isso mesmo que você leu, depende do tipo ou o termo correto nível de log e o ambiente que a aplicação está. Na fase de desenvolvimento utiliza-se o log no nível debug, esse nível ajuda a percorrer o algorítmo com maior frequência e acompanhar em detalhes. Em ambientes de teste e de produção utiliza o log no nível de erro ou info. Esses níveis possibilitam ter os registros de erros da aplicação ou alguma informação relevante, sem poluir os registros.

### Dicas / Links / Ferramentas
https://docs.python.org/3/library/logging.html


[Referências e Dicas ➡️](referencias.md)

[⬅️ Circuit breaker](breaker.md)

[↩️ Voltar ao README ](README.md)
