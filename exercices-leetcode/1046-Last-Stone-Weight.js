/*Você recebe uma matriz de números inteiros stonesonde stones[i]é o peso da pedra.ith

Estamos fazendo um jogo com as pedras. Em cada turno, escolhemos as duas pedras mais pesadas e as esmagamos juntas. Suponha que as duas pedras mais pesadas tenham pesos x e y com x <= y. O resultado desse golpe é:

Se x == y, ambas as pedras forem destruídas, e
Se x != y, a pedra de peso xé destruída, e a pedra de peso ytem novo peso y - x.
No final do jogo, resta no máximo uma pedra.

Devolva o peso da última pedra restante . Se não houver mais pedras, devolva 0.



Exemplo 1:

Entrada: pedras = [2,7,4,1,8,1]
 Saída: 1
 Explicação:
Combinamos 7 e 8 para obter 1 para que a matriz seja convertida em [2,4,1,1,1] então,
combinamos 2 e 4 para obter 2 para que a matriz seja convertida em [2,1,1,1] então,
combinamos 2 e 1 para obter 1 para que a matriz seja convertida em [1,1,1] então,
combinamos 1 e 1 para obter 0 para que a matriz seja convertida em [1], então esse é o valor da última pedra. */


var lastStoneWeight = function (stones) {
  const numbersQueue = new MinPriorityQueue();
};
