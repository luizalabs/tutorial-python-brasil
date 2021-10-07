# 💭 Planejando o que será desenvolvido 

<p align="center">
  <img style="float: right;" src="imgs/projeto.png" alt="Homem a frente de website de compras com caixas ao lado"/>
</p>

> ⚠️ O sistema desenvolvido é apenas para fins de treinamento e desenvolvimento das técnicas apresentadas. Aprenda as técnicas e certifique-se que são adequadas para o seu sistema.

## 🛍️ O que será desenvolvido?

Será desenvolvido um sistema com objetivo de obter informações a respeito de pedidos.

Os pedidos serão obtidos através de integração com o sistema de pedidos do **[Magalu](https://www.magazineluiza.com.br/)**.

Vamos fazer o enriquecimento desta informação antes de sua exibição e também iremos prover alguns dados estatísticos sobre o pedido.

Um pedido possui vários pacotes, cada um deles contendo itens.

Este sistema deve seguir as seguintes regras:

* Deve apresentar uma interface que possa ser consumida tanto por um website, quanto por um aplicativo para dispositivos móveis;

* Deve prover um _endpoint_ que indique a saúde do sistema;

* Para cada pacote de um pedido, retornar o seu prazo de entrega;

* Dado um pedido, retornar os seus itens;

* Os itens de um pedido devem conter um idntificador (sku), uma descrição, uma imagem, uma referência e a quantidade.

* Exibir um relatório com o total de métodos de pagamento utilizados por um cliente;

* Como será consumido por terceiros deve apresentar boa documentação;

* O sistema deve apresentar testes.

😨 E agora, o que fazer? Por onde começo? Vamos escolher nossas ferramentas!

[Escolhendo as melhores ferramentas ➡️](ferramentas.md)

[↩️ Voltar ao README ](README.md)