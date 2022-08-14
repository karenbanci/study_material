/**
 * Definition for a binary tree node.

 */
/**
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {boolean}
 */

function TreeNode(val, left, right) {
  this.val = val === undefined ? 0 : val;
  this.left = left === undefined ? null : left;
  this.right = right === undefined ? null : right;
}

var isSameTree = function (p, q) {
  if (p && q) {
    // compara o valor da raiz
    if (p.val === q.val) {
      // comparar os valores do nó à esquerda, se existir valor
      if (p.left === null && q.left === null) {
        // os dois são nulos
        console.log('os dois esquerdos sao nulos')
      } else if (p.left === null || q.left === null) {
        // um dos dois é nulo
        console.log("linha 26");
        return false;
      }

      // comparar os valores do nó à direita, se existir valor
      if (p.right === null && q.right === null) {
        // os dois são nulos
        console.log("os dois direitos sao nulos");

      } else if (p.right === null || q.right === null) {
        // um dos dois é nulo
        console.log("linha 34");
        return false;
      }
      // aqui vamos conferir as arvores - aqui estou fazendo a recursividade, chamando a funcao desde  o primeiro if de novo
      console.log('condicao de repetição recursiva', p.left, q.left)
      if (isSameTree(p.left, q.left)) {

        if (isSameTree(p.right, q.right)) {
          return true;

        } else {
          console.log('linha 42');
          return false;
        }
      } else {
        console.log("linha 48");
        return false;
      }
    } else {
      return false;
    }

  } else if(!p && !q) {
    return true;
  } else {
    return false
  }
};

// código simplificado
/*var isSameTree = function(p, q) {
    if (!p && !q) {
        return true;
    }
    if (!p || !q || p.val !== q.val) {
        return false;
    }
    return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
}; */



console.log("CASO nuloss -------------------------------");
console.log(isSameTree(null, null));


console.log("CASO A -------------------------------");
const casoA1 = new TreeNode(
  1,
  new TreeNode(2, null, null),
  new TreeNode(3, null, null)
);
const casoA2 = new TreeNode(
  1,
  new TreeNode(2, null, null),
  new TreeNode(3, null, null)
);
console.log("esperado: true");
console.log(isSameTree(casoA1, casoA2));

console.log("---- CASO B ---------------------------");
const casoB1 = new TreeNode(1, null, new TreeNode(2, null, null));
const casoB2 = new TreeNode(1, new TreeNode(2, null, null), null);
console.log("esperado: false");
console.log(isSameTree(casoB1, casoB2));

console.log("----------- CASO C --------------------");
const casoC1 = new TreeNode(
  1,
  new TreeNode(2, null, null),
  new TreeNode(3, null, null)
);
const casoC2 = new TreeNode(
  1,
  new TreeNode(3, null, null),
  new TreeNode(2, null, null)
);
console.log("esperado: false");
console.log(isSameTree(casoC1, casoC2));

console.log("-------------------- CASO D -----------");
const casoD1 = new TreeNode(
  1,
  new TreeNode(2, null, null),
  new TreeNode(3, null, null)
);
const casoD2 = new TreeNode(
  1,
  new TreeNode(2, null, null),
  new TreeNode(4, null, null)
);
console.log("esperado: false");
console.log(isSameTree(casoD1, casoD2));

console.log("--------------------------- CASO E ----");
const casoE1 = new TreeNode(
  1,
  new TreeNode(2, null, null),
  null
);
const casoE2 = null;
console.log("esperado: false");
console.log(isSameTree(casoE1, casoE2));

console.log("------------------------------- CASO F");
const casoF1 = new TreeNode(
  1,
  new TreeNode(2, new TreeNode(3, null, null)),
  new TreeNode(4, null, null)
);
const casoF2 = new TreeNode(
  1,
  new TreeNode(2, new TreeNode(5, null, null), null),
  new TreeNode(4, null, null)
);
console.log("esperado: false");
console.log(isSameTree(casoF1, casoF2));

console.log("------------------------------- CASO G");
const casoG1 = new TreeNode(
  2,
  new TreeNode(2, new TreeNode(3, null, null)),
  new TreeNode(4, null, null)
);
const casoG2 = new TreeNode(
  1,
  new TreeNode(2, new TreeNode(5, null, null), null),
  new TreeNode(4, null, null)
);
console.log("esperado: false");
console.log(isSameTree(casoG1, casoG2));
