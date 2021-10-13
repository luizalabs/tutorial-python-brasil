# 🦸 Técnicas (um pouco) mais avançadas

## 🚱 Rate limit
### O que é ?
Rate Limit é a limitação de solicitação entre um controlador de origem e uma interface destino. No mundo de serviços web podemos dizer que Rate Limit é a limitação de requisições de um usuário (client) para uma WebAPI.

### Quando utilizar
Utiliza a estratégia de Rate Limit no ambiente de WebAPIs para evitar ataques de invasores, quando o mesmo fica explorando as vulnerabilidades de segurança do sistema para infectar e controlar máquinas e dispositivos. 

### Dicas / Links / Ferramentas
- https://pypi.org/project/fastapi-limiter/
- https://pypi.org/project/slowapi/


## 🔒 Autenticação e Autorização
### O que é ?
Autenticação é o processo do sistema para verificar a identidade virtual do usuário o client, normalmente baseado em um login e senha. Autorização é o processo que permite o usuário ou client acessar uma ou mais funcionalidades e recursos do sistema.

### Quando utilizar?
Colocar um processo de Autenticação na sua é WebAPI reforçar a segurança da mesma evitando que usuários maliciosos consigam acessá-la e causar algum impacto no sistema. O processo de Autorização vem na sequência, a importância de adotar esse processo é que mesmo os usuários que consigam se autenticar não necessariamente eles terão acessos às informações e recursos. Na Autorização você consegue limitar o usuário nos acessos aos recursos e os dados do sistema.

### Dicas / Links / Ferramentas
- https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/
- https://pypi.org/project/python-oauth2/
- https://pypi.org/project/python-openid/
- https://www.keycloak.org/


## 🗺️ Hateoas
### O que é ?
Hateoas (Hypermedia As the Engine Of Application State) vem da palavra Hypermedia, onde os documentos são integrados através de links. Ou seja, quando clicamos em uma frase ou imagem em um site e é direcionado para outra página essa ação acontece de forma implicita ao usuário e utilizando hyperlink. Em WebAPIs é a capacidade de linkar recursos através de links dentro do documento json. Os clients não precisam conhecer as URLs de recursos, apenas de entrypoint. Ou seja, a API passa a fornecer links em atributos json que indicarão aos clients como navegar através dos seus recursos. 

### Quando utilizar?
A utilização de Hateoas acontece quando o Frontend (client) não precisa ter as regras para saber consumir as API. Pois, no próprio documento json tem os atributos existentes com os possíveis links para a navegação dos próximos recursos. Isso é importante quando temos APIs abertas e os clients não conhecem as regras de negócio do server (backend). Também podemos utilizar em times grandes que trabalham provendo recursos para várias equipes através de WebAPIs. 

### Dicas / Links / Ferramentas
- https://restful-api-design.readthedocs.io/en/latest/urls.html
- https://pypi.org/project/ripozo/


## 📰 Log
### O que é ?
Log nada mais é que a apresentação das informações de etapas percorridas do sistema ou ações que o algorítmo executou em algum processo. Essas informações são  registros que ficam gravados em arquivos e ajudam a identificar o comportamento do sistema e até identificação de erros.

### Quando utilizar?
Sempre! Mas depende do tipo de log. Isso mesmo que você leu, depende do tipo ou o termo correto nível de log e o ambiente que a aplicação está. Na fase de desenvolvimento utiliza-se o log no nível debug, esse nível ajuda a percorrer o algorítmo com maior frequência e acompanhar em detalhes. Em ambientes de teste e de produção utiliza o log no nível de erro ou info. Esses níveis possibilitam ter os registros de erros da aplicação ou alguma informação relevante, sem poluir os registros.

### Dicas / Links / Ferramentas
- https://docs.python.org/3/library/logging.html
- https://www.geeksforgeeks.org/logging-in-python/


## 📄 Paginação
### O que é ?
Paginação é a estratégia de dividir em páginas as informações solicitadas. Em WebAPI é a capacidade de dividir em partes a quantidade de informações retornada da requisição realizada. Sendo que a cada requisição solicitará a informação da página e o retorno é referente a quantidade configurada, não precisando retornar todas as informações. 

### Quando utilizar?
Normalmente é utilizado em recursos que provê uma listagem de resultados. Esse recurso, por padrão, exige um alto processamento para retornar todas as informações e consequentemente sobrecarrega o processamento da rede. Para isso é aplicado a paginação em sua API especificando apenas a quantidade limite de cada página.

### Dicas / Links / Ferramentas
- https://uriyyo-fastapi-pagination.netlify.app/
- https://fastapi.tiangolo.com/pt/tutorial/query-params/?h=limit
- https://alpha.dev.magalu.com/apis/maestro

## 🗄️ Cache
### O que é ?
É o local de armazenamento de dados temporários que pode ser acessado sem a necessidade de I/O ou utilização de recursos de rede.

### Quando utilizar?
Quando precisa obter dados com frequência e que não mudam. Caso adote a estratégia de um Banco de Dados a operação será vinculada um I/O, utilização de recursos de rede e afeta o desempenho da aplicação. Adotando uma estratégia de cache da aplicação, além de não necessitar os pontos anteriores, há uma melhora de performance do sistema. Esses dados podem ser como token de sessão, código de identificação (id) de entidade, nome de usuário ou qualquer outro dado que será usada constatemente pelo algorítimo e não sofrerá alteração.

### Dicas / Links / Ferramentas
- https://github.com/long2ice/fastapi-cache
- https://docs.python.org/pt-br/3.10/library/functools.html
- https://medium.com/fintechexplained/advanced-python-how-to-implement-caching-in-python-application-9d0a4136b845


## 🧠 Memória Compartilhada (nível avançado)
### O que é ?
É o compartilhamento de dados em objeto de memória entre threads e pods, utilizando apenas um único recurso para este dado. Ou seja, um respectivo dado foi armazenado em disco alocando um determinado tamanho de memória. Este mesmo dado poderá ser compartilhado por _n_ threads (processos) da mesma aplicação ou em pods diferente do mesmo recurso. Não tendo a necessidade de realizar alocações de memórias em diversos processamento repetindo o mesmo dado.

### Quando utilizar?
Quando tiver a necessidade de um dado ser acessado para leitura por alguns processos. Como, por exemplo, para a thread obter um token de client credential ao invés de ir no _vault_ poderá ser compartilhado através de _shared memory_ (sem ttl). 

### Dicas / Links / Ferramentas
- https://github.com/luizalabs/shared-memory-dict
- https://docs.python.org/3/library/multiprocessing.shared_memory.html
- https://docs.python.org/2/library/multiprocessing.html#sharing-state-between-processes


## ⚙️ Tarefa em Background (worker, mensageria, tópicos)
### O que é ?
Tarefas em background podem ser consideradas como tarefas assíncronas. Os processos assíncronos são processos que não dependem de uma resposta da realização da tarefa, como vemos em uma requisição de uma WebAPI, e são normalmente orientadas a mensagens e eventos. 

### Quando utilizar?
A utilização de tarefa em background pode ser utilizado para processar dados em lotes, leituras de arquivos, processos com muitas integrações de recursos e serviços, e tarefas que deverão ser executadas periodicamente em processos agendados.

### Dicas / Links / Ferramentas
- https://kafka.apache.org/
- https://www.rabbitmq.com/
- https://kafka-python.readthedocs.io/en/master/usage.html
- https://pika.readthedocs.io/en/0.10.0/



[Referências e Dicas ➡️](referencias.md)

[⬅️ Circuit breaker](breaker.md)

[↩️ Voltar ao README ](README.md)
