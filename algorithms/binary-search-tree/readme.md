# Introdução

fonte: Codecademy

Uma árvore binária é uma estrutura de dados eficiente para armazenamento e recuperação de dados rápidos devido ao seu tempo de O(log N)execução. É uma estrutura de dados de árvore especializada que é composta por um nó raiz e, no máximo, duas ramificações ou subárvores filhas. Cada nó filho é em si uma árvore binária.

Cada nó tem as seguintes propriedades:

* dados

* um valor de profundidade, onde a profundidade de 1 indica o nível superior da árvore e uma profundidade maior que 1 é um nível em algum lugar mais baixo na árvore

* um ponteiro esquerdo que aponta para um filho esquerdo que é em si uma árvore binária e deve ter um dado menor que os dados do nó raiz

* um ponteiro direito que aponta para um filho direito que é em si uma árvore binária e deve ter dados maiores que os dados do nó raiz

![Tree](introducao.png)

## Inserindo valores

Ao inserir um novo valor em uma árvore binária, comparamos com o valor do nó raiz:

If the new value is less than the root node's value
  If a left child node doesn't exist
    Create a new BinaryTree with the new value at a greater depth and assign it to the left pointer
  Else
    Recursively call .insert() on the left child node
Else
  If a right child node doesn't exist
    Create a new BinaryTree with the new value at a greater depth and assign it to a right pointer
  Else
    Recursively call .insert() on the right child node

Vamos ilustrar o procedimento de inserção com uma árvore cujo nó raiz possui os dados 100.

Insert 50
50 < 100, left child node doesn't exist, create a left child node
       100
       /
     50
Insert 125
125 > 100, right child node doesn't exist, create a right child node
        100
       /   \
      50    125
Insert 75
75 < 100, left child node of 50 exists, recursive insert at left child
75 > 50, right child node doesn't exist, create a right child node
        100
       /   \
      50    125
       \
       75
Insert 25
25 < 100, left child node of 50 exists, recursive insert at left child
25 < 50, left child node doesn't exist, create a left child node
        100
       /   \
      50    125
     /  \
    25  75
