# Search depth

font: codecademy

## One path

Vamos nos concentrar em percorrer todo o comprimento de um caminho e registrar o datavalor de cada vértice.

Para simplificar, implementaremos o iterador de travessia como uma função separada em vez de um método na Graphclasse. Em outras implementações, o iterador pode ser visto como um método de classe.

Também configuramos um gráfico de amostra em testGraph.js para você testar as travessias. Sinta-se à vontade para dar uma olhada no arquivo para se familiarizar com a estrutura do gráfico.

## All paths

Nós pegamos o jeito de percorrer um caminho, mas queremos percorrer todos os caminhos (não apenas o primeiro caminho possível). Modificaremos nossa implementação existente para iterar todos os outros caminhos usando um .forEach()loop para iterar por todos os startvértices edges.

Não teremos que nos preocupar em iterar por todos os vizinhos antes de descer o primeiro vértice conectado do vizinho. Isso ocorre porque a chamada recursiva ocorre antes da próxima iteração do loop for.

## Callback

Nossa implementação atual da travessia em profundidade simplesmente imprime os vértices do gráfico à medida que são percorridos. Isso seria útil em cenários em que queremos ver a ordem em que a travessia ocorre. Por exemplo, se o gráfico for uma lista de instruções, precisamos da ordem exata em que as etapas ocorrerão para determinar quais dependências precisam ser resolvidas primeiro.

No entanto, pode haver outras instâncias em que queremos fazer algo além de imprimir a ordem de passagem. Por exemplo, se precisamos apenas determinar se existe um caminho, como ver se um labirinto é solucionável, precisamos apenas de um valor verdadeiro ou falso. Podemos fazer isso abrindo um parâmetro de retorno de chamada para o usuário.
