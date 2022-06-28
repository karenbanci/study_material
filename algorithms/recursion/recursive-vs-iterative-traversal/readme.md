# Introdução

Nesta lição, você aprenderá como implementar uma solução recursiva para uma pesquisa de lista vinculada. O método aceita um valor como entrada e verifica recursivamente cada nó na lista encadeada, até que o nó de interesse seja encontrado. Se for encontrado, o método deve retornar o nó. Caso contrário, deve retornar null

* **Caso base 1** – retorna o nó atual se corresponder ao argumento de dados.

* **Caso base 2** – retorna null se o final da lista encadeada for atingido.

* **Caso base 3** – retorna uma chamada para .findNodeRecursively()com o próximo nó como argumento.

A abordagem recursiva apresentada nesta lição é semelhante às implementações para percorrer outras estruturas de dados, como árvores e diretórios. Esse é um insight importante a ser lembrado à medida que você encontra implementações mais recursivas.
