# Breadth Traversal

font: codecademy

## First Layers

A largura primeiro itera por todo o gráfico em camadas, descendo uma camada, que compreende os start vizinhos diretos do vértice. Em seguida, desce para a próxima camada, que consiste em todos os vértices vizinhos dos vértices da camada anterior.

Para este exercício, vamos nos concentrar em percorrer uma camada. Usaremos uma abordagem semelhante à que fizemos com a travessia em profundidade, mantendo uma matriz de visitedVertices para nos impedir de iterar pelos mesmos vértices.

No entanto, vamos iterar por todos os vértices vizinhos diretos em vez de iterar pela primeira aresta do vizinho. Também usaremos uma fila para percorrer o gráfico em vez de recursão para explorar as diferentes maneiras de implementar as travessias.


## All Layers

Até agora, podemos iterar uma camada, mas ainda temos que iterar as camadas restantes. Para isso, introduziremos uma fila que acompanhará todos os vértices a serem visitados.

À medida que iteramos pelo neighbors, adicionaremos seus vértices conectados ao final da fila, retiraremos o próximo neighborda fila, adicionaremos seus vértices conectados e assim por diante. Desta forma, permite-nos manter a ordem de visitas; visitaremos os vértices da mesma camada enquanto enfileiramos a próxima camada. Quando não há vértices restantes na camada atual, os vértices da próxima camada já estão enfileirados, então descemos e iteramos pela próxima camada.

Usaremos nossa implementação da Queueestrutura de dados que foi abordada em um curso anterior. Ele está localizado em Queue.js . Vá em frente e dê uma olhada rápida para atualizar sua memória da estrutura de dados e dos métodos disponíveis.
