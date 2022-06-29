const mergeSort = (startArray) => {
  // pegando o tamanho da array
  const length = startArray.length;
  // se o tamanho for maior que 1
  if (length === 1) {
    return startArray;
  }
  // cortando array pela metade
  const mid = Math.floor(length / 2);
  // to dizendo que a primeira metade vai para o lado esquerdo
  const leftArray = startArray.slice(0, mid);
  // to dizendo que a segunda metade vai para o lado direito
  const rightArray = startArray.slice(mid, length);

  // aqui estou retornando a array mesclada
  return merge(mergeSort(leftArray), mergeSort(rightArray));
};

const merge = (leftArray, rightArray) => {

  const sortedArray = [];

  // enquanto houver elementos na lista (esquerda e direita)
  while (leftArray.length > 0 && rightArray.length > 0) {
    // se o primeiro elemento da esquerda for menor que o primeiro elemento da direita
    if (leftArray[0] < rightArray[0]) {
      // vou adicionar ele na lista da array ordenada
      sortedArray.push(leftArray[0]);
      // e remover ele da leftArray
      leftArray.shift(leftArray[0]);
    } else {
      sortedArray.push(rightArray[0]);
      rightArray.shift(rightArray[0]);
    }
  }

  // depois de tudo terminado, vou concatenar a lista
  return sortedArray.concat(leftArray).concat(rightArray);
};

const inputArr = [3, 5, 2, 90, 4, 7];

console.log(mergeSort(inputArr));

module.exports = {
  mergeSort,
};
