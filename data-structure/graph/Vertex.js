const Edge = require("./Edge.js");

class Vertex {
  constructor(data) {
    this.data = data;
    this.edges = [];
  }

  addEdge(vertex, weight) {
    if (vertex instanceof Vertex) {
      this.edges.push(new Edge(this, vertex, weight));
    } else {
      throw new Error("Edge start and end must both be Vertex");
    }
  }

  // que gerenciemos sua própria remoção de vértices, assim como ele lida com sua própria criação de vértices.
  removeEdge(vertex) {
    // itere através de sua lista edgese filtre a propriedade Edgecujo endé estritamente igual ao final vertex.
    this.edges = this.edges.filter((edge) => edge.end !== vertex);
  }

  print() {
    const edgeList = this.edges.map((edge) =>
      edge.weight !== null ? `${edge.end.data} (${edge.weight})` : edge.end.data
    );

    const output = `${this.data} --> ${edgeList.join(", ")}`;
    console.log(output);
  }
}

module.exports = Vertex;
