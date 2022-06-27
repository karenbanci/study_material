const Edge = require("./Edge.js");
const Vertex = require("./Vertex.js");

class Graph {
  // Quando a Graphé criada pela primeira vez, precisamos de uma maneira de identificar se ela será direcionada ou não.
  constructor(isWeighted = false, isDirected = false) {
    this.vertices = [];
    this.isWeighted = isWeighted;
    // isDirectedPor padrão, isDirecteddeve ser definido como false.
    this.isDirected = isDirected;
  }

  addVertex(data) {
    // criar nova instancia de Vertex
    const newVertex = new Vertex(data);
    // adicionar a graph lista de vertices
    this.vertices.push(newVertex);

    return newVertex;
  }

  removeVertex(vertex) {
    // remova o vértice que é estritamente igual ao vértice dado no parâmetro.
    this.vertices = this.vertices.filter((v) => v !== vertex);
  }

  addEdge(vertexOne, vertexTwo, weight) {
    const edgeWeight = this.isWeighted ? weight : null;

    if (vertexOne instanceof Vertex && vertexTwo instanceof Vertex) {
      vertexOne.addEdge(vertexTwo, edgeWeight);

      if (!this.isDirected) {
        vertexTwo.addEdge(vertexOne, edgeWeight);
      }
    } else {
      throw new Error("Expected Vertex arguments.");
    }
  }

  // remove a aresta entre dois vértices fornecidos.
  removeEdge(vertexOne, vertexTwo) {
    if (vertexOne instanceof Vertex && vertexTwo instanceof Vertex) {
      vertexOne.removeEdge(vertexTwo);

      if (!this.isDirected) {
        vertexTwo.removeEdge(vertexOne);
      }
    } else {
      throw new Error("Expected Vertex arguments.");
    }
  }

  print() {
    this.vertices.forEach((vertex) => vertex.print());
  }
}

module.exports = Graph;
